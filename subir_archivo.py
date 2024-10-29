import base64
import boto3

def lambda_handler(event, context):
    bucket = event["body"]["bucket"]
    filename = event["body"]["filename"]
    folder = event["body"]["folder"]
    base_64_str = event["body"]["file"]

    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key= folder + "/" + filename, Body=base64.b64decode(base_64_str))
    return {
        "statusCode": 201
    }

# with open ("image_base64.txt", "r") as file:
#     im = file.readline().strip()

# event = {
#     "body": {
#         "bucket":"test-bucket-but-this-time-its-original",
#         "filename":"jean.png",
#         "file": im
#     }
# }

# # test: PASSED
# x = lambda_handler(event, {"hello":"itsme"})
# print(x)
