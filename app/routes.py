from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Yawara"

# API for getting Login
@app.route('/api/login')
def manage_login(method=['POST']):

# API for GETting User information
@app.route('/api/user/<int:user_id>', method=['GET'])
def get_user(user_id):

# API for registering User Information
@app.route('/api/user/register', method=['POST'])
def register_user():

# API for GETting Product Information
@app.route('/api/product/<int:product_id>', method=['GET'])
def get_product(product_id):

# API for registering Product Information
@app.route('/api/product/register', method=['POST'])
def register_product():
