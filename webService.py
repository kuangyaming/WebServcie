#!/usr/local/bin/python3.5

# 
# File Create Date:
#   Nov. 10. 2015
#
# Name: 
#   Kuang Yaming
#
# See READEME for instructions to deploy this web service
#

#
# Overall Design Notes:
# ---------------------
# 1. Use Flask as a framework to build web service to serve REST GET call 
# 2. Since there is no POST requirement in this particularily case, there is no database associated w/ this web service
# 3. If in the future there is POST, PUT, DELETE REST API calls, a database should be created to serve the purpose.
#    - In memory database for small application use case.
#    - On-disk database for big application use case.
#
# 4. Flask support multi-threading to serve incoming requests.
#       Flask -> Werkzueg (wrap's wsgiref)
# 
# 5. If the web server needs to serve high incoming load of requests, 
#    need to consider deploy this app Webfaction or Google App Engine;
#    
#    Detailed Flask Deployment Options refer to: 
#    http://flask.pocoo.org/docs/0.10/deploying/
#
#
# Improve Opportunity:
# * See README.txt: "Per-Thread Performance Testing" section:
#   When Fabonacci number from GET call is very large, split the response multiple 
#   times so that client could see continous output timely without being blocked for
#   a long time.
#
# * See README.txt: "Caching Capability" section:
#   Caches the last run of fabonacci list and only grow the list when necessary so that 
#   recaculate time could be reduced dramatically. 
#   This is very helpful when the input fabonacci number is very large.
# 
#

from flask import Flask, jsonify
from flask import make_response

app = Flask(__name__)

#
# Description:
#   REST GET Method
# 
# Input:
#   The count of Fibonacci Number 
#
# Output:
#   Return a list of Fibonacci numbers, in which the total counter of numbers equals to Input
#
# Example:
# Input: 3
# Output: 0, 1, 1
#
# Input: 6
# Output: 0, 1, 1, 2, 3, 5
#

@app.route('/Fib/api/v1.0/<int:fb_id>', methods=['GET'])
def get_fb(fb_id):
    Fb = [0]
    if fb_id >= 1:
        Fb.append (1)
    for x in range (2, fb_id):
        Fb.append(Fb[x-1] + Fb [x-2])

    return jsonify({'Fibonacci': Fb})

# 
# Description: 
#   Error handling for URL request
#
# Input:
#   Error code
#
# Output:
#   Return the error message to REST GET Call
# 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '/Fib/api/v1.0/<N>: Input number should be non-negative number.'}), 404)

if __name__ == '__main__':
    app.run(threaded=True)
