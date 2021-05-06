#txt
import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int(os.getenv('PORT', 5000)))
