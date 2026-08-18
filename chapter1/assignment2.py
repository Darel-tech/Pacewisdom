import json
import requests

JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com"
HTTPBIN = "https://httpbin.org"

def log_requests(method, url, body, response):
    print("-" * 70)
    print(f"METHOD: {method}")
    print(f"URL: {url}")
    print(f"BODY SENT: {json.dumps(body) if body else '(NONE)'}")
    print(f"STATUS: {response.status_code} {response.reason}")
    print(f"RESPONSE: {response.text[:300]}")

def main():
    url = f"{JSONPLACEHOLDER}/posts"
    body = {"title": "foo", "body": "bar", "userId": 1}
    r = requests.post(url, json=body)
    log_requests("POST", url, body, r)
    print("WHY: 201 Created -> the server created a new resource "
          "(jsonplaceholder) simulates this and hands back a fake id, "
          "e.g. 101, but does not persist it.")

    url = f"{JSONPLACEHOLDER}/posts/1"
    body = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    r = requests.put(url, json=body)
    log_requests("PUT", url, body, r)
    print("WHY: 200 OK -> the server accepted the full replacement of "
          "post 1 and returned the updated representation.")

    url = f"{JSONPLACEHOLDER}/posts/1"
    r = requests.delete(url)
    log_requests("DELETE", url, None, r)
    print("WHY: 200 OK -> jsonplaceholder confirms the delete with an "
          "empty JSON body ({}); some real APIs instead return 204 No Content.")

    url = f"{JSONPLACEHOLDER}/posts/99999"
    r = requests.get(url)
    log_requests("GET", url, None, r)
    print("WHY: 404 Not Found -> post id 99999 does not exist on the "
          "server, so there is nothing to return.")

    url = f"{HTTPBIN}/status/422"
    body = {"title": ""}  # e.g. imagine "title" is required and can't be empty
    r = requests.post(url, json=body)
    log_requests("POST", url, body, r)
    print("WHY: 422 Unprocessable Entity -> the request was well-formed "
          "(valid JSON, hit a real endpoint) but failed a validation rule "
          "(e.g. a required field was empty). This is different from 404: "
          "the resource/route exists, the *data* is the problem.")

    print("-" * 70)

if __name__ == "__main__":
    main()
