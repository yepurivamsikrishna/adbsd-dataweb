import dataset

db = dataset.connect('sqlite:///shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
            { "description": 'apples', "quantity" : 2},
        { "description": 'broccoli', "quantity" : 2 },
        { "description": 'pizza', "quantity" : 2 },
        { "description": 'tangerine', "quantity" : 2 },
        { "description": 'potatoes', "quantity" : 2 },
        { "description": 'spinach', "quantity" : 2 },
        { "description": 'cookies', "quantity" : 2 },
        { "description": 'milk', "quantity" : 2 },
        { "description": 'bread', "quantity" : 2 },

        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()
