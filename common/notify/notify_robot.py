import requests
import os

# "2aac663c6d2f"
def NotifyRobot(title, name, content):
    AUTODL_NOTIFY_TOKEN = os.getenv('AUTODL_NOTIFY_TOKEN')
    print(AUTODL_NOTIFY_TOKEN)
    resp = requests.post("https://www.autodl.com/api/v1/wechat/message/push",
                        json={
                            "token": AUTODL_NOTIFY_TOKEN,
                            "title": title,
                            "name": name,
                            "content": content
                        })

    print(resp.content.decode())

