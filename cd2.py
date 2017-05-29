from flask import Flask
from flask import render_template, session
import main
app = Flask(__name__)

@app.route('/')
def load_cd2():
    session['prw'] = main.preWait
    session['pow'] = main.postWait
    return render_template('index.html')

@app.route('/route-info')
def load_route():
    session['text'] = main.train_times
    return render_template('info.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()