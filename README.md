# GitHub Username Checker | PY 🐍

**GitHub Username Checker** is a Python tool that allows you to check the availability of GitHub usernames based on a wordlist. The tool checks usernames and saves the available ones in a generated TXT file.

## Requirements

- Python 3.X
- `requests` library (Install using `pip install requests`)

## Installation

1. Clone the repository.
2. Install the required libraries.
3. Run the tool :

    ```bash
    python checker.py
    ```

## Usage

1. Start the GitHub Username Checker:

    ```bash
    python checker.py
    ```

2. Enter the desired wordlist for the usernames you want to check in the usernames.txt (minimum length: 3 characters).

3. The tool will automatically check their availability on GitHub.

4. Available usernames will be saved in a created `available_usernames.txt` file.

## Features

- **Availability Checking :** The tool checks the availability of a wordlist.
- **Saving :** Available usernames are saved in a dedicated created TXT file.

## Example

```bash
C:\Users\Djahid\Desktop\GitHub Username Checker>python checker.py
Username 'github' is taken.
Username 'test' is taken.
Username 'djahid' is taken.
Username 'djahid1' is taken.
Username 'djahid2' is taken.
Username 'djahid3' is available.
Available usernames saved to 'available_usernames.txt'.
```

## Notes

- This tool is 100% proxy less and super simple to use.
- Use a valid internet connection while running the tool.
- Banned accounts may reappear as available.
