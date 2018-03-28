from flask import Flask
#ran into error because I forgot I had to import jsonify
from flask import jsonify
from flask import request
from flask import render_template
#no requests

#packages lower case f, classes upper class F

app = Flask(__name__)
#__name__ give each file a unique name

#@app.route('/')#basically / is homepage
#request ()inside is where it will understand
#def home():
#home method name doesn't really matter
#    return "Hello, World!"
#what is shown

#NEW CODE
#have to change to dictionary so jsonify it turns it to a dictionary
stores=[
{

    'name':'My Wonderful Store',
    'items':[
        {
        'name':'My Item',
        'price':1499
        }
        ]
}
]
#each dictionary has a name and a list of items with a name and price

#for if you want an index packages
@app.route('/')
def home():
    return render_template('index.html')

#Post used to recieve data
#GET used to send data back only
#POST /Store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store ={
        'name' : request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)



#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):#name must match one after string: acts as parameter
    #iterate over get_stores#if not match return error message
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'store not found'})
    #if the store name matches it will return


#GET /Store
@app.route('/store')
def get_stores():#name must match one after string: acts as parameter
    return jsonify({'stores':stores})
#POST /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):#name must match one after string: acts as parameter
    request_data=request.get_json()
    for store in stores:
        new_item = {
            'name':request_data['name'],
            'price': request_data['price']
        }
        #don't forget period before append
        store['items'].append(new_item)
        return jsonify(new_item)
    return jsonify({'message':'store not found'})

#GET/store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):#name must match one after string: acts as parameter
    for store in stores:
        if store['name']==name:
            return jsonify({'itmes':store['items']})
    return jsonify({'message':'store not found'})

app.run(port=5000)
#tells app to run
