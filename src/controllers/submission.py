from flask import jsonify, json
import boto3
import uuid

# dynamodb_endpoint = os.getenv('DYNAMODB_ENDPOINT', 'http://localhost:4566')

# dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url=dynamodb_endpoint)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
lambdaClient = boto3.client('lambda', region_name='us-east-1')

table = dynamodb.Table('code-submissions')

def processRun(codeSubmissionReq):
    item = {
        "pk": codeSubmissionReq.userId,
        "sk": codeSubmissionReq.userId + "#" + str(uuid.uuid4()),
        "code": codeSubmissionReq.code,
        "codeHiveId": "codehiveId100",
        "questionName": codeSubmissionReq.questionName
    }

    response = table.put_item(Item=item)
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        return "Saving submission to dynamo failed"

    response = lambdaClient.invoke(
        FunctionName="python-submission-ecr",
        InvocationType='RequestResponse',
        Payload=json.dumps(codeSubmissionReq.to_dict())
    )

    response_payload = json.loads(response['Payload'].read().decode('utf-8'))

    print("response_payload", response_payload)

    return jsonify({"response_payload": response_payload})