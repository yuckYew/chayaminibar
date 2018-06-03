from app import app
from flask_restful import Api, Resource
from app.models import User, Product

api = Api(app)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Yawara"

class UserAPI(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return {
            'username': user.username,
            'email': user.email,
            'rank': user.rank_id.name
        }

    def post(self, id):
        pass

    def delete(self, id):
        pass

class ProductAPI(Resource):
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        return {
            'productname': product.username,
            'price': product.price,
            'barcode': product.barcode
        }

    def post(self, id):
        pass

    def delete(self, id):
        pass

class LoginAPI(Resource):
    def get(self, id):
        pass

    def post(self, id):
        pass

api.add_resource(UserAPI,    '/api/users/<int:id>', endpoint='user')
api.add_resource(ProductAPI, '/api/products/<int:id>', endpoint='product')
api.add_resource(LoginAPI,   '/api/login', endpoint='login')
