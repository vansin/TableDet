
ln -s /media/elaine/data/datasets $(pwd)/data
ln -s /media/elaine/data/table_work_dirs $(pwd)/work_dirs
sudo ln -s /tmp/vansin/cvmart_data /home/data

# mkdir /tmp/ossfs

ln -s /tmp/ossfs work_dirs_no_pth
# ossfs moonstarimg /tmp/ossfs -o url=https://oss-cn-hangzhou.aliyuncs.com