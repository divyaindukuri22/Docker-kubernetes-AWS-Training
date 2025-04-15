# Terraform

## ✅ Prerequisites

- ✅ AWS Account
- ✅ AWS CLI installed and configured (`aws configure`)
- ✅ Terraform installed (v0.12+)
- ✅ IAM user with necessary EC2 permissions

---

### 1️⃣ Clone or Create Project Directory

```bash
mkdir terraform-ec2
cd terraform-ec2
```

---

### 2️⃣ Create Terraform Files

#### `main.tf`

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c02fb55956c7d316"  # Valid Amazon Linux 2 AMI for us-east-1
  instance_type = "t2.micro"

  tags = {
    Name = "Divya-EC2"
  }
}
```

#### `outputs.tf` (Optional)

```hcl
output "instance_public_ip" {
  value = aws_instance.example.public_ip
}
```

---

### 3️⃣ Initialize Terraform

```bash
terraform init
```

---

### 4️⃣ Preview the Plan

```bash
terraform plan
```

---

### 5️⃣ Apply the Configuration

```bash
terraform apply
```

Type `yes` when prompted.

---

### 6️⃣ Check the Output

```bash
terraform output instance_public_ip
```

Use this public IP to SSH into your instance (if you add a key pair later).

---

### 7️⃣ Destroy Resources (Optional)

```bash
terraform destroy
```

Type `yes` to confirm deletion of resources.

---
