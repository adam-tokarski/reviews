import asyncio
import humanize
from github import Github
from github.Repository import Repository
from github.PullRequest import PullRequest
from rich.table import Table

from dexi import config


class GithubAPI:
    def __init__(self) -> None:
        self._client = Github(config.GITHUB_TOKEN, per_page=config.DEFAULT_PAGE_SIZE)

    def get_repository(self, org: str, repo: str) -> Repository:
        return self._client.get_repo(f"{org}/{repo}")

    def get_pull_requests(
        self,
        repository: Repository = None,
        state: str = "open",
        sort: str = "created",
        base: str = "master",
    ) -> PullRequest:
        return repository.get_pulls(state=state, sort=sort, base=base)