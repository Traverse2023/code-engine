class CodeSubmissionReq:
    def __init__(self, body):
        self.code = body.get('code')
        self.questionId = body.get('questionId')
        self.language = body.get('language')
        self.userId = body.get('userId')
        self.questionName = body.get('questionName')

    def to_dict(self):
        return {
            'code': self.code,
            'questionId': self.questionId,
            'language': self.language,
            'userId': self.userId,
            'questionName': self.questionName
        }