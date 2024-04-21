import time

import requests

with open("token.txt", "r") as file:
    TOKEN = file.read()

session = requests.Session()
session.headers = {
    "X-Privy-Token": TOKEN
}


def get_posts():
    r = session.get(
        "https://api.meme.fun/ticker/0x692e17abe7c736f689389807c6c4fcebeca527ff9d7974a18b9c46b189e2f559" +
        "/posts?sort=recent"
    )

    return [i["id"] for i in r.json()["posts"]]


def set_like(post_id):
    r = session.post(
        "https://api.meme.fun/ticker/0x692e17abe7c736f689389807c6c4fcebeca527ff9d7974a18b9c46b189e2f559" +
        f"/post/{post_id}/vote",
        json={"upvote": True}
    )

    print(r.json())


def main():
    while True:
        ids = get_posts()

        for i in ids:
            set_like(i)
            time.sleep(1)

        time.sleep(900)


if __name__ == '__main__':
    main()
