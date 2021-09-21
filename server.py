import os, csv
from flask import Flask, render_template, send_from_directory, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

def write_to_log(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Could not save to database'
    else:
        return 'Something went wrong!'

if __name__ == "__main__":
    app.run()