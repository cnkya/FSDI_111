from flask import Flask # from the flask module import the flask calls

app = Flask(__name__)# creates an instance of the flask class (an obj)

@app.get("/") #flask decorator that "wraps"our view function

def index(): #view function
    me={ #python3 dictionary (key-value pairs)
        "first_name": "Christina",
        "last_name": "Nkya",
        "hobbies": "Reading",
        "is_online": True
    }
    return me #returning a dict from a view function auto-converts to JSON!
