# filters.py
from googleapiclient.errors import HttpError


def create_label(service, label):
    """Create a new label in Gmail and return the label ID."""
    """label = {
        'labelListVisibility': 'labelShow',
        'messageListVisibility': 'show',
        'name': label_name
    }"""

    try:
        result = (
            service.users()
            .labels()
            .create(userId='me', body=label)
            .execute()
        )
        print(f'Created label {label.get("name")} with ID: {result["id"]}')
        return result['id']
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def get_labels(service):
    """Retrieve all labels in the user's mailbox."""
    try:
        result = (
            service.users()
            .labels()
            .list(userId='me')
            .execute()
        )
        labels = result.get('labels', [])
        return {label['name']: label['id'] for label in labels}
    except HttpError as error:
        print(f'An error occurred: {error}')
        return {}

def create_filter(service, filter_content):
    """Create a Gmail filter using the provided data."""
    try:
        result = (
            service.users()
            .settings()
            .filters()
            .create(userId="me", body=filter_content)
            .execute()
        )
        print(f'Created filter with ID: {result.get("id")}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        result = None

    return result.get("id")