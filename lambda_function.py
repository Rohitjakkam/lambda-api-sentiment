import json
import boto3

def lambda_handler(event, context):
    print("Event Received:", json.dumps(event, indent=2))  # Log event for debugging

    comprehend = boto3.client('comprehend')

    try:
        # Check what API Gateway sends
        if "body" not in event:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Request body missing."})
            }

        # Ensure 'body' is properly extracted
        body = event["body"]  
        
        # If API Gateway sends body as a string, parse it
        if isinstance(body, str):
            body = json.loads(body)

        text = body.get("text", "").strip()  # Extract 'text' safely

        if not text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Text input is required."})
            }

        # Amazon Comprehend Sentiment Analysis
        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')

        return {
            "statusCode": 200,
            "body": json.dumps({"sentiment": response['Sentiment']})
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON format in request body."})
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
