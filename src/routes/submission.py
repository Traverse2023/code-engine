from flask import Blueprint, request, jsonify
from src.models.requests.CodeSubmissionReq import CodeSubmissionReq
from src.controllers.submission import processRun

submission = Blueprint('submission', __name__)


@submission.route('/submit', methods=['POST'])
def submit():
    codeSubmissionReq = CodeSubmissionReq(request.json)
    return processRun(codeSubmissionReq)

@submission.route('/submit', methods=['GET'])
def submit2():
    return "Hi"