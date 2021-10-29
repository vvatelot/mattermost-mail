# Mattermost Email Notification

This is a simple bot that reads incoming emails in mailbox with imap and sends a notification to a Mattermost Webhook.

## Requirements

- Python ^3.8
- Mattermost instance (obviously!)

## Configuration

- Install dependencies:

```bash
pip install --user -r requirements.txt
```

- Copy paste `.env.dist` file to `.env`
- Set your own imap and mattermost parameters
- Optional parameters :
  - `MAIL_LIMIT` (int=10): To set the limit of number of emails to be polled at once
  - `DEBUG` (bool=False): If set to `True`, does not send messages on webhook

## Use

Just run the command

```bash
python main.py
```
