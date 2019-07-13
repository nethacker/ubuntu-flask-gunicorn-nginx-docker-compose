from flask import Flask
hello = Flask(__name__)

@hello.route("/")
def greeting():
    return "<h1 style='color:red'>Hello World!</h1>"

if __name__ == "__main__":
    hello.run(host='0.0.0.0')
