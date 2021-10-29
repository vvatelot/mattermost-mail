from easyimap import connect as imap_connect
from easyimap.easyimap import MailObj
from environ import Env
from requests import post

env = Env(DEBUG=(bool, False), MAIL_LIMIT=(int, 10))

Env.read_env()


def format_message(email: MailObj) -> str:
    return (
        f":tada: Un nouveau message mail de *{email.from_addr}* a été envoyé sur la boite mail: **{email.title}** \n\n"
        "```quote \n"
        f"{email.body}"
        "\n```"
    )


def main() -> None:
    for email in imap_connect(
        host=env.str("MAIL_SERVER"),
        user=env.str("MAIL_USER"),
        password=env.str("MAIL_PASSWORD"),
    ).unseen(limit=env.int("MAIL_LIMIT")):
        if env.bool("DEBUG"):
            print(format_message(email))

        else:
            result = post(
                url=env("MATTERMOST_WEBHOOK_URL"),
                json={"text": format_message(email=email)},
            )
            print(result)


if __name__ == "__main__":
    main()
