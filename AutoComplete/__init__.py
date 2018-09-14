from flask import Flask,request,jsonify,render_template,url_for
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("Autocomplete.html")

@app.route('/textautocomplete', methods=['POST'])
def autocomplete():
	search = request.form.get('key')
	results = [search,"hello"+search,"good","hello","seriously","manish pandey"]
	return jsonify(results)

if __name__ == '__main__':
    app.run(debug="true")
