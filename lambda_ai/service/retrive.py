import boto3
from ddtrace.llmobs.decorators import retrieval
from ddtrace.llmobs import LLMObs

from botocore.exceptions import ClientError
@retrieval
def retrive(input_prompt):
  # Use the native inference API to send a text message to Anthropic Claude.

    # Create a Bedrock Runtime client in the AWS Region of your choice.
    client = boto3.client('bedrock-agent-runtime', region_name="us-east-1")
    # Set the model ID,
    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    kb_id = "ICQXXBQERM"
    # Define the prompt for the model.
    response = client.retrieve_and_generate(
        input={
            'text': input_prompt
        },retrieveAndGenerateConfiguration={
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kb_id,
                'modelArn': model_id,
            },
            'type': 'KNOWLEDGE_BASE'
        }
    )
    LLMObs.annotate(
        output_data=[
            {
                "score": 1,
                "name": "knowledgeBase",
                "id": '1',
                "text": response["output"]["text"] 
            }
        ]
    )
    
    return response["output"]["text"]
