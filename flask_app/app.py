from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f"""
                <!DOCTYPE html>
                <html>
                <head>
                  <title>Thank You</title>
                  <link rel="stylesheet" href='/static/style.css'>
                </head>
                <body>
                  <h1>Thanks, {name}!</h1>
                  <p>{message} - Your message has been received.</p>
                  <div class="nav">
                    <a href="/">Home</a> | <a href="/contact">Send Another</a>
                  </div>
                </body>
                </html>
                """
    return render_template('contact.html')

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)
