# rohan-portal-gun — local development

A fun Rick & Morty themed CLI built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/).

This README covers local development. For the user-facing package description, see [PYPI.md](./PYPI.md).

## Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation)

## Setup

```bash
git clone git@github.com:irohanrajput/portal-gun.git
cd portal-gun/rohan-portal-gun
poetry install
```

## Run the CLI locally

```bash
poetry run rohan shoot
poetry run rohan load
poetry run rohan sleep
```

Or drop into a Poetry shell:

```bash
poetry shell
rohan shoot
```

## Project layout

```
rohan-portal-gun/
├── pyproject.toml          # package metadata + deps
├── README.md               # this file
├── PYPI.md                 # long description rendered on PyPI
└── rohan_portal_gun/
    ├── __init__.py
    └── main.py             # Typer app and commands
```

## Adding a new command

Edit `rohan_portal_gun/main.py` and add a function decorated with `@app.command()`:

```python
@app.command()
def burp():
    '''rick burp'''
    console.print("[green]*buuurp*[/green]")
```

Then test it: `poetry run rohan burp`.

## Releasing a new version

Releases are fully automated via GitHub Actions + PyPI Trusted Publishing. The workflow lives at `.github/workflows/release.yml` and triggers on `v*` git tags.

### Step-by-step

```bash
# 1. make sure master is clean and you're on it
git status
git branch

# 2. bump the version in pyproject.toml
cd rohan-portal-gun
poetry version patch        # patch | minor | major
cd ..

# 3. stage code changes + version bump together
git add -A

# 4. commit
git commit -m "describe the change"

# 5. tag the commit (must match pyproject.toml version, prefixed with v)
git tag v$(cd rohan-portal-gun && poetry version -s)

# 6. push the commit and the tag
git push
git push --tags
```

The tag push is what triggers the workflow. `git push` alone will NOT publish — tags are not pushed by default.

### Watch the run

<https://github.com/irohanrajput/portal-gun/actions>

The workflow:
1. Checks out code
2. Installs Python + Poetry
3. Verifies `git tag` matches `pyproject.toml` version (fails loudly if not)
4. Runs `poetry build`
5. Publishes to PyPI via OIDC (no tokens)

Once green, verify at <https://pypi.org/project/rohan-portal-gun/> and test with:

```bash
pip install --upgrade rohan-portal-gun
rohan shoot
```

### Version bump cheat sheet

| Change | Command | Example |
|---|---|---|
| Bug fix, tiny tweak | `poetry version patch` | `0.2.1` → `0.2.2` |
| New feature (backwards compatible) | `poetry version minor` | `0.2.2` → `0.3.0` |
| Breaking change | `poetry version major` | `0.3.0` → `1.0.0` |

### Troubleshooting

**Tag / version mismatch** — you tagged `v0.2.2` but `pyproject.toml` still says `0.2.1` (or vice versa). Delete the bad tag and redo:

```bash
git tag -d v0.2.2                    # delete locally
git push --delete origin v0.2.2      # delete on GitHub
# fix pyproject.toml, commit, re-tag, re-push
```

**"File already exists" from PyPI** — you tried to publish a version that's already on PyPI. Versions are immutable. Bump again and re-tag with a new number.

**Workflow didn't trigger** — you forgot `git push --tags`. Only tag pushes start the release workflow.

**"Environment release not found"** — the GitHub environment in repo Settings → Environments doesn't match `release` in the workflow file. Both must be exactly `release`.

## Links

- PyPI: <https://pypi.org/project/rohan-portal-gun/>
- Repo: <https://github.com/irohanrajput/portal-gun>
