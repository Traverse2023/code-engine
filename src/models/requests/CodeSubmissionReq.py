class CodeSubmissionReq:
    def __init__(self, body):
        self.code = body.get('code')
        self.questionId = body.get('questionId')
        self.language = body.get('language')
        self.userId = body.get('userId')
        self.questionName = body.get('questionName')