from sanic import Sanic
from sanic.log import logger
from sanic.response import json, raw, file, file_stream
from sanic.request import Request
from sanic_cors import CORS
import requests
from sanic_openapi import openapi2_blueprint
from views import feature_bp,function_bp,publish_bp

app = Sanic("DTMS")
app.blueprint(openapi2_blueprint)
app.blueprint(feature_bp)
app.blueprint(function_bp)
app.blueprint(publish_bp)
CORS(app)

@app.route('/index')
async def index(request):
    return json({"Hello": "DTMS"})


if __name__ == "__main__":
    app.run(debug=False, access_log=True,port=8001)
