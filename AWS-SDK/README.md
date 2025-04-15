# AWS-SDK

## ✅ Prerequisites

- AWS account
- AWS CLI configured (`aws configure`)
- S3 Bucket (already created)
- Python 3.x installed
- Boto3 library installed (`pip install boto3`)

---

## 🧑‍💻 Project Setup

1. **Install Boto3**:
   ```bash
   pip install boto3
   ```

2. **Create your Python file** (`s3_example.py`):

---

## 💻 Step 1: Write the Python Program

`s3_example.py`:

```python
import boto3
from botocore.exceptions import NoCredentialsError

# Initialize the S3 client
s3 = boto3.client('s3')

# Bucket name and file info
bucket_name = '<your-bucket-name>'
file_name = 'sample.txt'
local_file = 'sample.txt'  # Make sure this file exists locally

# Upload file to S3
try:
    s3.upload_file(local_file, bucket_name, file_name)
    print(f"File '{file_name}' uploaded successfully!")

    # Download file from S3
    s3.download_file(bucket_name, file_name, f"downloaded_{file_name}")
    print(f"File '{file_name}' downloaded successfully!")

except FileNotFoundError:
    print(f"The file {local_file} was not found.")
except NoCredentialsError:
    print("Credentials not available.")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## 🛠️ Step 2: Run the Python Program

Run the script:
```bash
python s3_example.py
```

---

## 📄 Step 3: S3 Bucket Setup

1. Create an S3 Bucket via AWS Console or CLI:
   ```bash
   aws s3 mb s3://<your-bucket-name>
   ```
2. Upload a file to the bucket, or use your Python program to upload it.

---

## 🧪 Step 4: Test Upload & Download

1. **Upload a file** (e.g., `sample.txt`) via your Python program.
2. **Verify in the S3 bucket** through AWS Console or using:
   ```bash
   aws s3 ls s3://<your-bucket-name>/
   ```

You should see your file listed.

---

## 🧼 Step 5: Clean Up

If you want to remove the file from your bucket:

```bash
aws s3 rm s3://<your-bucket-name>/sample.txt
```

---

## 📝 Extras

- Add **error handling** for different AWS S3 exceptions.
- Make the script more modular by turning the logic into functions.
- Use **AWS IAM roles** for better security instead of default credentials.


## 📂 Folder Structure

Make sure your repo looks like this:

```
aws-sdk-python-s3/
├── README.md
├── s3_example.py
└── sample.txt  (if you'd like to upload it)
```
