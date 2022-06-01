import os
os.mkdir('/project/train/models/1')
os.mkdir('/project/train/models/1/2')

with open('/project/train/models/1/2/data.txt','w') as f:    #设置文件对象
    f.write('fdsafsdafsaddfsdadfdasfsadfasdfsaf')                 #将字符串写入文件中