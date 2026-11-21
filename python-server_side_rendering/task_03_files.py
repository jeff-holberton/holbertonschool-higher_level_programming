#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route("/items")
def items():
	try:
		with open("items.json", "r", encoding="utf-8") as file:
			data = json.load(file)
			items = data.get("items", [])
	except FileNotFoundError:
		items = []
	return render_template("items.html", items=items)

def parseJson(id):
	products = []
	error = ""
	try:
		with open("products.json", "r", encoding="utf-8") as file:
			data = json.load(file)
	except FileNotFoundError:
		error = "File not found"
	else:
		for product in data:
			if id is None or product["id"] == id:
				products.append([value for key, value in product.items() if key != "id"])
		if id is not None and not products:
			error = "Product not found"
	return products, error

def parseCSV(id):
	products = []
	error = ""
	try:
		with open("products.csv", "r", encoding="utf-8") as file:
			reader = csv.reader(file)
			next(reader)
			rows = list(reader)
	except FileNotFoundError:
		error = "File not found"
	else:
		for row in rows:
			if id is None or row[0] == str(id):
				products.append(row[1:])
		if id is not None and not products:
			error = "Product not found"
	return products, error

@app.route("/products")
def products():
	source = request.args.get('source')
	id = request.args.get("id", type=int)
	error = ""
	products = []

	if source == "json":
		products, error = parseJson(id)
	elif source == "csv":
		products, error = parseCSV(id)
	else:
		error = "Wrong source"
	return render_template("product_display.html", products=products, error=error)



if __name__ == '__main__':
	app.run(debug=True, port=5000)