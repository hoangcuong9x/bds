from flask import Flask, request, render_template, session, redirect, url_for
from user import Newbike
import mlab
mlab.connect()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        #User request form
        return render_template("index.html")
    elif request.method == "POST":
        form = request.form
        u = form["username"]
        e = form["email"]
        n = form["number"]
        nbike = Newbike(username=u.strip(), email=e.strip(), number=n.strip())
        nbike.save()
        return render_template("index.html", username=u, email=e, number=n, u=u)
@app.route("/list")
def list():
    userlist = Newbike.objects()
    return render_template('aboutmes.html', userlist=userlist)      
if __name__ ==  "__main__":
    app.run(debug=True)