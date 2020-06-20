from flask import Flask, render_template
from db.db import MongoService

app = Flask(__name__)
db = MongoService.get_instance()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
