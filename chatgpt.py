# chatgpt.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_openai_api_key():
    """Retrieve the OpenAI API key from environment variables."""
    return os.getenv('OPENAI_API_KEY')

def interpret_user_request(user_input):
    """Use OpenAI API to map natural language to Gmail filter settings."""

    prompt = f'''
    Given a user's natural language request, generate a Gmail filter in JSON format.

    Example 1:
    Input: "Filter all emails from `example@domain.com` to the label `Work`."
    Output: {{
        "criteria": {{
            "from": "example@domain.com"
        }},
        "action": {{
            "addLabelIds": ["Label_123456"]
        }}
    }}

    Example 2:
    Input: "Filter emails from `newsletter@example.com` containing the word `news` to the label `Newsletters`."
    Output: {{
        "criteria": {{
            "from": "newsletter@example.com",
            "query": "news"
        }},
        "action": {{
            "addLabelIds": ["Label_123457"]
        }}
    }}

    Example 3:
    Input: "{user_input}"
    Output:
    '''

    response = client.chat.completions.create(model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant that translates user requests into JSON Gmail filters."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=200,
    temperature=0)

    return response.choices[0].message.content.strip()
