# main.py

import json
from gmail_auth import gmail_authenticate
from filters import create_filter, create_label
from chatgpt import interpret_user_request

def main():

    service = gmail_authenticate()

    label_content = {
          "name": "TEST_LABEL",
          "messageListVisibility": "show",
          "labelListVisibility": "labelShow"
        }

    label_id = create_label(service, label_content)
    print(f'Label ID: {label_id}')

if __name__ == '__main__':
    main()
