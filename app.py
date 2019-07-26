from configparser import ConfigParser
import os

from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

app = Sanic(__name__)
# More cors info @ https://github.com/ashleysommer/sanic-cors
CORS(app)


@app.route("/", methods=['GET', 'OPTIONS'])
def hello_world(req):
    return json({'return': 'value'})


def read_config():
    cfg = os.path.dirname(os.path.realpath(__file__)) + '/config.ini'
    parser = ConfigParser()
    parser.read([cfg])
    return parser


config = read_config()
# print(config['APP'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
