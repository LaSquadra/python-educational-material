# Lesson 18 Notes: API Calls

An API lets one program communicate with another program. Web APIs often use
HTTP, the same request-response system used by browsers.

## Big Idea

Your Python program sends a request. The server sends back a response.

A request often includes:

- a URL
- an HTTP method like `GET` or `POST`
- headers
- sometimes a body

A response often includes:

- a status code
- headers
- a body, often JSON

## Status Codes

Status codes summarize what happened.

- `200` usually means success.
- `404` means not found.
- `401` or `403` usually means an authentication or permission issue.
- `500` means the server had a problem.

## API Keys

Some APIs require a key. Treat API keys like passwords. Do not paste real keys
into code, screenshots, or public repositories.

## Optional Live Requests

The lesson's live request example is intentionally optional. Network examples
can fail for normal reasons: no internet, server down, blocked access, timeout,
or missing credentials.

## Common Beginner Mistakes

- Assuming every response body is JSON.
- Ignoring status codes.
- Printing or committing API keys.
- Not handling network failures.
