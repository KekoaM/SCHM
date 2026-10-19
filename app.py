import hashlib
import os

from flask import Flask, Response, request

app = Flask(__name__)

COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME", "sessionid")


@app.route("/auth")
def auth():
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        # return Response("missing session cookie\n", status=401)
        token = ""

    resp = Response("ok\n", status=200)
    # Hash the token so the raw session value never appears in headers or logs
    resp.headers["X-Session-ID"] = hashlib.sha256(token.encode()).hexdigest()
    return resp


@app.route("/healthz")
def healthz():
    return "ok\n", 200
