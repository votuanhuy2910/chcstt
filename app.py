from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter"
)
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.vietnam")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    response = str(english_bot.get_response(userText))
    response = response.replace('\\n', '\n')
    return response

if __name__ == "__main__":
    app.run()