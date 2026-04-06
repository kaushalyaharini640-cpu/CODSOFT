from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data.get("message", "").lower()

    if "hello" in user or "hi" in user or "hey" in user:
        reply = "Hello buddy! How can I help you?"

    elif "how are you" in user:
        reply = "I'm doing great, thank you for asking!"

    elif "name" in user:
        reply = "I'm a simple chatbot, nice to meet you!"

    elif "time" in user:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        reply = "The current time is " + time

    elif "date" in user:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        reply = "Today's date is " + date

    elif "bye" in user:
        reply = "Okay buddy ❤️! See you later!"

    else:
        reply = "Sorry, I didn't understand that."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)