# Python Educational Material

Author(s): LaSquadra  
Started: December 2024

This repository is a free learning resource for students who want to read,
write, and reason about Python code. It starts with beginner fundamentals, then
builds toward practical software topics such as files, APIs, concurrency, local
LLMs, the OpenAI API, chatbots, embeddings, RAG, and simple AI agents.

This is not meant to be an exhaustive Python reference. It is a guided path that
helps students build enough foundation to keep researching, experimenting, and
creating on their own.

## Who This Is For

- New Python learners who want a structured sequence.
- Students who learn best by running small examples.
- Learners who want to understand not only syntax, but why certain tools and
  data types are useful.
- Beginners who eventually want to work with APIs, AI tools, and LLM-powered
  projects.

## Quick Setup

Install Python 3.12 or newer from:

https://www.python.org/downloads/

After installation, confirm Python is available:

Windows PowerShell:

```powershell
py -3 --version
```

macOS/Linux terminal:

```bash
python3 --version
```

Choose an editor or IDE:

- VS Code: good for Python plus other languages.
- PyCharm Community Edition: focused Python development environment.

No third-party packages are required for the core lessons. Some later lessons
show optional integrations with Ollama and the OpenAI API, but those examples
skip cleanly if the tools, packages, services, or API keys are not configured.

## How To Use This Repository

1. Read the numbered lesson files in order, starting with
   `00_summary_of_basic_data_types.py`.
2. Run each lesson file and read the output.
3. Open `practice_problems.py` and complete the matching practice section.
4. Experiment by changing values, adding print statements, and trying methods
   shown in each lesson.
5. Read the matching note in `lesson_notes/` when you want more context. Start
   with `lesson_notes/README.md` for the full note index.
6. Use `course_overview.txt` as the detailed syllabus.
7. Use `final_project_brief.md` when you are ready to build a small project.

Run a lesson from the repository folder:

Windows PowerShell:

```powershell
py -3 00_summary_of_basic_data_types.py
```

macOS/Linux terminal:

```bash
python3 00_summary_of_basic_data_types.py
```

Run the practice workbook:

Windows PowerShell:

```powershell
py -3 practice_problems.py
```

macOS/Linux terminal:

```bash
python3 practice_problems.py
```

## Course Path

The numbered lessons currently cover:

- Basic data types, variables, strings, booleans, comparisons, and conditionals
- Integers, floats, lists, tuples, sets, loops, dictionaries, and functions
- Imports, modules, file manipulation, classes, errors, packages, and virtual
  environments
- JSON, API calls, environment variables, multithreading, and multiprocessing
- Ollama, the OpenAI API, chatbot design, embeddings, RAG, and AI agents

There is also an optional lesson:

- `optional_data_type_design_and_performance.py`: choosing data types for
  readability, memory use, lookup speed, mutability, and better code design

Each lesson also has a companion Markdown note in `lesson_notes/`. These notes
explain the ideas in more depth without adding extra complexity to the runnable
lesson files.

The final project guide is:

- `final_project_brief.md`: project ideas, requirements, design questions, and
  a review checklist

## Optional AI Setup

The AI-related lessons are designed to be safe to run without external services.
They explain the setup shape, then skip live calls when requirements are not
available.

For local models with Ollama:

```powershell
ollama pull llama3.2
ollama run llama3.2
```

For OpenAI API examples:

Windows PowerShell:

```powershell
python -m pip install openai
$env:OPENAI_API_KEY = "your-api-key-here"
```

macOS/Linux terminal:

```bash
python3 -m pip install openai
export OPENAI_API_KEY="your-api-key-here"
```

## Notes For Students

- You are not expected to memorize everything.
- You are expected to run code, change it, break it, fix it, and ask questions.
- When a lesson lists extra methods or tools, treat them as invitations to
  explore.
- Good Python code is usually clear first, then optimized when there is a real
  reason to optimize.
  
