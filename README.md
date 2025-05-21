# Real-Time Payment Alert System

A serverless system that instantly notifies users of payment transactions via SMS or email, using AWS Lambda, SNS, and API Gateway.

---

## 🚀 Features

- Real-time alerts for payment transactions
- Serverless architecture for scalability and cost-efficiency
- Easy integration with frontend or mobile apps
- Supports SMS and email notifications via Amazon SNS

---

## 🛠️ Tech Stack

- AWS Lambda (Python)
- Amazon SNS (Simple Notification Service)
- AWS API Gateway
- Python (boto3)

---

## 📐 Architecture Overview

<!-- Architecture diagram will be added soon -->

1. User triggers a payment event.
2. AWS API Gateway receives the event and invokes the Lambda function.
3. Lambda processes the event and sends a notification via SNS.
4. SNS delivers real-time SMS/email alerts to subscribed users.

---

## 📚 How to Deploy

1. Create a Lambda function in AWS console with the provided `lambda_function.py` code.
2. Configure API Gateway to trigger the Lambda function.
3. Set up Amazon SNS topics and subscribe user endpoints (phone/email).
4. Test by triggering payment events via API Gateway endpoint.

---

## 👤 Author

Prajwal Kori  
[GitHub Profile](https://github.com/kori-prajwal)  
