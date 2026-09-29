"""Point every notebook and the README at your GitHub repository.

Run once after you create the repo, from the repo's top folder:
    python scripts/configure_repo.py your-username/your-repo-name
Optionally add a branch name (default: main):
    python scripts/configure_repo.py your-username/your-repo-name main
Then commit and push the changed files.
"""
import sys, pathlib

if len(sys.argv) < 2 or "/" not in sys.argv[1]:
    sys.exit(__doc__)
repo = sys.argv[1].strip("/")
branch = sys.argv[2] if len(sys.argv) > 2 else "main"
root = pathlib.Path(__file__).resolve().parent.parent
placeholder = "YOUR-GITHUB-USERNAME/cogs118d-datasets"

files = [root / "README.md"] + sorted((root / "notebooks").glob("*.ipynb"))
for path in files:
    text = path.read_text(encoding="utf-8")
    new = text.replace(placeholder, repo)
    if branch != "main":
        new = new.replace('BRANCH = \\"main\\"', f'BRANCH = \\"{branch}\\"').replace("/blob/main/", f"/blob/{branch}/")
    if new != text:
        path.write_text(new, encoding="utf-8")
        print("updated", path.relative_to(root))
print("Done. Commit and push these files.")
