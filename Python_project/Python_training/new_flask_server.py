from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/yolochka')     # todo (Terminal: export FLASK_APP=new_flask_server.py)
def yolochka():             # todo (Terminal:
    return 'Yolochka'
