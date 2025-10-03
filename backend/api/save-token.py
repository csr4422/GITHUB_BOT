from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Global variable to hold the token in memory
SAVED_TOKEN = None  

@app.route("/api/save-token", methods=["POST"])
def save_token():
    global SAVED_TOKEN
    data = request.get_json()
    token = data.get("token")

    if not token:
        return jsonify({"error": "Token is required"}), 400

    # Save to memory
    SAVED_TOKEN = token  

    # Save to .env file
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    env_lines = []

    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            env_lines = f.readlines()

    found = False
    for i, line in enumerate(env_lines):
        if line.startswith("TOKEN="):
            env_lines[i] = f"TOKEN={token}\n"
            found = True
            break

    if not found:
        env_lines.append(f"TOKEN={token}\n")

    with open(env_path, "w") as f:
        f.writelines(env_lines)

    return jsonify({"message": "Token saved successfully!"}), 200


@app.route("/api/get-token", methods=["GET"])
def get_token():
    """
    This endpoint shows the currently stored token.
    For security, don’t expose this in real apps!
    """
    return jsonify({"token": SAVED_TOKEN}), 200


if __name__ == "__main__":
    # Load from .env on startup if available
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                if line.startswith("TOKEN="):
                    SAVED_TOKEN = line.strip().split("=", 1)[1]
                    break

    app.run(debug=True, port=5000)
