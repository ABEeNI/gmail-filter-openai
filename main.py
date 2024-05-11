import json
from gmail_auth import gmail_authenticate
from filters import create_filter, create_label, get_labels
from chatgpt import interpret_user_request

def remove_none_values(d):
    if not isinstance(d, dict):
        return d
    return {k: remove_none_values(v) for k, v in d.items() if v is not None and remove_none_values(v) is not None}

def main():

    service = gmail_authenticate()

    user_input = input("Enter your filter request: ")
    filter_content = interpret_user_request(user_input)

    filter_dict = json.loads(filter_content)

    # Create a new dictionary, only adding fields that are not null
    new_filter_dict = remove_none_values(filter_dict)

    # Check if label exists, if not create it
    labels = get_labels(service)
    label_name = new_filter_dict['action']['addLabelIds'][0]
    if label_name not in labels:
        label_content = {"name": label_name}
        label_id = create_label(service, label_content)
    else:
        label_id = labels[label_name]

    # Set the label's ID in the new dictionary
    new_filter_dict['action']['addLabelIds'][0] = label_id

    print(new_filter_dict)
    # Create filter
    filter_id = create_filter(service, new_filter_dict)


if __name__ == '__main__':
    main()
