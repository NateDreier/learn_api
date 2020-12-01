#!/usr/bin/env python3

from flask import Flask, request
from flask_restful import Resource, Api
from flas_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = "souper_seacret"

jwt = JWT(app, authenticate, identity)  # /auth

technologies = []

# 400 BAD REQUEST
# 401 UNAUTHORIZED
# 404 NOT FOUND
# 200 OK
# 201 CREATED
# 202 ACCEPTED (delaying the creation)(ie the creation takes a couple of minutes)


class Tech(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, technologies), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, technologies), None):
            return {"message": f"{name} already exists"}, 400
        else:
            request_data = request.get_json()
            item = {"name": name, "cool factor": request_data["cool_factor"]}
            technologies.append(item)
            return item, 201


class TechList(Resource):
    def get(self):
        return {"item": technologies}


api.add_resource(Tech, "/tech/<string:name>")  # https://127.0.0.1:5000/tech/some_tech
api.add_resource(TechList, "/technologies")

app.run(debug=True, host="0.0.0.0")
