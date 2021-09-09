from flask import Flask, request,jsonify

#import rivescript connection
import bot

#create app
app = Flask(__name__)

#route
@app.route("/chat", methods=["GET"])
def chat(): 
    message = "hello bot"
    data = {}
    status, responce = bot.chat(message)    
    if status == 0:
        data["reply"] = responce            
        data["status"] = 'Success'
        return jsonify(data)
    else:
        data["reply"] = responce
        data["status"] = 'failed'
        return jsonify(data)



#if app run

if __name__=="__main__":
    app.run(debug= True)