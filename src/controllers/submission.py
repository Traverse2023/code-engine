from flask import jsonify
import os
import boto3
import uuid

# dynamodb_endpoint = os.getenv('DYNAMODB_ENDPOINT', 'http://localhost:4566')

# dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url=dynamodb_endpoint)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

batch_client = boto3.client('batch')

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

    response = batch_client.submit_job(
        jobName="code-submission-job",
        jobQueue="code-submission-queue",
        jobDefinition="code-submission-job",
        containerOverrides={
            'environment': [
                {'name': 'LANGUAGE', 'value': codeSubmissionReq.language},
                {'name': 'code', 'value': codeSubmissionReq.code}
            ]
        }
    )

    job_id = response['jobId']

    print("jobid", job_id)
    print(job_id)
    return jsonify({"jobId": job_id})