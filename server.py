from flask import Flask, render_template, url_for, request, redirect
import csv, os 

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def other_pages(page_name):
    return render_template(page_name)


def write_to_csv(data):
	filename = 'email_data.csv'
	if filename not in os.listdir('.'):
		with open(filename, mode='w', newline='') as file:
			csv_writer = csv.writer(file)
			csv_writer.writerow(['EMAIL ADDRESS', 'SUBJECT', 'MESSAGE'])
	with open(filename, 'a', newline='') as file:
		csv_writer = csv.writer(file)
		csv_writer.writerow([data['email'], data['subject'], data['message']])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('thank_you.html')
		except:
			return 'Unable to save to database'
	else:
		return 'Something went wrong. Try again!'
