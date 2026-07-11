# coding: utf-8
"""Lesson 27: Intro to AI Agents.

An AI agent is a loop that combines a model, instructions, and tools. The model
decides what to do next, and the program runs approved tools for it.

This lesson uses a tiny rule-based fake model so it runs without any external
API. Real AI APIs can use tool or function calling to follow the same pattern.
"""

import datetime


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def calculate(number_1, operator_symbol, number_2):
    """Calculate one simple operation."""
    try:
        left = float(number_1)
        right = float(number_2)
    except ValueError:
        return "Please give the calculator two numbers."

    if operator_symbol == "+":
        return str(left + right)
    if operator_symbol == "-":
        return str(left - right)
    if operator_symbol == "*":
        return str(left * right)
    if operator_symbol == "/":
        if right == 0:
            return "Cannot divide by zero."
        return str(left / right)

    return "The calculator supports +, -, *, and /."


def today():
    """Return today's date."""
    return datetime.date.today().isoformat()


def lookup_python_term(term):
    """Look up a small Python glossary entry."""
    glossary = {
        "list": "A list stores ordered items and can be changed.",
        "dictionary": "A dictionary stores key-value pairs.",
        "function": "A function is a reusable block of code.",
    }
    return glossary.get(term.lower(), "I do not know that term yet.")


TOOLS = {
    "calculate": calculate,
    "today": today,
    "lookup_python_term": lookup_python_term,
}


def fake_model(user_request):
    """Choose a tool call using simple rules."""
    lowered = user_request.lower()

    if "date" in lowered or "today" in lowered:
        return {"tool": "today", "arguments": []}
    if "calculate" in lowered:
        parts = lowered.replace("calculate", "").strip().split()
        if len(parts) == 3:
            return {"tool": "calculate", "arguments": parts}
        return {"final": "Please ask for calculations like: calculate 12 * 7."}
    if "list" in lowered:
        return {"tool": "lookup_python_term", "arguments": ["list"]}
    if "dictionary" in lowered:
        return {"tool": "lookup_python_term", "arguments": ["dictionary"]}

    return {"final": "I can help with dates, basic calculation, lists, or dictionaries."}


def run_agent(user_request):
    """Run one model-tool loop and return a final answer."""
    model_decision = fake_model(user_request)

    if "final" in model_decision:
        return model_decision["final"]

    tool_name = model_decision["tool"]
    arguments = model_decision["arguments"]
    tool_result = run_tool(tool_name, arguments)

    return f"I used the {tool_name} tool. Result: {tool_result}"


def run_tool(tool_name, arguments):
    """Run one approved tool by name."""
    if tool_name == "today":
        return today()
    if tool_name == "calculate":
        return calculate(arguments[0], arguments[1], arguments[2])
    if tool_name == "lookup_python_term":
        return lookup_python_term(arguments[0])

    return "That tool is not available."


def demonstrate_tool_registry():
    """Show the available local tools."""
    show_section("Tool registry")

    for tool_name in TOOLS:
        print(f"- {tool_name}")


def demonstrate_agent_loop():
    """Run a few agent requests."""
    show_section("Agent loop")

    requests = [
        "What is today's date?",
        "Calculate 12 * 7",
        "What is a Python list?",
    ]

    for request in requests:
        print(f"User: {request}")
        print(f"Agent: {run_agent(request)}")


def explain_real_tool_calling():
    """Connect the toy demo to real model tool calling."""
    show_section("Real model tool calling")

    print("In a real app, the model can choose from tool definitions you provide.")
    print("Your Python code still decides which tools are allowed to run.")
    print("This keeps external actions explicit, inspectable, and testable.")


def main():
    """Run each lesson section in order."""
    demonstrate_tool_registry()
    demonstrate_agent_loop()
    explain_real_tool_calling()


if __name__ == "__main__":
    main()
