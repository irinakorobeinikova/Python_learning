from flask import Flask

app = Flask(__name__)

# @app.route('/')       # todo (check web)
# def index():
#     return '<h1>Hello world</h1>'
#
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hi, %s!</h1>' % name


# @app.route('/user_info', methods=['GET'])       # todo (check Postman)
# def user_info():
#     name = 'Alex',
#     age = 34
#     user_list = [name, age]
#     resp = 'name=' + user_list[0] + 'age=' + user_list[1]
#     return resp



#
# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/yolochka')       # todo (check web)
# def yolochka():
#     return 'Yolochka'