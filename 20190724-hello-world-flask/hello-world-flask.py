'''
Script to run a "Hello World" using Python 3.X and Flask.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World!"

if __name__ == "__main__":
  app.run()
