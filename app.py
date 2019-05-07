from flask import Flask, request, render_template, session, redirect, url_for
from user import Newbike
import mlab
import smtplib
mlab.connect()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        #User request form
        return render_template("login.html")
    elif request.method == "POST":
        form = request.form
        # u = form["username"]
        # e = form["email"]
        s = form["sdt"]
        nbike = Newbike(sdt=s.strip())
        if s == '':
            notice = "vui long nhap sdt"
            return render_template("login.html", notice=notice)
        else:
            nbike.save()
            return render_template("index.html")
@app.route("/trangchu", methods=["GET", "POST"])
def trangchu():
    if request.method == "GET":
        #User request form
        return render_template("index.html")
    elif request.method == "POST":
        form = request.form
        u = form["username"]
        e = form["email"]
        n = form["number"]
        m = form["messenger"]
        nbike = Newbike(username=u.strip(), email=e.strip(), number=n.strip(), messenger=m.strip())
        nbike.save()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("spy12a6@gmail.com", "cuong11a6")
        msg = "Cam on quy khach da quan tam toi du an, goi ngay 012345678 de duoc tu van mien phi"
        server.sendmail("spy12a6@gmail.com", e, msg)
        server.quit()
        notice = 'tks kiu!'
        return render_template("index.html", username=u, email=e, number=n, messenger=m, u=u, notice=notice)
@app.route("/list")
def list():
    userlist = Newbike.objects()
    return render_template('aboutmes.html', userlist=userlist)     
if __name__ ==  "__main__":
    app.run(debug=True)