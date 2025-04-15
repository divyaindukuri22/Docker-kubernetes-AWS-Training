# lambda

## ✅ Prerequisites

- AWS account
- AWS CLI configured (`aws configure`)
- IAM user with Lambda + CloudWatch access
- Python installed locally
- `zip` utility to compress files

---

## 🧠 What We’re Building

A Lambda function that returns:  
```json
{
  "message": "Hello, Divya from Lambda!"
}
```

---

## 📁 Project Structure

```
lambda-hello-divya/
│
├── lambda_function.py
└── function.zip
```

---

## 🧾 Step 1: Write the Lambda Function

`lambda_function.py`:

```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, Divya from Lambda!'
    }
```

---

## 📦 Step 2: Zip the Function File

```bash
zip function.zip lambda_function.py
```

---

## ☁️ Step 3: Create the Lambda Function on AWS

```bash
aws lambda create-function \
  --function-name hello-divya \
  --runtime python3.9 \
  --role arn:aws:iam::<your-account-id>:role/<lambda-execution-role> \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip
```

> 💡 Make sure your IAM role has `AWSLambdaBasicExecutionRole` attached!

---

## 🧪 Step 4: Invoke the Function

```bash
aws lambda invoke \
  --function-name hello-divya \
  output.txt

cat output.txt
```

Expected output in `output.txt`:
```json
{"statusCode": 200, "body": "Hello, Divya from Lambda!"}
```

---

## 🛑 Step 5: Clean Up

```bash
aws lambda delete-function --function-name hello-divya
```

---

## 📚 Extras (Optional)

- Add triggers (API Gateway, S3, etc.)
- View logs:
  ```bash
  aws logs describe-log-groups
  aws logs get-log-events --log-group-name /aws/lambda/hello-divya ...
  ```


## 📂 Folder Setup

Make sure your GitHub repo looks like this:

```
aws-lambda-hello/
├── README.md
├── lambda_function.py
└── function.zip
```
