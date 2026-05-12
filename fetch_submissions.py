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
            return {"codeforces_max_id": 0}
    return {"codeforces_max_id": 0}

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

def merge_submissions(new_subs, existing_subs):
    """Merge new submissions with existing ones, avoiding duplicates"""
    if not existing_subs:
        return new_subs
    
    # Create a set of existing submission IDs
    existing_ids = {s['id'] for s in existing_subs}
    # Add only new submissions
    for sub in new_subs:
        if sub['id'] not in existing_ids:
            existing_subs.append(sub)
    
    # Sort by ID (descending to match original format)
    existing_subs.sort(key=lambda x: x['id'], reverse=True)
    
    return existing_subs

def filter_accepted(submissions):
    """Filter only accepted solutions from Codeforces"""
    return [s for s in submissions if s.get('verdict') == 'OK']

def save_submissions(submissions, platform, output_dir):
    """Save submissions to JSON file"""
    output_path = Path(output_dir) / f"{platform}_submissions.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(submissions, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved {len(submissions)} submissions to {output_path}")

def generate_accepted_markdown(submissions, output_dir, username, contests=None):
    """Generate markdown table with only accepted solutions"""
    output_path = Path(output_dir) / "codeforces_accepted.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not submissions:
        # Create empty file with placeholder message
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# Codeforces - Accepted Solutions ({username})\n\n")
            f.write(f"No accepted solutions found yet.\n")
        print(f"✓ Generated empty markdown: {output_path}")
        return
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Codeforces - Accepted Solutions ({username})\n\n")
        f.write(f"Total Accepted: **{len(submissions)}**\n\n")
        f.write("| # | Problem | Rating | Contest | Date | Solution |\n")
        f.write("|---|---------|--------|---------|------|----------|\n")
        
        for i, sub in enumerate(submissions, 1):
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
            
            f.write(f"| {i} | {problem} | {rating} | {contest_name} | {time} | {solution_link} |\n")
    
    print(f"✓ Generated markdown: {output_path}")

def main():
    print("Fetching Codeforces submissions...\n")
    
    codeforces_username = "Ayon"
    base_dir = "submissions"
    
    # Load previous state
    state = load_state()
    print(f"Previous state - Codeforces max ID: {state['codeforces_max_id']}\n")
    
    # Load existing submissions
    cf_existing = []
    
    cf_path = Path(f"{base_dir}/codeforces/codeforces_submissions.json")
    if cf_path.exists():
        with open(cf_path, 'r', encoding='utf-8') as f:
            cf_existing = json.load(f)
    
    # Fetch Codeforces
    try:
        print(f"Fetching Codeforces ({codeforces_username})...")
        cf_subs = fetch_codeforces_submissions(codeforces_username)
        
        # Merge with existing
        cf_all = merge_submissions(cf_subs, cf_existing)
        
        print(f"Fetching Codeforces contest details...")
        contests = fetch_codeforces_contests()
        
        cf_accepted = filter_accepted(cf_all)
        print(f"  → Total: {len(cf_all)}, Accepted: {len(cf_accepted)}\n")
    except Exception as e:
        print(f"✗ Codeforces fetch failed: {e}\n")
        cf_all = cf_existing
        cf_accepted = filter_accepted(cf_existing)
        contests = {}
    
    # Update state
    if cf_all and len(cf_all) > 0:
        state['codeforces_max_id'] = max(cf_all, key=lambda x: x['id'])['id']
    
    # Save submissions
    print("Saving submissions...")
    save_submissions(cf_all, 'codeforces', f"{base_dir}/codeforces")
    save_submissions(cf_accepted, 'codeforces_accepted', f"{base_dir}/codeforces")
    
    # Save state
    save_state(state)
    
    print("\nGenerating markdown table...")
    generate_accepted_markdown(cf_accepted, base_dir, codeforces_username, contests)
    
    print("\n✓ All submissions fetched and merged!")
    print(f"\n📊 Summary:")
    print(f"  Codeforces - Total: {len(cf_all)}, Accepted: {len(cf_accepted)}")

if __name__ == "__main__":
    main()


