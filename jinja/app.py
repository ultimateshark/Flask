from flask import Flask,render_template,url_for,redirect
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html',ls=["hello","manish","pandey","green"])



if __name__ == '__main__':
    app.run(debug='True',port='8000',host='0.0.0.0')
