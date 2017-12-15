from flask import Flask, request
from caesar import rotate_string
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form method = 'POST'>
            <label>Rotate by:
                <input type="text" name="rot" value='0' />
            </label>

            <label>
                <textarea name="text"></textarea>
            </label>

            <label>
                <input type="submit" value="Submit Query"/>
            </label>
        </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():

    a_rot = int(rot)
    a_text = str(text)
    new_text = rotate_string(rot, text)

    encrypted_text = """"
    <!DOCTYPE html>
    <html lang="en">
        <body>
            <h1>""" + new_text + """
            </h1>
        </body>
    </html>
    """

    return encrypted_text

app.run()