import boto3

def lambda_handler(event, context):
    nombre_bucket = event["body"]["name"]

    try:
        s3 = boto3.client("s3")
        s3.create_bucket(Bucket=nombre_bucket, ObjectOwnership="BucketOwnerPreferred")
        s3.put_public_access_block(Bucket=nombre_bucket, PublicAccessBlockConfiguration={'BlockPublicAcls': False,'IgnorePublicAcls': False,'BlockPublicPolicy': False,'RestrictPublicBuckets': False})
        s3.put_bucket_acl(ACL='public-read-write',Bucket=nombre_bucket)
        return {
            "statusCode":201,
            "bucket": nombre_bucket,
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 400,
            "message":"No se pudo crear el bucket"
        }

# s3X = boto3.client('s3')
# s3X.create_bucket(Bucket="my_bucket_name",ObjectOwnership="BucketOwnerPreferred")
# s3X.put_public_access_block(Bucket=nombre_bucket, PublicAccessBlockConfiguration={'BlockPublicAcls': False,'IgnorePublicAcls': False,'BlockPublicPolicy': False,'RestrictPublicBuckets': False})
# s3X.put_bucket_acl(ACL='public-read-write',Bucket=’my_bucket_name’)

# test: PASSED
# ans = lambda_handler({"body":{"name": "test-bucket-but-this-time-its-original"}}, {"hello":"its me"})
# print(ans)