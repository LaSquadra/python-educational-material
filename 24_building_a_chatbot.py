# coding: utf-8
"""Lesson 24: Building a Chatbot.

A chatbot keeps a conversation history and sends new user messages to a
provider. A provider can be a cloud API, a local model, or a fake provider used
for practice.

This lesson uses two classes on purpose:

- `Chatbot` manages the conversation history.
- `EchoProvider` decides what reply text to return.

Keeping those jobs separate lets the chatbot use a different provider later
without rewriting the conversation-history code.

This lesson runs with an echo provider by default, so it does not need API keys
or local services.
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


class EchoProvider:
    """A safe practice provider that does not call any external service."""

    def chat(self, messages):
        """Return a simple response based on the latest user message."""
        latest_message = messages[-1]["content"]
        return f"Echo tutor: You said '{latest_message}'. What would you try next?"


class Chatbot:
    """Store conversation messages and ask a provider for replies."""

    def __init__(self, provider):
        """Create a chatbot with a provider and a starting system message."""
        self.provider = provider
        self.messages = [
            {"role": "system", "content": "You are a friendly Python tutor."}
        ]

    def send(self, user_text):
        """Add a user message, get a reply, and save the reply."""
        self.messages.append({"role": "user", "content": user_text})
        reply = self.provider.chat(self.messages)
        self.messages.append({"role": "assistant", "content": reply})
        return reply


def explain_provider_choices():
    """Explain how real providers fit into the same chatbot shape."""
    show_section("Provider choices")

    print("A provider is the part of the program that produces the reply.")
    print("The chatbot stores messages; the provider turns messages into text.")
    print("For learning, we can use EchoProvider so the script always runs.")
    print("Later, the provider could call OpenAI, Ollama, or another model service.")


def demonstrate_scripted_chat():
    """Run a short non-interactive chatbot conversation."""
    show_section("Scripted chatbot demo")

    bot = Chatbot(EchoProvider())
    for user_text in ["What is a loop?", "Can you show a tiny example?"]:
        print(f"You: {user_text}")
        print(f"Bot: {bot.send(user_text)}")


def run_command_line_chat():
    """Offer an optional command-line loop."""
    show_section("Optional command-line loop")

    print("This loop uses EchoProvider. Type 'quit' to stop.")
    bot = Chatbot(EchoProvider())

    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in {"quit", "exit"}:
            print("Bot: Goodbye!")
            break
        if not user_text:
            print("Bot: Please type a message or 'quit'.")
            continue
        print(f"Bot: {bot.send(user_text)}")


def main():
    """Run each lesson section in order."""
    explain_provider_choices()
    demonstrate_scripted_chat()
    print("\nThe interactive loop is available by calling run_command_line_chat().")


if __name__ == "__main__":
    main()
