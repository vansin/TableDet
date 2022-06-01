# -*- coding: utf-8 -*-

import oss2
import os
 
OSS_ACCESS_KEY_ID = os.getenv('OSS_ACCESS_KEY_ID')
OSS_ACCESS_KEY_SECRET = os.getenv('OSS_ACCESS_KEY_SECRET')
OSS_ENDPOINT = os.getenv('OSS_ENDPOINT')


print(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET, OSS_ENDPOINT)

endpoint = OSS_ENDPOINT # Suppose that your bucket is in the Hangzhou region.
auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
bucket = oss2.Bucket(auth, endpoint, 'moonstarimg')
# The object key in the bucket is story.txt
# key = 'story.txt'
# # Upload
# bucket.put_object(key, 'Ali Baba is a happy youth.')
# # Download
# bucket.get_object(key).read()
# # Delete
# bucket.delete_object(key)


# # Traverse all objects in the bucket
# for object_info in oss2.ObjectIterator(bucket):
#     print(object_info.key)


