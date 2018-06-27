import os
from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return "Hello World"


@app.route('/svn_up')
def svn_up():
    return os.popen('svn up /data/nginx/sourceconfig').read()


@app.route('/update_logic')
def update_logic():
    return os.popen('cd /data/game/logic && ./stop.sh && ./start.sh').read()


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8880, debug=True)