from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """<h1>HELLO THERE</h1>
        <form method="get" action="/cheese">
            <button type="submit">GUESS</button>
        </form>
    """

@app.route("/cheese")
def burger():
    return "<h1>CHEESEBURGERS ARE BETTER"

if __name__ == '__main__':
    app.run(debug=True)