import httpx


def get_github_repository(repo: str) -> dict:
    print(f"🐙 GitHub tool executing for: {repo}")

    url = f"https://api.github.com/repos/{repo}"

    try:
        response = httpx.get(
            url,
            timeout=10.0,
            headers={
                "Accept": "application/vnd.github+json"
            },
        )

        response.raise_for_status()

        data = response.json()

        result = {
            "name": data["name"],
            "full_name": data["full_name"],
            "description": data["description"],
            "language": data["language"],
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "open_issues": data["open_issues_count"],
            "default_branch": data["default_branch"],
        }

        print(f"🐙 GitHub result: {result}")

        return result

    except httpx.TimeoutException:
        print("❌ GitHub request timed out")
        return {
            "error": "GitHub request timed out"
        }

    except httpx.HTTPStatusError as e:
        print(f"❌ GitHub returned HTTP {e.response.status_code}")
        return {
            "error": f"GitHub API returned {e.response.status_code}"
        }

    except httpx.RequestError as e:
        print(f"❌ GitHub request failed: {e}")
        return {
            "error": "Unable to connect to GitHub"
        }
        
