
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'beverage':{'pepsi': {'type': '2 ltr bottle', 'price': 120, 'qty': 50},
                'coke' : {'type': '500 ml bottle', 'price': 65, 'qty': 85},
                'sprite': {'type': '300 ml can', 'price': 50, 'qty': 60}},

    'biscuts': {'marie' : {'type': '120 gms pack', 'price': 85, 'qty': 75},
                'goodday':{'type': '50 gms pack', 'price': 30, 'qty': 100},
              'krackjack':{'type': '100 gms pack', 'price':40, 'qty': 35}}
}

class Products(Resource):

    def get(self, product):
        return {product: products[product]}

api.add_resource(Products, "/getproduct/<product>")

if __name__ == '__main__':
    app.run(debug=True)