from flask import Flask, jsonify, g, abort
from flask.views import MethodView

app = Flask(__name__)

class UserAPI(MethodView):
    def get(self):
        return jsonify({
    'username':'fake',
    'avatar':'http://lorempixel.com/100/100/nature/'
    })

    def post(self):
        return 'UNSUPPORTED!'

def check_login(f):
    def wrapper(*args, **kwargs):
        if not None:
            abort(401)
        return f(*args, **kwargs)
    return wrapper

view = check_login(UserAPI.as_view('user'))

app.add_url_rule('/user', view_func = view)

if __name__ == '__main__':
    app.run(port=9000, debug=True)