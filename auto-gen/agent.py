from __future__ import annotations
import os
from pathlib import Path
from typing import List, Tuple
from connectonion import Agent, llm_do
from git import Repo
from jinja2 import Template
from dotenv import load_dotenv
load_dotenv()


REPO_ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = Path(__file__).parent / "prompts"
TEMPLATES_DIR = Path(__file__).parent / "templates"
DEFAULT_TEST_DIR = REPO_ROOT / "tests"
DEFAULT_DOC_DIR = REPO_ROOT / "docs"
CODE_SUFFIXES = {".py"}

def get_changed_files(base="HEAD~1", head="HEAD") -> List[str]:
    """Return list of changed .py files."""
    repo = Repo(REPO_ROOT)
    diff = repo.git.diff("--name-status", f"{base}..{head}")
    changed = []
    for line in diff.splitlines():
        status, path = line.split("\t", 1)
        p = Path(REPO_ROOT, path)
        if p.suffix in CODE_SUFFIXES and p.is_file():
            changed.append(path)
    return changed

def read_file(rel_path: str) -> str:
    return (REPO_ROOT / rel_path).read_text(encoding="utf-8")

def module_name_from_path(rel_path: str) -> str:
    return ".".join(Path(rel_path).with_suffix("").parts)

def ensure_parent(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)

def _render_template(tpl_path: Path, **kw) -> str:
    t = Template(tpl_path.read_text(encoding="utf-8"))
    return t.render(**kw)

def generate_pytest_for_file(rel_path: str) -> Tuple[str, str]:
    source = read_file(rel_path)
    modname = module_name_from_path(rel_path)
    try:
        code = llm_do(
            f"Generate pytest for module `{modname}`:\n```python\n{source}\n```",
            system_prompt=str(PROMPTS_DIR / "writer_test.md"),
        )
    except Exception:
        code = _render_template(TEMPLATES_DIR / "pytest_skeleton.j2", modname=modname)
    base = Path(rel_path).with_suffix("").name
    return f"tests/test_{base}.py", code

def generate_doc_for_file(rel_path: str) -> Tuple[str, str]:
    source = read_file(rel_path)
    modname = module_name_from_path(rel_path)
    try:
        md = llm_do(
            f"Write documentation for `{modname}`:\n```python\n{source}\n```",
            system_prompt=str(PROMPTS_DIR / "writer_doc.md"),
        )
    except Exception:
        md = _render_template(TEMPLATES_DIR / "doc_skeleton.j2", modname=modname)
    base = Path(rel_path).with_suffix("").name
    return f"docs/{base}.md", md

def write_file(rel_path: str, content: str) -> str:
    path = REPO_ROOT / rel_path
    ensure_parent(path)
    path.write_text(content, encoding="utf-8")
    return rel_path

def commit_and_push(branch="auto/tests-docs") -> str:
    repo = Repo(REPO_ROOT)
    if branch not in repo.heads:
        repo.git.checkout("-b", branch)
    else:
        repo.git.checkout(branch)
    if repo.is_dirty(untracked_files=True):
        repo.git.add(all=True)
        repo.index.commit("Auto: add tests & docs")
        try:
            repo.git.push("--set-upstream", "origin", branch)
            return f"Pushed to origin/{branch}"
        except Exception as e:
            return f"Commit done, push failed: {e}"
    return "No changes"

agent = Agent(
    name="repo_helper",
    system_prompt="You are a repository assistant that generates tests & docs.",
    tools=[
        get_changed_files,
        generate_pytest_for_file,
        generate_doc_for_file,
        write_file,
        commit_and_push,
    ],
    max_iterations=20,
    model="co/gpt-4o-mini"
)

if __name__ == "__main__":
    prompt = """
    1) Use get_changed_files("HEAD~1","HEAD")
    2) For each changed file, call generate_pytest_for_file and write_file
    3) Then call generate_doc_for_file and write_file
    4) Finally call commit_and_push("auto/tests-docs")
    """
    print(agent.input(prompt))
