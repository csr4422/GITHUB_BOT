# GitHub Trending Star Bot

A Python bot that stars trending GitHub repositories for a specified programming language. Includes a simple HTML UI for generating the run command.

## Features

- Scrapes GitHub Trending for the latest repositories in a given language
- Stars repositories using your GitHub account
- Set a limit for how many repositories to star
- Simple HTML UI for generating the run command

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Github_bot
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install requests beautifulsoup4 python-dotenv
   ```
3. **Set up your GitHub token:**
   - Create a `.env` file in the project root:
     ```env
     GITHUB_TOKEN=your_personal_access_token
     ```
   - The token must have `public_repo` (for public repos) or `repo` (for private repos) scope.

## Usage

### Command Line

Run the bot for a specific language (e.g., Python) and star up to 5 trending repos:

```bash
python main.py python --limit 5
```

- Replace `python` with any language supported by GitHub Trending.
- Change `--limit` to star more or fewer repositories.

## Notes

- The bot uses web scraping and may break if GitHub changes its Trending page layout.
- Make sure your GitHub token is valid and has the correct permissions.
