import json

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))  # 👈 Logs input event

    try:
        amount = event.get("amount")
        recipient = event.get("recipient")

        if not amount or not recipient:
            print("Missing data")
            return {
                'statusCode': 400,
                'body': json.dumps("Missing transaction details.")
            }

        message = f"New Transaction: ₹{amount} to {recipient}"
        print("Message to send:", message)

        return {
            'statusCode': 200,
            'body': json.dumps(message)
        }

    except Exception as e:
        print("Error occurred:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
