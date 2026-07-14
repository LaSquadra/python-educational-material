# Lesson 24 Notes: Building A Chatbot

A chatbot keeps track of conversation history and uses a provider to generate
replies.

## Big Idea

The chatbot has two jobs:

- store messages
- ask something else for a reply

That "something else" is the provider. It might be a fake echo provider, a local
model, or a cloud API.

## Why Use A Provider

Separating the chatbot from the provider makes the design flexible. The chatbot
can keep the same conversation logic while the provider changes.

For learning, an echo provider is useful because it always runs and does not
need credentials.

## Conversation History

Many chat systems use messages with roles:

- `system` for overall behavior
- `user` for user messages
- `assistant` for assistant replies

Keeping history lets future replies consider earlier context.

## Optional Input Loop

The command-line loop is optional because interactive code can block automated
lesson runs. Students can call it manually when they are ready.

## Common Beginner Mistakes

- Mixing conversation storage and API logic too tightly.
- Forgetting to save assistant replies.
- Creating an infinite input loop without a way to quit.
- Putting real API calls into examples that should run offline.
