from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('ui.html')

if __name__ == "__main__":
    app.run(debug=True)
