# main.py

import json
from gmail_auth import gmail_authenticate
from filters import create_filter, create_label
from chatgpt import interpret_user_request

def main():

    service = gmail_authenticate()

    # Prompt the user for the filter details
    user_input = input("Describe the Gmail filter you want to create: ")

    # Interpret user input via OpenAI
    filter_data = interpret_user_request(user_input)

    # Extract label name from the filter data
    label_name = None
    if '"addLabelIds":' in filter_data:
        label_name = input("Enter the label name if you want to create a new label or skip: ")

    # Create the label if necessary
    if label_name:
        label_id = create_label(service, label_name)
        filter_data = filter_data.replace("Label_123456", label_id)

    # Convert the filter_data string to a Python dictionary
    try:
        filter_data = json.loads(filter_data)
    except json.JSONDecodeError as error:
        print(f'Error decoding the JSON: {error}')
        return

    # Create the Gmail filter
    create_filter(service, filter_data)

if __name__ == '__main__':
    main()
