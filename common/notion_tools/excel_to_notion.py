from notion_client.helpers import get_id
from notion_client import Client
import pandas as pd

# 从excel中读取数据


import os

import arxiv


NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")

while NOTION_TOKEN == "":
    print("NOTION_TOKEN not found.")
    NOTION_TOKEN = input("Enter your integration token: ").strip()

# Initialize the client
notion = Client(auth=NOTION_TOKEN)


def manual_inputs(parent_id="", db_name="") -> tuple:
    """
    Get values from user input
    """
    if parent_id == "":
        is_page_ok = False
        while not is_page_ok:
            input_text = input("\nEnter the parent page ID or URL: ").strip()
            # Checking if the page exists
            try:
                if input_text[0:4] == "http":
                    parent_id = get_id(input_text)
                    print(f"\nThe ID of the target page is: {parent_id}")
                else:
                    parent_id = input_text
                notion.pages.retrieve(parent_id)
                is_page_ok = True
                print("Page found")
            except Exception as e:
                print(e)
                continue
    while db_name == "":
        db_name = input("\n\nName of the database that you want to create: ")

    return (parent_id, db_name)


def create_database(parent_id: str, db_name: str) -> dict:
    """
    parent_id(str): ID of the parent page
    db_name(str): Title of the database
    """
    print(f"\n\nCreate database '{db_name}' in page {parent_id}...")
    properties = {
        "Name": {"title": {}},  # This is a required property
        "Description": {"rich_text": {}},
        "In stock": {"checkbox": {}},
        "Food group": {
            "select": {
                "options": [
                    {"name": "🥦 Vegetable", "color": "green"},
                    {"name": "🍎 Fruit", "color": "red"},
                    {"name": "💪 Protein", "color": "yellow"},
                ]
            }
        },
        "Price": {"number": {"format": "dollar"}},
        "Last ordered": {"date": {}},
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {"name": "Duc Loi Market", "color": "blue"},
                    {"name": "Rainbow Grocery", "color": "gray"},
                    {"name": "Nijiya Market", "color": "purple"},
                    {"name": "Gus's Community Market", "color": "yellow"},
                ]
            },
        },
        "+1": {"people": {}},
        "Photo": {"files": {}},
    }
    title = [{"type": "text", "text": {"content": db_name}}]
    icon = {"type": "emoji", "emoji": "🎉"}
    parent = {"type": "page_id", "page_id": parent_id}
    newdb = notion.databases.create(
        parent=parent, title=title, properties=properties, icon=icon
    )

    # notion.databases.update()

    return newdb


database_id = 'c029ed80d2754bfb960a6ed951f04e00'

def re_data(database_id='c029ed80d2754bfb960a6ed951f04e00', title='', Authors=''): 
    
    data = dict(
        parent={'database_id': database_id},
        properties={
            'Paper Title': {
                'title': [
                    {
                        'text': {
                            'content': title
                        }}
                ]
            },

            "Tags": {
                "multi_select": [
                    {
                        "name": 'CVPR2022'
                    }
                ]
            },

            # "Authors": {
            #     "rich_text": [
            #         {
            #             "type": "text",
            #             "text": {
            #                 "content": Authors
            #             }
            #         }]}



        }
    )

    return data


if __name__ == "__main__":

    # parent_id, db_name = manual_inputs()
    # newdb = create_database(parent_id=parent_id, db_name=db_name)
    # print(f"\n\nDatabase {db_name} created at {newdb['url']}\n")





    df = pd.read_excel('/project/acceptedpapers.xlsx')


    records = df.to_dict(orient='records')
    for i,record in enumerate(records):

        print(i)

        search = arxiv.Search(
        query  = record['Paper Title'],
        max_results = 1
        )

        for result in search.results():
            print(result.title)
            result.download_pdf(dirpath='/home/elaine/Documents/cvpr2022')


        q_data = {
                    "filter": {
                        "property": "Paper Title",
                        "rich_text": {
                            "contains": record["Paper Title"]
                        }
                    }
                }
        
        q = notion.databases.query(database_id, **q_data)
        if len(q['results'])<1:
            data = re_data(title=record['Paper Title'], Authors=record['Authors'])
            r_json = notion.pages.create(**data)
            record[id]=r_json['id']



    print(records)

    import mmcv

    mmcv.dump(records, '111.json')


# 把excel的数据写到notion



# 给各个论文打标签
