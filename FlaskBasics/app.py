from flask import Flask,render_template,url_for,redirect

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/firstpage")
def firstpage():
    return "My First Web Page!!!"

@app.route("/secondpage/<int:num>")
def secondpage(num):
    if num==0:
        return redirect(url_for("index"))
    return str(num)
@app.route("/index")
def index():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug='True')
