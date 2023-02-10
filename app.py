from flask import Flask, render_template, request
from chatgpt_api.chatgpt_response import ChatgptResponse

app = Flask(__name__)

message = {"query": "response"}

@app.route("/")
def index():
    return render_template("index.html", message=message)

@app.route("/chatgpt/", methods=["GET", "POST"])
def chat_gpt():
    chatter = ChatgptResponse()
    if request.method == "POST":
        query = request.form["query"]
        gpt_resp = chatter.get(prompt=query, max_tokens=1000)
    else:
        query = "You have not asked a question yet"
        gpt_resp = "There is no response yet"
    return render_template("chatgpt.html", gpt_query=query, gpt_resp=gpt_resp)
