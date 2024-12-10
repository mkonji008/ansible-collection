from flask import Flask, render_template_string

app = Flask(__name__)

html_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://unpkg.com/htmx.org@1.9.0"></script>
    <title>HTMX Sample</title>
</head>
<body>
    <h1>HTMX Sample Application</h1>
    <button hx-get="/greet" hx-target="#greeting">Greet Me</button>
    <div id="greeting"></div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/greet')
def greet():
    return "Hello from HTMX!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

