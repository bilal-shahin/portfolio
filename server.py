import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import csv
app = Flask(__name__)
# print(__name__)

# app.add_url_rule(
#     '/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))


# @app.route('/<string:username>/<int:age>')
# def hello_world(username='John Doe', age=18):
#     # return 'hello world!'
#     return render_template('./index.html', name=username, age_id=age)

@app.route('/')
def my_home():
    return render_template('./index.html')


# This is more dynamic and handle all the next routing urls
@app.route('/<string:page_name>')
def site_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./database.txt', mode='a') as file:
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        file.write(f'\n{email},{subject},{message}')
        # for key, value in data.items():
        #     file.write(f'{key}: {value}\n')
        # file.write("*"*20+'\n')


def write_to_csv(data):
    with open('./database.csv', mode='a') as database: # we can add the parameter newline=''
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        fieldnames = ['email', 'subject', 'message']
        csv_dictwriter = csv.DictWriter(database, fieldnames=fieldnames)
        csv_dictwriter.writeheader()
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('./thank_you.html')
        except :
            return 'did not save to database'
    else:
        return 'something went wrong'


# @app.route('/index.html')
# def index():
#     return render_template('./index.html')


# @app.route('/projects.html')
# def my_projects():
#     return render_template('./projects.html')


# @app.route('/work.html')
# def work():
#     return render_template('./work.html')


# @app.route('/about.html')
# def about_me():
#     return render_template('./about.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('./components.html')


@app.route('/favicon.ico')
def icon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'mario.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs'


@app.route('/blog/2020/dogs')
def blog_dog():
    return 'This is my dog'


@app.route('/about.html')
def about():
    return render_template('./about.html')
