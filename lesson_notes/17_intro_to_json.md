# Lesson 17 Notes: JSON

JSON is a text format for structured data. It is common in APIs, configuration
files, logs, and exported data.

## Big Idea

JSON looks similar to Python dictionaries and lists, but JSON is text. Python's
`json` module converts between JSON text and Python data.

## Main Conversions

- `json.loads()` turns JSON text into Python data.
- `json.dumps()` turns Python data into JSON text.
- `json.load()` reads JSON from a file.
- `json.dump()` writes JSON to a file.

## JSON vs Python

JSON has its own spelling for a few values:

- JSON `true` becomes Python `True`
- JSON `false` becomes Python `False`
- JSON `null` becomes Python `None`

The `json` module handles those conversions.

## Why JSON Matters

Many APIs send responses as JSON. If students understand dictionaries, lists,
and strings, JSON is the bridge between Python programs and many web services.

## Common Beginner Mistakes

- Forgetting that JSON files contain text, not Python objects.
- Using single quotes in JSON text. JSON requires double quotes.
- Trying to write Python values to a file without converting or dumping them.
- Committing generated demo files that should be ignored.
