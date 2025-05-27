from flask import Flask, render_template, request
from fulfillment.validate_hsn import fulfill

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        hsn_input = request.form.get("hsn_codes")
        hsn_codes = [code.strip() for code in hsn_input.split(",")]
        response = fulfill({"hsncode": hsn_codes})
        results = response["validation_results"]
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
