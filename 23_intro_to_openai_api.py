# coding: utf-8
"""Lesson 23: Intro to the OpenAI API.

The OpenAI API lets Python programs send prompts to OpenAI models. Most real
programs store the API key in an environment variable instead of writing it in
code.

API vocabulary:

- A client is the Python object that talks to the service.
- A model is the AI system you ask to generate a response.
- Instructions describe how the model should behave.
- Input is the user's request or data.
"""

import os


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def explain_environment_variables():
    """Explain how API keys are usually provided."""
    show_section("API keys and environment variables")

    print("Do not paste secret API keys directly into lesson files.")
    print("Set an environment variable named OPENAI_API_KEY instead.")
    print("PowerShell example:")
    print("  $env:OPENAI_API_KEY = 'your-api-key-here'")


def get_openai_client():
    """Return an OpenAI client if the package and key are available."""
    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set, so the live API demo was skipped.")
        return None

    try:
        from openai import OpenAI
    except ImportError:
        print("The openai package is not installed, so the live API demo was skipped.")
        print("Install it with: python -m pip install openai")
        return None

    return OpenAI()


def show_responses_api_shape():
    """Print the basic Responses API code shape."""
    show_section("Responses API code shape")

    print("A minimal OpenAI Python call looks like this:")
    print("  from openai import OpenAI")
    print("  client = OpenAI()")
    print('  response = client.responses.create(model="gpt-5.6", input="Hello!")')
    print("  print(response.output_text)")


def demonstrate_optional_response():
    """Try a guarded Responses API call."""
    show_section("Optional live response")

    client = get_openai_client()
    if client is None:
        return

    try:
        response = client.responses.create(
            model="gpt-5.6",
            instructions="Answer like a friendly Python tutor.",
            input="What is a Python dictionary? Give one short example.",
        )
    except Exception as error:
        print("The API request did not complete.")
        print(f"Reason: {error}")
        return

    print(response.output_text)


def main():
    """Run each lesson section in order."""
    explain_environment_variables()
    show_responses_api_shape()
    demonstrate_optional_response()


if __name__ == "__main__":
    main()
