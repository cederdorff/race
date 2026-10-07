#!/usr/bin/env python3
"""Generer markdown-filer.md: en oversigt over alle .md-filer i cederdorffs repos.

Brug:
    python3 scripts/generate-markdown-index.py
    python3 scripts/generate-markdown-index.py --repos repos.txt --forks forks.txt

Uden --repos hentes listen over offentlige repos fra GitHub API'et.
Repos klones overfladisk (uden store filer) til --cache (standard: .cache/repos).
"""

import argparse
import json
import subprocess
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

OWNER = "cederdorff"
GITHUB = f"https://github.com/{OWNER}"
SKIP_DIRS = ("node_modules/", "vendor/", "libs/", ".github/ISSUE_TEMPLATE/")
BOILERPLATE_TITLES = (
    "React + Vite",
    "Getting Started",
    "Welcome to Remix",
    "Welcome to React Router",
    "Getting Started with Create React App",
    "Project Template",
    "project-template",
    "React with RACE",
    "RACE Your React",
)


def fetch_repos_from_api():
    repos, page = [], 1
    while True:
        url = f"https://api.github.com/users/{OWNER}/repos?per_page=100&type=owner&page={page}"
        with urllib.request.urlopen(url) as response:
            batch = json.load(response)
        if not batch:
            return repos
        repos += [(r["name"], r["fork"]) for r in batch]
        page += 1


def git(repo_dir, *args):
    result = subprocess.run(["git", "-C", str(repo_dir), *args], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else ""


def clone(name, cache):
    target = cache / name
    if not target.exists():
        subprocess.run(
            ["git", "clone", "-q", "--depth", "1", "--filter=blob:limit=300k", "--no-checkout",
             f"{GITHUB}/{name}", str(target)],
            capture_output=True,
        )
    return target


def first_heading(text):
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip().strip("*").strip()
    return ""


def scan(name, cache):
    repo_dir = clone(name, cache)
    branch = git(repo_dir, "rev-parse", "--abbrev-ref", "HEAD").strip() or "main"
    date = git(repo_dir, "log", "-1", "--format=%cs").strip()
    files = []
    for path in git(repo_dir, "ls-tree", "-r", "--name-only", "HEAD").splitlines():
        if not path.lower().endswith((".md", ".markdown")):
            continue
        if any(skip in path for skip in SKIP_DIRS):
            continue
        files.append((path, first_heading(git(repo_dir, "show", f"HEAD:{path}"))))
    return {"name": name, "branch": branch, "date": date, "files": files}


def link(repo, path):
    url_path = path.replace(" ", "%20")
    return f"{GITHUB}/{repo['name']}/blob/{repo['branch']}/{url_path}"


def is_boilerplate(title):
    return any(title.startswith(b) for b in BOILERPLATE_TITLES)


def render(repos, forks):
    own = [r for r in repos if r["name"] not in forks and r["date"]]
    own.sort(key=lambda r: r["date"], reverse=True)
    rich = [r for r in own if len(r["files"]) > 1]
    single = [r for r in own if len(r["files"]) == 1]
    empty = [r for r in own if not r["files"]]
    total = sum(len(r["files"]) for r in own)

    out = [
        "# Alle markdown-filer",
        "",
        f"Alle `.md`-filer i de egne repos på [github.com/{OWNER}]({GITHUB}?tab=repositories): "
        f"**{total} filer i {len(own) - len(empty)} repos**. Forks er ikke talt med.",
        "",
        "Filen er genereret med `scripts/generate-markdown-index.py`. Kør scriptet igen for at opdatere den. "
        "Den håndskrevne oversigt over kurser og opgaver står i [README.md](README.md).",
        "",
        f"- [Repos med flere markdown-filer](#repos-med-flere-markdown-filer) ({len(rich)})",
        f"- [Repos med kun én markdown-fil](#repos-med-kun-én-markdown-fil) ({len(single)})",
        f"- [Repos uden markdown](#repos-uden-markdown) ({len(empty)})",
        f"- [Forks](#forks) ({len(forks)})",
        "",
        "## Repos med flere markdown-filer",
        "",
    ]
    for repo in rich:
        out.append(f"### [{repo['name']}]({GITHUB}/{repo['name']})")
        out.append("")
        out.append(f"Senest opdateret {repo['date']} · {len(repo['files'])} filer")
        out.append("")
        long_list = len(repo["files"]) > 20
        if long_list:
            out += ["<details>", "<summary>Vis alle filer</summary>", ""]
        out += ["| Fil | Titel |", "| --- | --- |"]
        for path, title in repo["files"]:
            out.append(f"| [`{path}`]({link(repo, path)}) | {title.replace('|', '/')} |")
        if long_list:
            out += ["", "</details>"]
        out.append("")

    out += [
        "## Repos med kun én markdown-fil",
        "",
        "Typisk en README. *Standard* betyder, at README'en er en uændret skabelon fra Vite, Next.js, Remix el.lign.",
        "",
        "| Repo | Opdateret | Fil | Titel |",
        "| --- | --- | --- | --- |",
    ]
    for repo in single:
        path, title = repo["files"][0]
        mark = " *(standard)*" if is_boilerplate(title) else ""
        out.append(
            f"| [{repo['name']}]({GITHUB}/{repo['name']}) | {repo['date']} | "
            f"[`{path}`]({link(repo, path)}) | {title.replace('|', '/')}{mark} |"
        )

    out += ["", "## Repos uden markdown", ""]
    out.append(", ".join(f"[{r['name']}]({GITHUB}/{r['name']})" for r in empty) or "Ingen.")
    out += ["", "## Forks", "", "Kopier af andres repos. Deres markdown-filer er ikke med i oversigten.", ""]
    out.append(", ".join(f"[{name}]({GITHUB}/{name})" for name in sorted(forks, key=str.lower)) or "Ingen.")
    out.append("")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repos", help="Fil med reponavne (adskilt af mellemrum eller linjeskift)")
    parser.add_argument("--forks", help="Fil med navne på forks (bruges sammen med --repos)")
    parser.add_argument("--cache", default=".cache/repos")
    parser.add_argument("--output", default="markdown-filer.md")
    args = parser.parse_args()

    if args.repos:
        names = Path(args.repos).read_text().split()
        forks = set(Path(args.forks).read_text().split()) if args.forks else set()
    else:
        api_repos = fetch_repos_from_api()
        names = [name for name, _ in api_repos]
        forks = {name for name, fork in api_repos if fork}

    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)
    own_names = [n for n in names if n not in forks]
    with ThreadPoolExecutor(max_workers=16) as pool:
        repos = list(pool.map(lambda n: scan(n, cache), own_names))

    Path(args.output).write_text(render(repos, forks))
    print(f"Skrev {args.output}")


if __name__ == "__main__":
    main()
