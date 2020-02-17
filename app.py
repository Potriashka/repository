from flask import Flask, render_template

app = Flask(__name__)

website_names = "" # здесь названия всех вебстраниц

@app.route("/search", methods=[GET, POST])
def search():
	search = request.form["search"]
	if search in website_names:
	 	return render_template(f"{search}.html")
	else:
		return render_template("404.html") # сам напишешь
		
if __name__ == "__main__":
	app.run(debug=True)
