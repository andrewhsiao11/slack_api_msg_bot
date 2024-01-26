def send_slack_message(message: str):
    import requests

    payload = '{"text": "%s"}' % message
    response = requests.post(
        "SLACK ACCOUNT HOOK HERE",
        data=payload
    )
    print(response.text)


def main(message_text: str):

    send_slack_message(message=message_text)


msg = 'hello world'

if len(msg) > 0:
    main(message_text=msg)
else:
    print('Give me a message')