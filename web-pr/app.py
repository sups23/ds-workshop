from flask import Flask, render_template, request
from load_model import predict_model

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])

def index():

    if (request.method == "POST"):
        data = request.form.to_dict()
        result = predict_model(data)
        
        return render_template("index.html", result=result)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
