import boto3

def lambda_handler(event, context):
    bucket = event["body"]["bucket"]
    directorio = event["body"]["directorio"]

    s3 = boto3.client("s3")

    try:
        s3.put_object(
            Bucket=bucket,
            Key=(directorio + "/")
        )
        return {
            'statusCode': 201,
            'directorio': directorio
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 400,
            "message":"No se pudo crear el directorio"
        }

# test: PASSED
# x = lambda_handler({
#     "body": {
#         "bucket":"test-bucket-but-this-time-its-original",
#         "directorio":"dir1"
#     }
# }, {"helo":"itsme"})
# print(x)