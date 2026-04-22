from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    user_input = request.args.get("name", "")
    return f"<h1>Hello {user_input}</h1>"  # ❌ XSS vulnerable

if __name__ == "__main__":
    app.run(debug=True)
