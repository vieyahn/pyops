from flask import Flask
from flask import redirect
from flask import request
from flask import make_response
from flask_script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap


from flask_script import Form

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)




@app.route('/')
def index():
    return render_template('dinner.html')


    #response = make_response('<h1>This document carries a cookie!</h1>')
    #response.set_cookie('answer','42')
    #return response


    #user_agent = request.headers.get('User-Agent')
   # return '%s'%user_agent


   # return '<h1>Weclome to order your meal<h1>'


@app.route('/node1')
def node1():
    return  '+1'

@app.route('/user/<name>')
def node2(name):
    return render_template('today.html',name=name)

#return redirect('htt://www.baidu.com')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()