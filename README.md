# AIN-3005: Advanced Python Programming

These projects are created as part of the following training: AIN-3005 "Advanced Python Programming"

# AIN-3005: Advanced Python Programming

This repository is the single source of truth for code assets used in **AIN-3005 (Advanced Python Programming)**. It is designed to help you onboard quickly, stay aligned throughout the semester, and accelerate your learning curve with runnable examples and module-based content.

The operating model is simple: each module folder contains practical material that supports lecture outcomes, lab-style practice, and homework/project implementation patterns.

## What you will find here

You should expect a structured set of folders that map to course modules and hands-on topics. As of now, the repository includes the following top-level areas:

- `module01/` and `module02/` for early-course foundations and core Python practice.
- `module03-unit.testing-using-pytest/` for unit testing workflows with `pytest`.
- `module05/` for additional advanced topics covered later in the term.
- `lecture-notes/` for supporting lecture materials.
- `developing-rest-api/` for web/service-oriented development examples.

New modules and assets may be added during the semester, so pull regularly to stay current.

## Getting started (local setup)

This repo assumes you can run Python locally. A standard, low-friction setup looks like this:

1. Install a modern Python version (recommended: Python 3.11+).
2. Clone the repository.
3. Create and activate a virtual environment.
4. Install dependencies when they exist in a module (for example, a `requirements.txt` file).

Example (Windows PowerShell):

```powershell
git clone https://github.com/deepcloudlabs/ain3005-2025.2026.git
cd ain3005-2025.2026
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Example (macOS/Linux):

```bash
git clone https://github.com/deepcloudlabs/ain3005-2025.2026.git
cd ain3005-2025.2026
python3 -m venv .venv
source .venv/bin/activate
```

If a module provides dependencies, install them from that module directory:

```bash
pip install -r requirements.txt
```

## How to use the repository effectively

For best throughput, treat each module folder as a mini-delivery with the following workflow:

- Read the module material and notes (if provided).
- Run the example scripts end-to-end before editing anything.
- Make incremental changes and re-run frequently.
- For testing modules, run tests locally and iterate until green.

If you are following along with course distribution via MS Teams as well, use this repo as your “canonical” implementation reference and Teams as the communication/coordination layer.

## Running code and tests

### Running a script
Navigate into the relevant module folder and run:

```bash
python your_script_name.py
```

### Running tests (pytest)
In the testing module (or wherever tests exist), run:

```bash
pytest -q
```

If `pytest` is not installed in your environment:

```bash
pip install pytest
```

## Collaboration and support model

If you encounter issues (setup friction, runtime errors, unclear instructions), the fastest escalation path is:

1. Reproduce the problem and capture the exact error message.
2. Note which module folder and file you were running.
3. Share your environment details (OS + Python version).
4. Report via the course channel (or open a GitHub Issue if instructed).

This keeps the feedback loop tight and makes it easier to de-risk blockers for everyone.

## Academic integrity

Use this repository as a learning accelerator, not as a copy/paste pipeline. You are expected to understand what you submit, be able to explain it, and comply with the university’s academic integrity rules.
