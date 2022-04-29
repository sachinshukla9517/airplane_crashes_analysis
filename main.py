from flask import Flask

#intializing Flask
app = Flask(__name__)

@app.route("/home")
def homepage():
    return"This is Homepage"



if __name__=='__main__':
   
   # to run the flask app in debug mode (app will start authomatically)
   app.run(debug=True)
