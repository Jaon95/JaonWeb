from flask import Flask, request, jsonify

from ext import db
from users import User

import logging
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import get_debug_queries


app = Flask(__name__)
app.config.from_object('config')
app.config['DATABASE_QUERY_TIMEOUT'] = 0.0001
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

formatter = logging.Formatter(
    "[%(asctime)s]{%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
)
handler = RotatingFileHandler('slower_query.log', maxBytes=1000, backupCount=10)
handler.setLevel(logging.WARN)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= app.config['DATABASE_QUERY_TIMEOUT']:
            app.logger.warn(
                ('Context:{}\nSlow QUERY:.{}\nParameters:{}\nDuration:{}\n'.format(query.context, query.statement, query.parameters, query.duration))
            )
    
    return response
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/users', methods=['POST','GET'])
def users():
    username = request.form.get('name')

    user = User(username)
    print('User ID : {} '.format(user.id))
    db.session.add(user)
    db.session.commit()

    return jsonify({'id':user.id})

if __name__ == '__main__':
    app.run(host = 'localhost', port = 9000)