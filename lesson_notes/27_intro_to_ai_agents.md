# Lesson 27 Notes: Intro To AI Agents

An AI agent combines a model, instructions, tools, and a loop. The important
idea is not magic autonomy. It is controlled decision-making plus approved tool
use.

## Big Idea

An agent loop often looks like this:

1. Receive a user request.
2. Decide whether a tool is needed.
3. Run an approved tool.
4. Return a final answer.

The lesson uses a fake rule-based model so students can understand the control
flow without needing an external API.

## Tools

A tool is a function the program is willing to run. Examples:

- calculate something
- look up a term
- read a file
- call an API

Real agents should only receive tools that are safe and appropriate for the
task.

## Why Explicit Tool Execution Matters

The model can suggest a tool, but Python code should still decide what is
allowed to run. This keeps actions inspectable and testable.

## Safety Mindset

Before giving an agent a tool, ask:

- What can this tool access?
- What can it change?
- What happens if the model asks for the wrong thing?
- Should a human approve this action?

## Common Beginner Mistakes

- Treating agents as fully independent.
- Giving tools too much power too early.
- Skipping validation of tool arguments.
- Hiding tool behavior behind code that is hard to inspect.
