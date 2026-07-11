# coding: utf-8
"""Lesson 18: API Calls.

An API lets one program ask another program for data or ask it to do work. Many
web APIs use HTTP, the same request-and-response system used by web browsers.

Common API vocabulary:

- A URL is the address of the resource you want.
- A request is the message your program sends.
- A response is the message the server sends back.
- A status code describes whether the request succeeded.
- Headers are extra details sent with a request or response.
- A JSON body is structured data sent as text.
- An API key is a secret value that identifies your app or account.

This lesson uses a sample response by default so it can run without internet
access. The optional live request function is not called by `main`.
"""

import json
import urllib.error
import urllib.request


SAMPLE_API_URL = "https://api.example.com/students/ada"
SAMPLE_JSON_BODY = """
{
  "id": 1,
  "name": "Ada",
  "current_lesson": 18,
  "ready_for_concurrency": true
}
"""


def show_section(title):
    """Print a consistent section heading for the lesson output."""
    print(f"\n{title}")
    print("-" * len(title))


def explain_request_parts():
    """Describe the pieces of a basic HTTP API request."""
    show_section("Parts of an API request")

    print(f"URL: {SAMPLE_API_URL}")
    print("HTTP method: GET")
    print("Request header example: Accept: application/json")
    print("A GET request usually asks to read data.")


def demonstrate_sample_response():
    """Use a hardcoded response instead of making a network request."""
    show_section("Sample API response")

    status_code = 200
    headers = {
        "Content-Type": "application/json",
        "X-Lesson": "Intro to API Calls",
    }
    body = SAMPLE_JSON_BODY

    print(f"Status code: {status_code}")
    print(f"Content-Type header: {headers['Content-Type']}")
    print(f"Raw JSON body: {body.strip()}")


def parse_sample_json_body():
    """Convert a JSON response body into Python data."""
    show_section("Parsing a JSON body")

    student = json.loads(SAMPLE_JSON_BODY)

    print(f"Student name: {student['name']}")
    print(f"Current lesson: {student['current_lesson']}")
    print(f"Ready for concurrency? {student['ready_for_concurrency']}")


def explain_api_keys():
    """Explain API keys without requiring one."""
    show_section("API keys")

    print("Some APIs require an API key.")
    print("An API key is like a password for your program, so keep it secret.")
    print("Do not paste real API keys into public code or screenshots.")
    print("Programs often read keys from environment variables.")


def optional_live_request(url):
    """Try a live GET request with urllib and handle common failures.

    This function is intentionally not called by main because lessons should run
    reliably without internet access. It is a preview of several ideas working
    together: request objects, headers, context managers, byte decoding, and
    exception handling.
    """
    show_section("Optional live urllib request")

    print("This is an advanced optional preview, not required practice.")
    print("The normal lesson uses sample data so it works without internet.")

    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json"},
        method="GET",
    )

    try:
        # `with` closes the network response after the indented block finishes.
        with urllib.request.urlopen(request, timeout=5) as response:
            status_code = response.status
            content_type = response.headers.get("Content-Type", "unknown")
            # Network responses arrive as bytes, so decode turns them into text.
            body = response.read().decode("utf-8")
    except urllib.error.URLError as error:
        print(f"Could not complete request: {error}")
    else:
        print(f"Status code: {status_code}")
        print(f"Content-Type: {content_type}")
        print(f"First 200 characters of the body: {body[:200]}")


def main():
    """Run each lesson section in order."""
    explain_request_parts()
    demonstrate_sample_response()
    parse_sample_json_body()
    explain_api_keys()


if __name__ == "__main__":
    main()
