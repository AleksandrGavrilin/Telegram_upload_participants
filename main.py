import sys
from telethon.sync import TelegramClient
from telethon.tl.types import Channel


# replace with your own API and HASH identifiers:
API_ID = ''
API_HASH = ''


# replace with your own API and HASH identifiers:
def download_participants(client, chat_link):
    chat_entity = client.get_entity(chat_link)
    if isinstance(chat_entity, Channel):
        chat_id = chat_entity.id
    else:
        raise ValueError("Invalid chat link provided")

    output_file = f"{chat_id}_participants.txt"

    upload_participants(client, chat_id, output_file)


# uploading chat usernames to a file
def upload_participants(client, chat_id, output_file):
    with open(output_file, 'w') as file:
        for participant in client.get_participants(chat_id):
            if hasattr(participant, 'username'):
                file.write(f"{participant.username}\n")


# launch the utility
def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <chat link>')
    else:
        chat_link = sys.argv[1]
        client = TelegramClient('session', API_ID, API_HASH)

        with client:
            download_participants(client, chat_link)
            print("Members have been successfully downloaded.")


if __name__ == '__main__':
    main()
