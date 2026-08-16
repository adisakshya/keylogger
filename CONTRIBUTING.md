# Contributing

Thank you for helping improve this educational project. Please use it only on
systems and input you are explicitly authorized to test.

## Getting started

1. Fork the repository and create a branch from `master`.
2. Create a virtual environment with a supported Python 3 release and install
   dependencies with `pip install -r requirements.txt`.
3. Follow the README when performing authorized local checks. Do not submit
   captured data, credentials, or any other sensitive material in issues,
   commits, or pull requests.

## Changes and validation

- Keep changes focused on one issue.
- Run `python -m py_compile bin/*.py` for changes to Python sources.
- Update documentation when user-visible behavior changes.
- Add or update tests when the repository gains coverage for the affected code.

## Pull requests

Use a descriptive branch name and a concise commit message. In the pull request
description, explain the problem, link the related issue with `Fixes #<number>`,
and list the checks you ran. Keep pull requests small enough to review easily.

New contributors can find suitable work in issues labeled
[`good first issue`](https://github.com/adisakshya/keylogger/labels/good%20first%20issue).
