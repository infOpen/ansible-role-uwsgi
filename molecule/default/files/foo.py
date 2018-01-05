from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    """
    Hello world route :)
    """
    return "<html><body><h1 style='color:blue'>Hello World!</h1></body></html>"


if __name__ == "__main__":
    application.run()
