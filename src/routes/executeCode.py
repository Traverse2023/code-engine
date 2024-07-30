from flask import Blueprint
from controllers.executeCode import hi2

executeCode = Blueprint('executeCode', __name__)

@executeCode.route('/hi')
def hi():
    return hi2()

@executeCode.route('/bye')
def bye():
    return "About - Bye"
