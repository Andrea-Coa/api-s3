import base64
import boto3

def lambda_handler(event, context):
    bucket = event["body"]["bucket"]
    filename = event["body"]["filename"]
    base_64_str = event["body"]["file"]
    """
    s3_bucket_name, s3_file_name, base_64_str
    Allows for the upload of a base64 string to a s3 object, may need fleshing out down the line, returns location
    of file in S3
    :param s3_bucket_name: S3 bucket name to push image to
    :param s3_file_name: File name
    :param base_64_str: base 64 string of the image to push to S3
    :return: Tuple of bucket_name and s3_file_name
    """
    s3 = boto3.resource('s3')
    s3.Object(bucket, filename).put(Body=base64.b64decode(base_64_str))
    return (bucket, filename)

# with open ("image_base64.txt", "r") as file:
#     im = file.readline().strip()

# event = {
#     "body": {
#         "bucket":"test-bucket-but-this-time-its-original",
#         "filename":"jean.png",
#         "file": im
#     }
# }

# test: PASSED
# x = lambda_handler(event, {"hello":"itsme"})
# print(x)