#!/usr/bin/env python3

import requests
import json

headers = {"Content-Type": "application/json"}


def auth():
    auth = {"username": "nate", "password": "asdf"}
    response = request.get("http://127.0.0.1:5000/auth", headers=headers, auth=auth)

def test_GET_technologies_200():
    response = requests.get("http://127.0.0.1:5000/technologies", headers=headers)
    assert response.status_code == 200


def test_POST_k8s_201():
    payload = {"cool_factor": 1000}
    response = requests.post(
        "http://127.0.0.1:5000/tech/k8s", headers=headers, data=json.dumps(payload)
    )
    assert response.status_code == 201


1


def test_POST_k8s_400():
    payload = {"cool_factor": 1000}
    response = requests.post(
        "http://127.0.0.1:5000/tech/k8s", headers=headers, data=json.dumps(payload)
    )
    assert response.status_code == 400


def test_GET_k8s_200():
    response = requests.get("http://127.0.0.1:5000/tech/k8s", headers=headers)
    assert response.status_code == 200


def test_GET_k8s_404():
    response = requests.get("http://127.0.0.1:5000/tech/tit", headers=headers)
    assert response.status_code == 404
