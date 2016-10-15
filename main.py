from flask import Flask
from flask import session
from flask import redirect
from flask import render_template
import ConfigParser


############################
#          CONFIG          #
############################

config = ConfigParser.RawConfigParser()
config.read('secrets.cfg')

publicProblems=[0,1,2,3]
privateProblems=[-1]
app = Flask(__name__)

app.secret_key=config.get('Flask','secret')

############################
#    PRIVATE FUNCTIONS     #
############################
def authenticated(session):
    return 'user' in session


@app.route("/") # take note of this decorator syntax, it's a common pattern
def hello():
    if authenticated(session):
            return 'Hello '+str(session['user']['id'])+'!'
    return "Hello World!"

@app.route("/problems/<int:problemId>")
def show_problem(problemId):
    if authenticated(session):
        if problemId in publicProblems:
            return render_template('problem'+str(problemId)+'.html', user=session['user'])
        elif problem in privateProblems:
            if session['isAdmin']:
                return render_template('problem'+str(problemId)+'priv.html', user=session['user'])
    else:
        pass # TODO : please log in
    abort(404)

@app.route("/login/<int:userId>")
def login(userId):
    session['user']={'id':userId}
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
