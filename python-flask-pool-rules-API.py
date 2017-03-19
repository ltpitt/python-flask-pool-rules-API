from flask import Flask, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Category, Item

APPLICATION_NAME = "Pool games rules API"

app = Flask(__name__)

engine = create_engine('sqlite:///item-catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# JSON APIs to view Games Information
@app.route('/catalog/JSON')
def catalog_JSON():
    """
    Return a JSON containing all items in catalog
    """
    items = session.query(Item).all()
    return jsonify(CatalogItems=[i.serialize for i in items])


@app.route('/catalog/<int:category_id>/JSON')
def catalog_category_JSON(category_id):
    """
    Return a JSON containing all items in the specified category_id
    """
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/<int:category_id>/<int:item_id>/JSON')
def catalog_item_JSON(category_id, item_id):
    """
    Return a JSON containing the specified item_id
    """
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(item=item.serialize)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)