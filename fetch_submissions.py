#!/usr/bin/env python3
import json
import urllib.request
import os
from datetime import datetime
from pathlib import Path

def fetch_codeforces_submissions(username):
    """Fetch all Codeforces submissions for a user"""
    try:
        url = f"https://codeforces.com/api/user.status?handle={username}"
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        if data.get('status') == 'OK':
            submissions = data.get('result', [])
            print(f"✓ Fetched {len(submissions)} Codeforces submissions for {username}")
            return submissions
        else:
            print(f"✗ Error fetching Codeforces: {data.get('comment', 'Unknown error')}")
            return []
    except Exception as e:
        print(f"✗ Error fetching Codeforces: {e}")
        return []

def fetch_codeforces_contests():
    """Fetch contest information from Codeforces"""
    try:
        url = "https://codeforces.com/api/contest.list"
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        if data.get('status') == 'OK':
            contests = {c['id']: c for c in data.get('result', [])}
            print(f"✓ Fetched {len(contests)} contest details")
            return contests
        else:
            return {}
    except Exception as e:
        print(f"✗ Error fetching contests: {e}")
        return {}

def fetch_atcoder_submissions(username):
    """Fetch all AtCoder submissions for a user"""
    try:
        url = f"https://atcoder.jp/api/v2/users/{username}/submissions?limit=10000"
        with urllib.request.urlopen(url, timeout=10) as response:
            submissions = json.loads(response.read().decode())
        
        print(f"✓ Fetched {len(submissions)} AtCoder submissions for {username}")
        return submissions
    except Exception as e:
        print(f"✗ Error fetching AtCoder: {e}")
        return []

def filter_accepted(submissions, platform):
    """Filter only accepted solutions"""
    if platform == 'codeforces':
        return [s for s in submissions if s.get('verdict') == 'OK']
    else:  # atcoder
        return [s for s in submissions if s.get('result') == 'AC']

def save_submissions(submissions, platform, output_dir):
    """Save submissions to JSON file"""
    output_path = Path(output_dir) / f"{platform}_submissions.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(submissions, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved {len(submissions)} submissions to {output_path}")

def generate_accepted_markdown(submissions, platform, output_dir, username, contests=None):
    """Generate markdown table with only accepted solutions"""
    if not submissions:
        return
    
    output_path = Path(output_dir) / f"{platform}_accepted.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {platform.capitalize()} - Accepted Solutions ({username})\n\n")
        f.write(f"Total Accepted: **{len(submissions)}**\n\n")
        f.write("| # | Problem | Rating | Contest | Date | Solution |\n")
        f.write("|---|---------|--------|---------|------|----------|\n")
        
        for i, sub in enumerate(submissions, 1):
            if platform == 'codeforces':
                problem = sub.get('problem', {}).get('name', 'N/A')
                rating = sub.get('problem', {}).get('rating', '?')
                problem_id = sub.get('problem', {}).get('index', '')
                contest_id = sub.get('contestId', '')
                
                # Get contest name
                contest_name = 'N/A'
                if contests and contest_id in contests:
                    contest_name = contests[contest_id].get('name', f'Contest {contest_id}')
                else:
                    contest_name = f'Contest {contest_id}'
                
                time = datetime.fromtimestamp(sub.get('creationTimeSeconds', 0)).strftime('%Y-%m-%d')
                submission_id = sub.get('id', '')
                solution_link = f"[View](https://codeforces.com/contest/{contest_id}/submission/{submission_id})"
            else:  # atcoder
                problem = sub.get('problem', {}).get('title', 'N/A')
                rating = '-'
                contest = sub.get('contest_id', 'N/A')
                contest_name = contest
                time = sub.get('epoch_second', 0)
                if time:
                    time = datetime.fromtimestamp(time).strftime('%Y-%m-%d')
                submission_id = sub.get('id', '')
                solution_link = f"[View](https://atcoder.jp/contests/{contest}/submissions/{submission_id})"
            
            f.write(f"| {i} | {problem} | {rating} | {contest_name} | {time} | {solution_link} |\n")
    
    print(f"✓ Generated markdown: {output_path}")

def main():
    print("Fetching all submissions...\n")
    
    codeforces_username = "Ayon"
    atcoder_username = "AyonCoder"
    base_dir = "submissions"
    
    # Fetch Codeforces
    print(f"Fetching Codeforces ({codeforces_username})...")
    cf_subs = fetch_codeforces_submissions(codeforces_username)
    
    print(f"Fetching Codeforces contest details...")
    contests = fetch_codeforces_contests()
    
    cf_accepted = filter_accepted(cf_subs, 'codeforces')
    print(f"  → {len(cf_accepted)} accepted solutions\n")
    
    # Fetch AtCoder
    print(f"Fetching AtCoder ({atcoder_username})...")
    at_subs = fetch_atcoder_submissions(atcoder_username)
    at_accepted = filter_accepted(at_subs, 'atcoder')
    print(f"  → {len(at_accepted)} accepted solutions\n")
    
    # Save and generate
    print("Saving submissions...")
    save_submissions(cf_subs, 'codeforces', f"{base_dir}/codeforces")
    save_submissions(at_subs, 'atcoder', f"{base_dir}/atcoder")
    save_submissions(cf_accepted, 'codeforces_accepted', f"{base_dir}/codeforces")
    save_submissions(at_accepted, 'atcoder_accepted', f"{base_dir}/atcoder")
    
    print("\nGenerating markdown tables...")
    generate_accepted_markdown(cf_accepted, 'codeforces', base_dir, codeforces_username, contests)
    generate_accepted_markdown(at_accepted, 'atcoder', base_dir, atcoder_username)
    
    print("\n✓ All submissions fetched and saved!")
    print(f"\n📊 Summary:")
    print(f"  Codeforces - Total: {len(cf_subs)}, Accepted: {len(cf_accepted)}")
    print(f"  AtCoder - Total: {len(at_subs)}, Accepted: {len(at_accepted)}")

if __name__ == "__main__":
    main()


