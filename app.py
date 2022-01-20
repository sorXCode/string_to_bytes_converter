from flask import Flask, render_template, request, flash
from wtforms import TextAreaField, SelectField, validators, Form, BooleanField
from converter import convert_str_to_hex_and_pad, prefix_var, convert_hex_to_str


app = Flask(__name__)
app.secret_key = "some_secret"


class InputForm(Form):
    """
    Form for inputting data
    """
    text = TextAreaField("Text")
    encoding = SelectField(
        "Encoding",
        [validators.DataRequired()],
        choices=[(f"bytes-{x}", f"BYTES-{x}") for x in range(32, 0, -1)],
    )
    add_prefix = BooleanField(f"Add '{prefix_var}' Prefix", default=True, render_kw={"checked": True})
    result = TextAreaField("Bytes")
    str_to_hex = BooleanField("Convert to Bytes", default=True, render_kw={"checked": True})


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Route to handle conversion logics.
    """

    def convert_str_to_bytes(submitted_text, submitted_encoding, add_prefix):
        """
        Convert submitted text to bytes and pad it with zeros.
        """
        encoding_length_map = {f"bytes-{x}": x * 2 for x in range(1, 33)}
        max_result_length = encoding_length_map[submitted_encoding]
        result = convert_str_to_hex_and_pad(
            submitted_text, max_result_length, add_prefix
        )

        prefix_length = len(prefix_var) if add_prefix else 0
        if len(result) > max_result_length + prefix_length:
            flash(
                f"Text too long for selected encoding, max Text length should be {submitted_encoding.split('-')[-1]}",
                "error",
            )
            result = ""
        return result

    def convert_to_str(submitted_str):
        """
        Convert submitted bytes to string.
        """
        return convert_hex_to_str(submitted_str)
    
    template_file = "template.html"
    form = InputForm(request.form)
    if request.method == "POST":
        if form.validate():
            # extract fields from validated form
            submitted_text = request.form["text"]
            submitted_encoding = request.form["encoding"]
            add_prefix = request.form.get("add_prefix", False)
            convert_to_hex = request.form.get("str_to_hex")
            result = request.form["result"]

            if convert_to_hex:
                result = convert_str_to_bytes(
                        submitted_text=submitted_text,
                        submitted_encoding=submitted_encoding,
                        add_prefix=add_prefix,
                    )
            else:
                try:
                    submitted_text = convert_to_str(result)
                except Exception as e:
                    flash(f"Error: {e}", "error")
                    submitted_text = ""

            return render_template(
                template_file,
                form=InputForm(
                    text=submitted_text, encoding=submitted_encoding, result=result
                ),
            )

    return render_template(template_file, form=form)
