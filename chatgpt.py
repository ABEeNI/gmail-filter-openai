import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
purpose_instructions = """
    You are a helpful assistant designed to output JSON. You will be prompted by a user's
    natural language request, who wants to create Gmail filters using Gmail API.
    Based on the user's input and the schema of the JSON object that the API endpoint
    awaits, you will generate the appropriate JSON output. Always provide the JSON object in
    the following format, containing all the following fields:
    {"criteria": { "from": "string", "to": "string", "subject": "string", "query": "string",
    "negatedQuery": "string", "hasAttachment": boolean, "excludeChats": boolean, "size": integer,
    "sizeComparison": "enum (SizeComparison)" }, "action": { "addLabelIds": ["string"], "removeLabelIds": ["string"],
    "forward": "string"} }
    All the fields that were not relevant from the users request even if they were boolean ones, should equal to null.
    """
def get_openai_api_key():
    """Retrieve the OpenAI API key from environment variables."""
    return os.getenv('OPENAI_API_KEY')

def interpret_user_request(user_input):
    """Use OpenAI API to map natural language to Gmail filter settings."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": purpose_instructions},
            {"role": "user", "content": user_input}
        ]
    )
    print(response.choices[0].message.content)

    return response.choices[0].message.content.strip()
