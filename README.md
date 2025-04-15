# GUTSY
Tool that looks for leaks of user in Github


# **GUTSY** – GitHub User Trufflehog Scanner Yo

**GUTSY** is a tool that helps you scan all public repositories of a GitHub user for secrets like API keys and tokens, using Trufflehog.

---

## **Installation**

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/gutsy.git
    cd gutsy
    ```

2. Make the script executable:

    ```bash
    chmod +x scan_user_repos.sh
    ```

---

## **Usage**

1. Run the script:

    ```bash
    ./scan_user_repos.sh
    ```

2. Enter the GitHub username when prompted:

    ```bash
    Enter GitHub username: girishkotla
    ```

3. The script will scan all public repositories of the user and save the results in a JSON file.

---

## **Output**

Results will be saved to a file called `girishkotla_leaks.json` in the current directory.

---

## **License**

This project is licensed under the MIT License.

