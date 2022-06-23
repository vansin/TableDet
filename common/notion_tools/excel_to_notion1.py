from notion_client.helpers import get_id
from notion_client import Client
import pandas as pd

# 从excel中读取数据
from common.notion_tools.search_word_in_pdf import search_word_in_pdf

import os

import arxiv
import re

NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")

while NOTION_TOKEN == "":
    print("NOTION_TOKEN not found.")
    NOTION_TOKEN = input("Enter your integration token: ").strip()

# Initialize the client
notion = Client(auth=NOTION_TOKEN)


database_id = 'c029ed80d2754bfb960a6ed951f04e00'
import mmcv


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


def axiv_data(page_id, Abs_url):

    data = dict(
        page_id=page_id,
        properties={
            "Abs_url": {
                "url": Abs_url
            }
        }
    )

    return data


if __name__ == "__main__":

    # parent_id, db_name = manual_inputs()
    # newdb = create_database(parent_id=parent_id, db_name=db_name)
    # print(f"\n\nDatabase {db_name} created at {newdb['url']}\n")

    df = pd.read_excel('/project/acceptedpapers.xlsx')

    records = df.to_dict(orient='records')
    recodds = mmcv.load('/project/cvpr2022.json')

    for i, record in enumerate(records):


        print('progress',i)
        if i in [62, 140]:
            continue

        search = arxiv.Search(
            query=record['Paper Title'],
            max_results=1
        )

        pdf_url = None
        entry_id = None

        for result in search.results():
            print(result.title)
            print(result.pdf_url)
            print(result.entry_id)
            Abs_url = result.entry_id




            get_short_id = result.entry_id.split('arxiv.org/abs/')[-1]
            nonempty_title = result.title if result.title else "UNTITLED"
            # Remove disallowed characters.
            clean_title = '_'.join(re.findall(r'\w+', nonempty_title))
            filename = "{}.{}.{}".format(get_short_id, clean_title, 'pdf')

            prefix = '/home/elaine/Documents/cvpr2022'

            record['file_path']=prefix+'/'+filename

            if not os.path.exists(prefix+'/'+filename):

                result.download_pdf(dirpath=prefix, filename=filename)
            else:
                print('已存在')

            print('score:',search_word_in_pdf(prefix+'/'+filename))


        # q_data = {
        #     "filter": {
        #         "property": "Paper Title",
        #         "rich_text": {
        #                     "contains": record["Paper Title"]
        #         }
        #     }
        # }

        # q = notion.databases.query(database_id, **q_data)
        # if len(q['results']) < 1:
        #     data = re_data(title=record['Paper Title'],
        #                    Authors=record['Authors'])
        #     r_json = notion.pages.create(**data)
        #     record['id'] = r_json['id']
        # else:
        #     record['id'] = q['results'][0]['id']

        # if Abs_url:

        #     data = axiv_data(record['id'], Abs_url)
        #     notion.pages.update(**data)
        #     #

    print(records)


    mmcv.dump(records, '111.json')


# 把excel的数据写到notion


# 给各个论文打标签
