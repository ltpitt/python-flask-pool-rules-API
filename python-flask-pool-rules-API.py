#!flask/bin/python
import datetime
from flask import Flask, jsonify, abort, make_response
from flask.ext.httpauth import HTTPBasicAuth

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from sqlalchemy.orm.exc import NoResultFound

from db_setup import Base, Team, Match

from flask.ext.cors import CORS

auth = HTTPBasicAuth()
app = Flask(__name__)

CORS(app)

engine = create_engine('sqlite:///pool-rules.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def help():
    return 'Welcome to Pool Rules API v1.0<br><br>Functions currently implemented in backend \
    (add to the end of your current url):<ul>/api/v1.0/categories</ul><ul>/api/v1.0/categories/1 \
    (or other available team id)</ul>'

# JSON APIs
@app.route('/api/v1.0/categories')
@app.route('/api/v1.0/categories/')
#@auth.login_required
def categories_JSON():
    """
    Returns a JSON containing all categories data
    """
    session.commit()
    try:
        categories = session.query(Category).all()
    except NoResultFound, e:
        return make_response(jsonify({'error': 'No categories were found'}), 404)
    if len(categories) == 0:
        abort(404)
    return jsonify(Categories=[i.serialize for i in categories])

@app.route('/api/v1.0/categories/<int:category_id>')
@app.route('/api/v1.0/categories/<int:category_id>/')
#@auth.login_required
def category_JSON(category_id):
    """
    Returns a JSON containing the specified category_id data
    """
    session.commit()
    try:
        category = session.query(Team).filter_by(id=category_id).one()
    except NoResultFound, e:
        return make_response(jsonify({'error': 'No row was found for category_id=' + str(category_id)}), 404)
    return jsonify(Category=[category.serialize])


@app.route('/api/v1.0/categories/<int:category_id>/<int:rule_id>')
@app.route('/api/v1.0/categories/<int:category_id>/<int:rule_id>/')
def category_rule_JSON(category_id, rule_id):
    """
    Return a JSON containing the specified rule_id
    """
    rule = session.query(Rule).filter_by(id=rule_id).one()
    return jsonify(rule=rule.serialize)


@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'rick'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
