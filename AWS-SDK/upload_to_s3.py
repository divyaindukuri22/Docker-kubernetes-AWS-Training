import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Upload the file
s3.upload_file(
    Filename='hello.txt',             # Local file path
    Bucket='divya-test-bucket-123',     # Replace with your actual bucket
    Key='folder/hello.txt'            # Path in S3 bucket
)

print("Upload successful!")
