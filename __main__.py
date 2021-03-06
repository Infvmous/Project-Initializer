import sys
import os
import json
from typing import Union

from urllib.request import Request, urlopen
from urllib.error import HTTPError


BASE_URL = 'https://api.github.com'
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')


def create_project_folder(folder_name: str, project_folder: str) -> None:
    """
    Creates a folder with a project in a folder with projects
    if such a project name doesn't exist
    """
    try:
        os.mkdir(f'{project_folder}/{folder_name}')
        print(f'Directory {folder_name} created')
    except FileExistsError:
        sys.exit(f'Directory {folder_name} already exists')


def handle_response_status_codes(req: Request, data: str) -> Union[dict, None]:
    """
    Throws HTTPError if request wasn't successful
    """
    try:
        resp = urlopen(req, data=data)
        return json.load(resp)
    except HTTPError as e:
        sys.exit(f'Status: {e.code} {e.msg}\nHeaders: \n{e.hdrs}')


def create_github_repository(repo_name: str) -> None:
    """
    Creates new GitHub repository with repository name repo_name
    """
    req = Request(f'{BASE_URL}/user/repos', method='POST')
    req.add_header('Authorization', f'token {GITHUB_TOKEN}')
    data = json.dumps({'name': repo_name}).encode()
    content = handle_response_status_codes(req, data)
    print(f'Setting up new project at {content["html_url"]}')


def main(project_name: str, project_folder: str) -> None:
    create_project_folder(project_name, project_folder)
    create_github_repository(project_name)


if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        sys.exit(f'Project name is missing at {sys.argv}')
