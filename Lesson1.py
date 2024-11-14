import flask
import importlib

print(importlib.metadata.version("flask"))
app = Flask(__name__)
def home():return('hello worlds')