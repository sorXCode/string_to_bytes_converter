from flask import Flask, render_template, request, flash
from wtforms import TextAreaField, SelectField, validators, Form, BooleanField
from converter import convert_and_pad, prefix_var


app = Flask(__name__)
app.secret_key = "some_secret"


class InputForm(Form):
    value = TextAreaField("Text", [validators.DataRequired()])
    encoding = SelectField(
        "Encoding",
        [validators.DataRequired()],
        choices=[(f"bytes-{x}", f"BYTES-{x}") for x in range(32, 0, -1)],
    )
    prefix = BooleanField(f"Add '{prefix_var}' Prefix", default=True)
    result = TextAreaField("Result")


@app.route("/", methods=["GET", "POST"])
def index():
    form = InputForm(request.form)
    if request.method == "POST":
        if form.validate():
            submitted_value = request.form["value"]
            submitted_encoding = request.form["encoding"]
            prefix = request.form.get("prefix", False)

            encoding_length_map = {f"bytes-{x}": x * 2 for x in range(1, 33)}
            max_result_length = encoding_length_map[submitted_encoding]
            result = convert_and_pad(submitted_value, max_result_length, prefix)

            prefix_length = len(prefix_var) if prefix else 0
            print(result)
            if len(result) > max_result_length + prefix_length:
                flash("Value too long for selected encoding", "error")
                print(len(result))
                result = ""

            return render_template(
                "index.html",
                form=InputForm(
                    value=submitted_value, encoding=submitted_encoding, result=result
                ),
            )

    return render_template("index.html", form=form)
