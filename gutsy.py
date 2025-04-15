import os
import requests
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

lock = Lock()

def splash_header():
    print("🐷 TruffleHog GitHub User Scanner 🐷\n")

def get_github_repos(username, token):
    print(f"\n[*] Fetching public repos for user: {username}")
    print("---------------------------------------------")
    repos = []
    page = 1
    headers = {"Authorization": f"token {token}"}
    while True:
        response = requests.get(
            f"https://api.github.com/users/{username}/repos?per_page=100&page={page}",
            headers=headers
        )
        if response.status_code != 200:
            print(f"[!] GitHub API error: {response.status_code} - {response.text}")
            sys.exit(1)
        data = response.json()
        if not data:
            break
        repos.extend([repo['html_url'] for repo in data])
        page += 1
    return repos

def run_trufflehog_scan(args):
    repo_url, username, token, idx, total, results_file = args
    print(f"🚀 Starting scan on repo: {repo_url} ({idx}/{total})")
    
    # Run the TruffleHog scan
    result = subprocess.run([
        "docker", "run", "-v", f"{os.getcwd()}:/pwd", "-e", f"GITHUB_TOKEN={token}",
        "trufflesecurity/trufflehog:latest", "github", f"--repo={repo_url}"
    ], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

    # Print the scan output for debugging purposes
    print(f"Scan output for {repo_url}: {result.stdout}")

    with lock:
        # Append scan results to the results file
        with open(results_file, "a") as f:
            f.write(f"========== SCAN START: {repo_url} ==========\n")
            f.write(result.stdout)  # This is the actual scan output
            f.write(f"=========== SCAN END: {repo_url} ===========\n\n")

    print(f"✅ Scan complete for repo {repo_url}")

def main():
    splash_header()

    if len(sys.argv) < 3:
        print("Usage: python3 gutsy.py <github_username> <github_token> [--threads <num>]")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    
    # Handle threads argument
    threads = 5  # Default threads
    if len(sys.argv) == 5 and sys.argv[3] == '--threads':
        try:
            threads = int(sys.argv[4])
        except ValueError:
            print("Invalid value for threads. Using default (5).")
            threads = 5

    repos = get_github_repos(username, token)
    total = len(repos)

    if not repos:
        print(f"\n[!] No repos found or user does not exist.")
        sys.exit(1)

    print(f"\n[✔] Repos found for user '{username}' — Total: {total}. Proceeding with the scans...")
    print(f"\n[*] Starting TruffleHog scan on each repo...\n")

    results_file = f"{username}_results.txt"
    open(results_file, "w").close()  # Create or clear the results file
    print(f"📂 Results will be saved to {results_file}")

    args_list = [
        (repo_url, username, token, idx + 1, total, results_file)
        for idx, repo_url in enumerate(repos)
    ]

    # Use ThreadPoolExecutor for concurrent scanning
    with ThreadPoolExecutor(max_workers=threads) as executor:
        list(executor.map(run_trufflehog_scan, args_list))

    print(f"\n🎉 All scans complete! Results saved to {results_file}.")
    print(f"[✔] Finished scanning {total} repositories.")

    with open(results_file, 'r') as f:
        if "Found verified result" in f.read():
            print("\n╔════════════════════════════════════════════╗")
            print("║  🎯  VERIFIED RESULT FOUND IN SCAN! 🎯     ║")
            print("╠════════════════════════════════════════════╣")
            print(f"║  ➤ Check {results_file} for details.   ║")
            print("╚════════════════════════════════════════════╝")

if __name__ == "__main__":
    main()
