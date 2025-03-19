# Nimo: AI Assistant Chatbot

Nimo is an AI-powered WhatsApp chatbot designed to assist you with a wide range of tasks and conversations. Whether you need quick answers or just a friendly chat, Nimo is here to make your life easier.

Nimo integrates with the WhatsApp API to send messages to predefined contacts. It utilizes a language model (LLM) for backend communication, providing you with accurate and efficient responses directly within your WhatsApp chat.

## Key features:
- Send personalized messages to contacts.
- AI-powered chatbot for answering questions and having conversations.
- Simple and intuitive interface for managing conversations.


## Installation

Clone the Repository
```bash
git clone https://github.com/your-username/nimo-ai-chatbot.git
cd nimo-ai-chatbot
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt

```bash
pip install -r requirements.txt
```

## Usage

Frontend (to select contact and start the conversation):
```bash
python app.py
```
Backend: Whatsapp Webhook using ngrok

Configure webhook by following steps @[ngrok dashboard](https://dashboard.ngrok.com)
```bash
ngrok http http://localhost:8080
```

### Other Requirements:

- [WhatsApp Business API](https://business.whatsapp.com/products/business-platform)
- Business App setup on [Meta for Developers](https://developers.facebook.com)
- Connect webhook with the app

#### To get ImageID:

```bash
curl 'https://graph.facebook.com/<API_VERSION>/<PHONE_NUMBER_ID>/media' \
-H 'Authorization: Bearer <ACCESS_TOKEN>' \
-F 'messaging_product=whatsapp' \
-F 'file=@<FILE_PATH_AND_NAME>;type=<MIME_TYPE>'
```
MIME_TYPE : [WhatsApp API Guide](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media#upload-media)

## Contributing

If you'd like to contribute to the development of Nimo, feel free to fork the repository and submit pull requests. Here are some ways you can contribute:

- Reporting bugs and issues.
- Adding new features or enhancing existing functionality.
- Improving documentation.

## License

[MIT](https://choosealicense.com/licenses/mit/)