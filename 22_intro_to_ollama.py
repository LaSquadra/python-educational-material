# coding: utf-8
"""Lesson 22: Intro to Ollama.

Ollama runs large language models on your own computer. This is often called
using a local model.

Local model vocabulary:

- A model is the program that predicts text.
- A prompt is the text you send to the model.
- A chat message has a role, such as `user` or `assistant`.
- Ollama's local API usually runs at `http://localhost:11434/api`.
"""

import json
import urllib.error
import urllib.request


OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def explain_local_models():
    """Describe why someone might use a local model."""
    show_section("What local models are")

    print("A local model runs on your computer instead of a cloud service.")
    print("This can be useful for learning, privacy experiments, and offline demos.")
    print("Local models still need enough disk space, memory, and CPU or GPU power.")


def show_setup_commands():
    """Print beginner-friendly Ollama setup guidance."""
    show_section("Ollama setup commands")

    print("Install Ollama from: https://ollama.com")
    print("Then try these commands in a terminal:")
    print("  ollama pull llama3.2")
    print("  ollama run llama3.2")
    print("When Ollama is running, its API is usually available at:")
    print("  http://localhost:11434/api")


def ask_ollama_once(model="llama3.2"):
    """Try one optional Ollama chat request without crashing."""
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": "Explain Python lists in one sentence."}
        ],
        "stream": False,
    }

    request = urllib.request.Request(
        OLLAMA_CHAT_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError:
        print("Ollama is not running, so the live chat demo was skipped.")
        print("Start Ollama and pull a model if you want to try the API call.")
        return
    except TimeoutError:
        print("Ollama did not respond quickly, so the live chat demo was skipped.")
        return

    message = data.get("message", {})
    print(message.get("content", "Ollama responded, but no message text was found."))


def demonstrate_optional_api_call():
    """Show how a local Ollama API call can be made."""
    show_section("Optional local API call")

    print(f"Trying POST {OLLAMA_CHAT_URL}")
    ask_ollama_once()


def main():
    """Run each lesson section in order."""
    explain_local_models()
    show_setup_commands()
    demonstrate_optional_api_call()


if __name__ == "__main__":
    main()
