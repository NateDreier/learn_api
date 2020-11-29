#!/usr/bin/env bash

# -H --header : this is an extra header to include in the request when sending HTTP to a server
# -f --fail : spits out error code 22 if curl failed
# -X --request : Specifies a custom request method to use when comunicating with the HTTP server
# -L --location : If the server reports that the requested page has moved to a different location --->
# --->  (3xx response code), this option will make curl redo the request on the new location



pass_fail() {
    if [[ $? -eq 0 ]]; then
        echo "SUCCESS"
    else
        echo "FAIL"
    fi
}
    
fail_succeeded() {
    if [[ $? -eq 22 ]]; then
        echo "SUCCESS"
    else
        echo "FAIL"
    fi
}

curl -Lf -H 'Content-Type: application/json' -X POST 'http://127.0.0.1:5000/tech/k8s' --data-raw '{"cool_factor": 1000}' > /dev/null 2>&1
pass_fail
curl -Lf -H 'Content-Type: application/json' -X GET 'http://127.0.0.1:5000/tech/k8s' > /dev/null 2>&1
pass_fail
curl -Lf -H 'Content-Type: application/json' -X GET 'http://127.0.0.1:5000/technologies' > /dev/null 2>&1
pass_fail
curl -Lf -H 'Content-Type: application/json' -X GET 'http://127.0.0.1:5000/tech/tit' > /dev/null 2>&1
fail_succeeded

