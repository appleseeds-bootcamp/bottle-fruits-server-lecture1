from bottle import route, run, static_file, request
import json

fruits = [
    {"name": "mango", "max": "12"},
    {"name": "banana", "max": "30"}
]

@route('/fruits/add', method="POST")
def add_fruit():
	new_fruit = {
		"name": request.json.get("name"),
		"max": request.json.get("max"),
	}
	fruits.append(new_fruit)
	return json.dumps(fruits)

@route('/fruits')
def get_fruits():
    return static_file("index.html", root="static")

@route('/fruitlist')
def get_fruits_list():
    return json.dumps(fruits)

@route('/fruit/<name>')
def fruit_page(name):
    res = [fruit for fruit in fruits if fruit["name"] == name][0]
    return "Please buy me {}, if they cost less than {} shekels per kilo".format(name, res["max"])

if __name__ == "__main__":
    run(host="localhost", port=7000, debug=True, reloader=True)