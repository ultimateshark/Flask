from flask import Flask,render_template,url_for,redirect,request
from mysqldb import connection
from passlib.hash import sha256_crypt
from flask_mail import Mail,Message
app=Flask(__name__)
#Configuration for gmail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='YourEmail@gmail.com'
app.config['MAIL_PASSWORD']='**************'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

"""Configuration For WorkMail
app.config['MAIL_SERVER']='smtp.mail.us-west-2.awsapps.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='youremail@yoursite.in'
app.config['MAIL_PASSWORD']='**********'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
"""
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form['user']
        passwd=request.form['passwd']
        c,conn=connection()
        c.execute("use example")
        udata=c.execute("select * from user where name='{0}'".format(name))
        udata=c.fetchone()
        if sha256_crypt.verify(passwd,udata[3]):
            msg=Message('From Manish Pandey',sender='in.hodophile@gmail.com',recipients=[udata[2]])
            msg.body="You logged in now"
            mail.send(msg)
            return str(udata)
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
    app.run(debug='True',port='8000',host='0.0.0.0')
