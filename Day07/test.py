
products = {
    'beverage':{'pepsi': {'type': '2 ltr bottle', 'price': 120, 'qty': 50},
                'coke' : {'type': '500 ml bottle', 'price': 65, 'qty': 85},
                'sprite': {'type': '300 ml can', 'price': 50, 'qty': 60}},

    'biscuts': {'marie' : {'type': '120 gms pack', 'price': 85, 'qty': 75},
                'goodday':{'type': '50 gms pack', 'price': 30, 'qty': 100},
              'krackjack':{'type': '100 gms pack', 'price':40, 'qty': 35}},

    'choclates' :{'dairymilk':{'type':'30 gms pack', 'price': 40, 'qty': 150},
                  'kitkat': {'type': '50 gms pack', 'price': 120, 'qty': 50},
                  '5 star': {'type': '40 gms pack', 'price': 65, 'qty': 75}
    }
}

ky = products['biscuts'].keys()

for k in ky:
    products['biscuts'][k].setdefault("gst", 10)

print(products['biscuts'])