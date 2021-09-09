from flask import Flask

#import rivescript connection
import bot

#create app
app = Flask(__name__)

#route
@app.route("/chat", methods=["POST"])
def chat():
    message = "hello bot"
    response = bot.chat(message)
    return response


#if app run

if __name__=="__main__":
    app.run()