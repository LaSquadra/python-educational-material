# Lesson 13 Notes: File Manipulation

Programs often need to read information from files or save information for
later. File manipulation is how Python talks to the filesystem.

## Big Idea

Files store data outside your running program. When a program ends, ordinary
variables disappear, but saved files remain.

## Reading Files

Reading a file brings text from disk into Python.

Use an explicit encoding when possible:

```python
open("notes.txt", "r", encoding="utf-8")
```

This helps avoid surprises between different computers.

## Writing And Appending

- Write mode `"w"` creates or replaces a file.
- Append mode `"a"` adds to the end of a file.

Be careful with write mode because it can overwrite existing contents.

## Paths

The lessons use `pathlib.Path` because it handles Windows, macOS, and Linux path
differences more cleanly than hand-written strings.

## Common Beginner Mistakes

- Opening a file that does not exist.
- Forgetting that `"w"` replaces file contents.
- Using platform-specific path separators by hand.
- Forgetting to close files. The `with` statement handles this for you.
