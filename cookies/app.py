from flask import Flask,render_template,url_for,redirect,request,make_response
from mysqldb import connection
from passlib.hash import sha256_crypt
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form['user']
        passwd=request.form['passwd']
        try:
            check=request.cookies.get("name")
            if check==name:
                return "already logged in as "+name
        except:
            pass
        c,conn=connection()
        c.execute("use example")
        udata=c.execute("select * from user where name='{0}'".format(name))
        udata=c.fetchone()
        if sha256_crypt.verify(passwd,udata[3]):
            response=make_response("hello you are logged in now!!!")
            response.set_cookie("name",udata[1])
            return response
        else:
            return "wrong credential"

@app.route("/signup",methods=["POST"])
def signup():
    c,conn=connection()
    c.execute("use example")
    name=request.form['user']
    email=request.form['email']
    passwd=sha256_crypt.encrypt(request.form['passwd'])
    c.execute("INSERT INTO user (name,email,passwd) VALUES ('{0}','{1}','{2}')".format(name,email,passwd))
    conn.commit()
    c.close()
    conn.close()
    return "submitted"
if __name__ == '__main__':
    app.run(debug='True',port='8000')
