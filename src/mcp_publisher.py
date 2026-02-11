import json

def publish_recommendation(message):
    """
    Simulates MCP publishing (SNS/SQS)
    """
    print("\n[MCP MESSAGE SENT]")
    print(json.dumps(message, indent=2))
