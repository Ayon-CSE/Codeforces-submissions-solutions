#!/usr/bin/env python3
import json
import urllib.request
import os
from datetime import datetime
from pathlib import Path

def load_state():
    """Load the last fetched submission state"""
    state_file = Path("submissions/state.json")
    if state_file.exists():
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {"codeforces_max_id": 0, "atcoder_max_id": 0}
    return {"codeforces_max_id": 0, "atcoder_max_id": 0}

def save_state(state):
    """Save the current fetch state"""
    state_file = Path("submissions/state.json")
    state_file.parent.mkdir(parents=True, exist_ok=True)
    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2)

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

def merge_submissions(new_subs, existing_subs, platform):
    """Merge new submissions with existing ones, avoiding duplicates"""
    if not existing_subs:
        return new_subs
    
    # Create a set of existing submission IDs
    if platform == 'codeforces':
        existing_ids = {s['id'] for s in existing_subs}
        # Add only new submissions
        for sub in new_subs:
            if sub['id'] not in existing_ids:
                existing_subs.append(sub)
    else:  # atcoder
        existing_ids = {s['id'] for s in existing_subs}
        for sub in new_subs:
            if sub['id'] not in existing_ids:
                existing_subs.append(sub)
    
    # Sort by ID/time (descending to match original format)
    if platform == 'codeforces':
        existing_subs.sort(key=lambda x: x['id'], reverse=True)
    else:
        existing_subs.sort(key=lambda x: x['id'], reverse=True)
    
    return existing_subs

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
    output_path = Path(output_dir) / f"{platform}_accepted.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not submissions:
        # Create empty file with placeholder message
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# {platform.capitalize()} - Accepted Solutions ({username})\n\n")
            f.write(f"No accepted solutions found yet.\n")
        print(f"✓ Generated empty markdown: {output_path}")
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
    print("Fetching new submissions...\n")
    
    codeforces_username = "Ayon"
    atcoder_username = "AyonCoder"
    base_dir = "submissions"
    
    # Load previous state
    state = load_state()
    print(f"Previous state - Codeforces max ID: {state['codeforces_max_id']}, AtCoder max ID: {state['atcoder_max_id']}\n")
    
    # Load existing submissions
    cf_existing = []
    at_existing = []
    
    cf_path = Path(f"{base_dir}/codeforces/codeforces_submissions.json")
    if cf_path.exists():
        with open(cf_path, 'r', encoding='utf-8') as f:
            cf_existing = json.load(f)
    
    at_path = Path(f"{base_dir}/atcoder/atcoder_submissions.json")
    if at_path.exists():
        with open(at_path, 'r', encoding='utf-8') as f:
            at_existing = json.load(f)
    
    # Fetch Codeforces
    try:
        print(f"Fetching Codeforces ({codeforces_username})...")
        cf_subs = fetch_codeforces_submissions(codeforces_username)
        
        # Merge with existing
        cf_all = merge_submissions(cf_subs, cf_existing, 'codeforces')
        
        print(f"Fetching Codeforces contest details...")
        contests = fetch_codeforces_contests()
        
        cf_accepted = filter_accepted(cf_all, 'codeforces')
        print(f"  → Total: {len(cf_all)}, Accepted: {len(cf_accepted)}\n")
    except Exception as e:
        print(f"✗ Codeforces fetch failed: {e}\n")
        cf_all = cf_existing
        cf_accepted = filter_accepted(cf_existing, 'codeforces')
        contests = {}
    
    # Fetch AtCoder (non-critical)
    try:
        print(f"Fetching AtCoder ({atcoder_username})...")
        at_subs = fetch_atcoder_submissions(atcoder_username)
        
        # Merge with existing
        at_all = merge_submissions(at_subs, at_existing, 'atcoder')
        at_accepted = filter_accepted(at_all, 'atcoder')
        print(f"  → Total: {len(at_all)}, Accepted: {len(at_accepted)}\n")
    except Exception as e:
        print(f"⚠ AtCoder fetch failed (non-critical): {e}\n")
        at_all = at_existing
        at_accepted = filter_accepted(at_existing, 'atcoder')
    
    # Update state
    if cf_all:
        state['codeforces_max_id'] = max(cf_all, key=lambda x: x['id'])['id']
    if at_all:
        state['atcoder_max_id'] = max(at_all, key=lambda x: x['id'])['id']
    
    # Save and generate
    print("Saving submissions...")
    save_submissions(cf_all, 'codeforces', f"{base_dir}/codeforces")
    save_submissions(at_all, 'atcoder', f"{base_dir}/atcoder")
    save_submissions(cf_accepted, 'codeforces_accepted', f"{base_dir}/codeforces")
    save_submissions(at_accepted, 'atcoder_accepted', f"{base_dir}/atcoder")
    
    # Save state
    save_state(state)
    
    print("\nGenerating markdown tables...")
    generate_accepted_markdown(cf_accepted, 'codeforces', base_dir, codeforces_username, contests)
    generate_accepted_markdown(at_accepted, 'atcoder', base_dir, atcoder_username)
    
    print("\n✓ All submissions fetched and merged!")
    print(f"\n📊 Summary:")
    print(f"  Codeforces - Total: {len(cf_all)}, Accepted: {len(cf_accepted)}")
    print(f"  AtCoder - Total: {len(at_all)}, Accepted: {len(at_accepted)}")

if __name__ == "__main__":
    main()


