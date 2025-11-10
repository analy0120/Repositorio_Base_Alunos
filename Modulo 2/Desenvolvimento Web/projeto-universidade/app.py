from flask import Flask, request, jsonify, render_template, json
# from main import ler_dados 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = request.get_data()
        return jsonify(data)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        data = request.json()
        print(data)
        return jsonify(data)
    
if __name__=="__main__":
    app.run() 