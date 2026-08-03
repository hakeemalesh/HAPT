# HAPT Installation Guide

## Overview

This guide explains how to install and run the Hybrid AI Trading Platform (HAPT) on a clean machine.

---

# Requirements

- Python 3.12 or later
- Git
- Linux (Ubuntu recommended)

Windows users can install HAPT using WSL (Windows Subsystem for Linux).

---

# Clone the Repository

```bash
git clone <repository-url>

cd HAPT
```

---

# Create a Virtual Environment

```bash
python3 -m venv .venv
```

---

# Activate the Virtual Environment

Linux / WSL

```bash
source .venv/bin/activate
```

Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Verify Installation

Run:

```bash
pytest
```

Expected result:

```
106 passed
```

---

# Start HAPT

Run:

```bash
python -m app.main
```

Expected startup:

- Banner displayed
- Startup checks
- Market scan
- Trade planning
- AI review
- Paper broker execution
- Trade journal

---

# Development Workflow

After making code changes:

Compile:

```bash
python -m py_compile app/main.py
```

Run tests:

```bash
pytest
```

Run HAPT:

```bash
python -m app.main
```

Commit changes:

```bash
git add .

git commit -m "Description"
```

---

# Repository Structure

```
app/
tests/
config/
data/
docs/
docker/
scripts/
```

---

# Support

For additional information, refer to:

- README.md
- ARCHITECTURE.md
- CHANGELOG.md