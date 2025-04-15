Absolutely, here's **everything in proper `README.md` Markdown format**, ready to drop straight into your `README.md` file:

---

```markdown
# 🐷 GUTSY — GitHub User TruffleHog Scanner

GUTSY is a Python-based tool that scans **all public GitHub repositories of a user** using [TruffleHog](https://github.com/trufflesecurity/trufflehog). It helps find secrets and sensitive data exposed in public repos.

---

## 🚀 Features

- 🔍 Scans all public GitHub repositories for secrets
- 🐳 Uses Dockerized TruffleHog — no local install needed
- ⚡ Multi-threaded scanning (adjustable)
- 📁 Saves detailed results per repo
- 🎯 Highlights **verified secrets** after scan completes

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/girishkotla/GUTSY.git
cd GUTSY
```

---

## ⚙️ Requirements

Make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/) (installed and running)
- GitHub Personal Access Token (classic token with `repo` scope)

To install dependencies (if any are added later), use:

```bash
pip install -r requirements.txt
```

Currently, GUTSY uses only Python standard libraries and Docker.

---

## 🧪 Usage

```bash
python3 gutsy.py <github_username> <github_token> [--threads <num>]
```

### Example:

```bash
python3 gutsy.py octocat ghp_yourtokenhere --threads 10
```

### Parameters:

- `<github_username>`: GitHub username to scan
- `<github_token>`: GitHub personal access token
- `--threads <num>`: *(Optional)* Number of threads (default: 5)

---

## 📁 Output Format

All scan results are saved in a file named:

```bash
<github_username>_results.txt
```

Each repository output is wrapped like this:

```
========== SCAN START: https://github.com/octocat/Hello-World ==========
<TruffleHog scan output>
=========== SCAN END: https://github.com/octocat/Hello-World ===========
```

---

## 🎯 Verified Secrets Detection

If any scan includes `Found verified result`, you'll see this:

```
╔════════════════════════════════════════════╗
║  🎯  VERIFIED RESULT FOUND IN SCAN! 🎯     ║
╠════════════════════════════════════════════╣
║  ➤ Check octocat_results.txt for details. ║
╚════════════════════════════════════════════╝
```

---

## 🐳 Under the Hood

GUTSY runs this Docker command under the hood for each repository:

```bash
docker run -v $(pwd):/pwd -e GITHUB_TOKEN=<token> trufflesecurity/trufflehog github --repo=<repo_url>
```

Make sure Docker is up and running before you start scanning!

---

## ⚠️ Disclaimer

> This tool is for **educational and authorized testing** purposes only.  
> Do not scan repositories you don’t own or have permission to analyze.

---

## 🤝 Contributing

Pull requests are welcome! If you spot bugs or have ideas, open an issue or fork the repo.

---

## 📜 License

MIT License — see [LICENSE](LICENSE) file.
```

---

You're all set now! Let me know if you want me to generate a nice `requirements.txt`, or add shields.io badges to your README.
