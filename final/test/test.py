from datetime import datetime, timedelta
from flask import Flask, request, render_template,redirect,url_for
from bs4 import BeautifulSoup
from werkzeug.datastructures import LanguageAccept
from flask.helpers import make_response
from flask.json import jsonify
import jwt,requests

app = Flask(__name__)

@app.route('/')
def url():
    return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():

    auth = request.authorization

    if auth and auth.password == 'password':

        # token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        if request.method == "POST":
            user = request.form["check"]
            return redirect(url_for("user", usr=user))
        else:
            return render_template('test.html')
        
        # return jsonify({'token': token})
    
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})

@app.route("/<usr>")
def user(usr):
    usr = usr.lower()
    r = requests.get('https://www.coingecko.com/en/coins/'+  usr)
    html_doc = r.text
    soup = BeautifulSoup(html_doc,'html.parser')
    # return redirect(s)
    return soup.prettify()
    # return f"<h1>Error invalid coin.</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
