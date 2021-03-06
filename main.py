from flask import Flask, request,jsonify, render_template 

#import rivescript connection
import bot

#create app
app = Flask(__name__)

#route
@app.route("/chat", methods=["POST"])
def chat(): 
    request_data = request.get_json()
    message = request_data['message']
    data = {}
    status, responce = bot.chat(message)    
    if status == 0:
        data["reply"] = responce            
        # data["status"] = 'Success'
        return jsonify(data)
    else:
        data["reply"] = responce
        # data["status"] = 'failed'
        return render_template('index.html', mood = jsonify(data))


@app.route('/')
def index():
    
    return render_template('index.html')


#if app run

if __name__=="__main__":
    app.run(debug= True)