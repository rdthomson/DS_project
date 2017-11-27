from flask  import Flask, url_for, render_template
app = Flask(__name__)


# Web root
@app.route("/")
def root():
        return render_template('index.html'), 200

@app.route("/problems")
def problems():
        return render_template('problems.html'), 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
