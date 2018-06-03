from app import app
from flask_restful import Api, Resource

api = Api(app)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Yawara"

class UserAPI(Resource):
    def get(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

class ProductAPI(Resource):
    def get(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

class LoginAPI(Resource):
    def get(self, id):
        pass

    def post(self, id):
        pass

api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
api.add_resource(ProductAPI, '/products/<int:id>', endpoint='product')
api.add_resource(LoginAPI, '/login', endpoint='login')
