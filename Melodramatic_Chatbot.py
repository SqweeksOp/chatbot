#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import random

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

#starting from the loading
with open('clean_conversations.pickle', 'rb') as fp:
    clean_conversations = pickle.load(fp)

app = Flask(__name__)

bot = ChatBot("Savage")

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

trainer = ListTrainer(bot)
trainer.train(['hello','Hi','Hello','hi'])
trainer.train(['What is your name?', 'My name is Ari'])
trainer.train(['Who are you?','I am God!'])
trainer.train(['Who created you?', 'A Human', 'You?'])

#trainer.train(clean_conversations)

end_list = ['bye', 'goodbye', 'see you later', 'see you soon', 'au revoir', 'ciao', 'bi', 'bie', 'talk to you later']
chatbot_bye = ['Bye', 'See you soon', 'Au Revoir', 'Ciao', 'Goodbye']

#deploying flask as a web application
@app.route("/")
def home():
    return render_template("chatbot.html")

#making the connection of the chatbot with the flask app
@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    
    if user_text.strip().lower() in end_list:
        reply = random.choice(chatbot_bye)
    else:
        reply = str(bot.get_response(user_text))

    return reply

#running the flask app
if __name__ == "__main__":
    app.run()

