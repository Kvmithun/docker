from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    name = ""

    if request.method == "POST":
        name = request.form["name"]

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask User Input</title>

        <style>
            body {{
                font-family: Arial;
                background: #f2f2f2;
                text-align: center;
                padding-top: 100px;
            }}

            .card {{
                background: white;
                width: 400px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
            }}

            input {{
                padding: 10px;
                width: 250px;
            }}

            button {{
                padding: 10px 20px;
                margin-top: 15px;
                background: black;
                color: white;
                border: none;
                border-radius: 5px;
            }}

            h2 {{
                color: green;
            }}
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Welcome</h1>

            <form method="POST">

                <input 
                    type="text" 
                    name="name"
                    placeholder="Enter your name"
                    required
                >

                <br>

                <button type="submit">
                    Submit
                </button>

            </form>

            <h2>{f"Hello, {name}!" if name else ""}</h2>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)