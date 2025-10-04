import requests
from bs4 import BeautifulSoup
from .config import GITHUB_HEADERS


def get_trending_repos(language, limit=5):
    # Get trending repositories for a given language
    try:
        url = f"https://github.com/trending/{language}?since=daily"
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        tags = soup.find_all("h2", class_="h3")
        repos = [tag.a["href"].strip("/") for tag in tags]
        return repos[:limit]
    except Exception as e:
        print(f"Error fetching trending repos: {e}")
        return []


def star_repo(token, full_name):
# Star a repository
    try:
        url = f"https://api.github.com/user/starred/{full_name}"
        headers = GITHUB_HEADERS.copy()
        headers["Authorization"] = f"token {token}"
        response = requests.put(url, headers=headers, timeout=10)
        return response.status_code == 204
    except Exception as e:
        print(f"Error starring {full_name}: {e}")
        return False


def star_repos_batch(token, language, limit):
    # Star multiple trending repos and return results
    repos = get_trending_repos(language, limit)
    starred = []
    failed = []
    
    for repo in repos:
        if star_repo(token, repo):
            starred.append(repo)
        else:
            failed.append(repo)
    
    return {
        "repos": repos,
        "starred": starred,
        "failed": failed
    }