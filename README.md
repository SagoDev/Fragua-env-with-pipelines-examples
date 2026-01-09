# Fragua Environment — Step by Step Guide

This repository provides a **step-by-step, educational walkthrough** for building a complete **Fragua execution environment**.

The goal is to demonstrate, incrementally and clearly, how to:

- Configure and register **Fragua Sets** using `fragua-sets`
- Create reusable **FraguaSteps**
- Assemble **FraguaPipelines**
- Execute pipelines using the **Fragua Environment**

This project is intended as a **learning and reference environment**, not as a production-ready framework.

---

## 🎯 Project Objectives

- Build a minimal but realistic Fragua environment from scratch
- Showcase best practices for:
  - Step composition
  - Pipeline design
  - Set organization
  - Registry usage
- Reduce abstraction noise and focus on **execution clarity**
- Provide reusable patterns for future Fragua-based projects

---

## 🐍 Virtual Environment Recommendation

It is **strongly recommended** to run this project inside a **Python virtual environment** to ensure dependency isolation and reproducibility.

Using a virtual environment helps to:

- Avoid dependency conflicts with other Python projects
- Ensure consistent package versions across executions
- Keep the learning environment clean and predictable

### Recommended setup (venv)

```bash
# Create a virtual environment
python -m venv .venv
```

```bash
# Activate the virtual environment
# Windows
.venv\Scripts\activate
```

```bash
# Linux / macOS
source .venv/bin/activate
```
```bash
# Install requirements
pip install -r requirements.txt
```
---

## 📦 Core Technologies

- **Fragua 1.6.2** — Execution engine and orchestration primitives
- **fragua-sets 1.4** — Predefined, reusable sets of functions.
- **Python 3.12+**
- **pandas** — Used in transformation and loading examples

---