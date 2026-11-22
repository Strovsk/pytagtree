# Contributing

## Setup

```sh
pipx install pdm
pdm install          # creates .venv with dev tools (ruff, debugpy, commitizen, pre-commit)
```

## Everyday commands

| Command | What it does |
| --- | --- |
| `pdm run test` | Run the test suite |
| `pdm run lint` / `pdm run lint:fix` | Check / fix lint issues with Ruff |
| `pdm run format` / `pdm run format:check` | Format / check formatting with Ruff |
| `pdm run commit` | Write a Conventional Commit interactively |

## Commit messages

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <description>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
A `!` after the type or a `BREAKING CHANGE:` footer marks a breaking change.

Run `pdm run hooks` once to install the git hooks from `.pre-commit-config.yaml`: they format staged
Python files with Ruff and reject commit messages that are not Conventional Commits.

## Versioning and releases

Versions follow [SemVer](https://semver.org/) and are derived from the commits since the last tag:
`fix` bumps the patch, `feat` bumps the minor, and a breaking change bumps the major.

Releases are fully automated by the Release workflow (`.github/workflows/release.yml`). On every
push to `main` it runs the tests and `cz bump`, which updates the version in `pyproject.toml` and
`CHANGELOG.md`, creates the `bump:` commit and the `vX.Y.Z` tag, and pushes them. It then publishes
to PyPI with `pdm publish` and creates the GitHub Release. If there is no `feat`, `fix` or breaking
change since the last tag, nothing is released.

Do not run `pdm run bump` locally; `pdm run changelog --dry-run` previews the next entry.
