from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/experts")
def experts():
    return render_template('ex.html')
if __name__ ==  "__main__":
    app.run(debug=True)