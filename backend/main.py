import argparse
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "trending-star-bot"
}
#get the trending repos
def get_trending_repos(language):
    url = f"https://github.com/trending/{language}?since=daily"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    tags = soup.find_all("h2", class_="h3")
    return [tag.a["href"].strip("/") for tag in tags]

#star the repos
def star_repo(token, full_name):
    url = f"https://api.github.com/user/starred/{full_name}"
    headers = HEADERS.copy()
    headers["Authorization"] = f"token {token}"
    requests.put(url, headers=headers)


def main():
    parser = argparse.ArgumentParser(description="Star trending GitHub repos by language.")
    parser.add_argument("language", help="Programming language ")
    parser.add_argument("--limit", type=int, default=5, help="Max number of repos to star")#pass a limit in this way ,e.g:"--limit 5" 

    args = parser.parse_args()

    repos = get_trending_repos(args.language)
    for repo in repos[:args.limit]:
        print(f"Starring: {repo}")
        star_repo(token, repo)

if __name__ == "__main__":
    main()