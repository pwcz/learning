from flask import request, jsonify, Blueprint
from my_app.catalog.models import Product, Category
from my_app import db
from decimal import Decimal

catalog = Blueprint('catalog', __name__)


@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


@catalog.route('/product/<key>')
def product(key):
    prod = Product.objects.get_or_404(key=key)
    return f"Product - {prod.name}, ${prod.price}"


@catalog.route('/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price),
            "category": product.category.name
        }
    return jsonify(res)


@catalog.route('/product-create', methods=['POST', ])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    categ_name = request.form.get('category')
    if not (category := Category.query.filter_by(name=categ_name).first()):
        category = Category(categ_name)
    product = Product(name=name, price=Decimal(price), category=category)
    db.session.add(product)
    db.session.commit()
    return 'Product created.'


@catalog.route('/category-create', methods=['POST',])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return 'Category created.'
