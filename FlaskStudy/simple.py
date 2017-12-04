from flask import url_for, request, abort, redirect, Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/people/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'name : {0}; UA : {1} '.format(name, user_agent)

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return user_id
    else:
        return 'Open login page'

@app.route('/secret/')
def secret():
    abort(401)
    print('this is never executed')

if __name__ == '__main__':
    app.run(port=9000, debug=app.debug)