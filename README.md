# Fragua Environment — Step by Step Guide

This repository provides a **step-by-step, educational walkthrough** for building a complete **Fragua execution environment**.

The goal is to demonstrate, incrementally and clearly, how to:

- Configure and register **Fragua Sets** using `fragua-sets`
- Create reusable **FraguaSteps**
- Assemble **FraguaPipelines**
- Execute pipelines using the **Fragua Agent**
- Understand the architectural roles of each component

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

## 📦 Core Technologies

- **Fragua** — Execution engine and orchestration primitives
- **fragua-sets** — Predefined, reusable sets of functions and pipelines
- **Python 3.12+**
- **pandas** — Used in transformation and loading examples

---

## 🧱 Conceptual Architecture

The environment is built around the following core concepts:

### FraguaStep
- Represents a **single execution unit**
- Wraps a pure function
- Can define:
  - Parameters
  - Inputs (`use`)
  - Outputs (`save_as`)

### FraguaPipeline
- An **ordered sequence of FraguaSteps**
- Describes *what* should be executed, not *how*
- Immutable by design

### FraguaSet
- A **named collection of reusable execution units**
- Can contain:
  - Callables
  - Pipelines
- Registered into a central registry

### FraguaRegistry
- Central lookup structure for:
  - Sets
  - Pipelines
  - Execution units

### FraguaAgent
- Stateless executor
- Receives a pipeline and executes it step by step
- Holds no domain logic

---

