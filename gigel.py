from flask import Flask
from flask_restful import Api, Resource, reqparse
import re

app = Flask(__name__)
api = Api(app)

users = [
	{
	"email": "dul@gmail.com",
	"HP": "08712358",
	"name": "dul",
	"occupation": "Network Engineer",
	"password" : "qwe12345"
	},
	{
	"email": "mandra@gmail.com",
	"HP": "08351023",
	"name": "mandra",
	"occupation": "Doctor",
	"password" : "12345qwe"
	}
]

class User(Resource):
	def get(self, email):
		for user in users:
			if(email == user["email"]):
				return user, 200
		return "email not registered", 404

	def post(self, email):
		parser = reqparse.RequestParser()
		parser.add_argument("email")
		parser.add_argument("HP")
		parser.add_argument("name")
		parser.add_argument("occupation")
		parser.add_argument("password")
		args = parser.parse_args()

		for user in users:
			if(email == user["email"]):
				return "Email {} has already been used".format(email), 400
			#elif(HP == user["HP"]):
				#return "Number {} has already been used".format(HP), 400

		user = {
			"email": email,
			"HP": args["HP"],
			"name": args["name"],
			"occupation": args["occupation"],
			"password": args["password"]
		}
		users.append(user)
		return user, 201

	def put(self, email):
		parser = reqparse.RequestParser()
		parser.add_argument("password")
		parser.add_argument("occupation")
		args = parser.parse_args()

		for user in users:
			if(email == user["email"]):
				user["occupation"] = args["occupation"]
				return user, 200	

			if(user["password"] == args["password"]):
				if len(password)<8:
					return "Make sure your password is at lest 8 letters", 400
				if re.search('[0-9]',password) is None:
					return "Make sure your password has a number in it", 400
				if re.search('[a-z]',password) is None:
					return "Make sure your password has alphabet", 400

		user = {
			"email": email,
			"occupation": args["occupation"],
			"password": args["password"]
		}
		users.append(user)
		return user, 201

	def delete(self, email):
		global users
		users = [user for user in users if user["email"] != email]
		return "{} is deleted.".format(email), 200
	  
api.add_resource(User, "/user/<string:email>")
app.run(debug=True)