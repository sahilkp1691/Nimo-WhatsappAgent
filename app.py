import requests
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import markdown

load_dotenv()
app = Flask(__name__)

# WhatsApp API Details
api_token = os.getenv("API_TOKEN")
phoneNumberID = os.getenv("PHONE_NUMBER_ID")
ngrok_token = os.getenv("NGROK_TOKEN")

API_URL = f"https://graph.facebook.com/v17.0/{phoneNumberID}/messages"

contacts = [
    {"name": os.getenv("sp_name"), "phone": os.getenv("SP_PHONE_NUMBER")},
    {"name": os.getenv("sl_name"), "phone": os.getenv("SL_PHONE_NUMBER")},
    {"name": os.getenv("er_name"), "phone": os.getenv("ER_PHONE_NUMBER")},
    {"name": os.getenv("rt_name"), "phone": os.getenv("RT_PHONE_NUMBER")},
]

message = """Hello! <>, I'm Nimo, your personal AI assistant.👋🏻\n\nI'm here to help you with quick answers, assist you in making decisions, or even just have a friendly chat whenever you need it! Whether you have a question, want to explore new ideas, or need assistance with a task, I've got your back.\n\nJust type your thoughts, and I'll do my best to assist you.\n\nLooking forward to chatting with you! 🦊"""

chat_history = []


def send_message(phone_number, message, contact_name="{user}"):
    imageID = 3966175443597784
    footer = "`Nimo - Made with 🫶🏻 by Sahil Pansare`"

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "image",
        "image": {
            "id": imageID,
            "caption": f"{message.replace('<>', contact_name)}\n\n{footer}",
        },
    }

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        },
        json=payload,
    )

    if response.status_code == 200:
        print(f"✅ Message sent successfully to {phone_number}", flush=True)
    else:
        print(f"❌ Failed to send message: {response.status_code}", flush=True)
        print(response.json(), flush=True)


def parse_received_text():
    print("\n\nCHAT HISTORY: ", chat_history)


## ROUTES
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_contact = request.form.get("contact")
        if selected_contact:
            contact_name = next(
                contact["name"]
                for contact in contacts
                if contact["phone"] == selected_contact
            )
            send_message(selected_contact, message, contact_name.split()[0])
            return jsonify({"status": "Message Sent"}), 200
    return render_template("index.html", contacts=contacts)


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Verification logic for Meta Webhook
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if verify_token == ngrok_token:
            return str(challenge)  # Meta requires this exact response
        return "Verification failed", 403

    # Handle Incoming Messages
    if request.method == "POST":
        data = request.get_json()
        if "messages" in data:
            for message in data["messages"]:
                from_number = message["from"]
                received_text = message["text"]["body"]
                print(f"📩 Received message from {from_number}: {received_text}")
        return jsonify({"status": "received"}), 200


@app.route("/chat-history", methods=["GET"])
def get_chat_history():
    return render_template("chat-history.html", chat_history=chat_history)


@app.route("/readme")
def readme():
    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()
        html_content = markdown.markdown(content)
    return render_template("readme.html", content=html_content)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
