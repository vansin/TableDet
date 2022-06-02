#! /bin/bash

# mkdir /tmp/vansin_ram
# sudo mount -t tmpfs -o size=72G tmpfs /tmp/vansin_ram


# cp /home/tml/datasets/datasets.zip /tmp/vansin_ram/datasets.zip
# unzip /tmp/vansin_ram/datasets.zip -d /tmp/vansin_ram
# ln -s /tmp/vansin_ram/datasets $(pwd)/data


mkdir /tmp/vansin
sudo mount -t cifs -o username=vansin,password=Tml768300.,uid=$(id -u),gid=$(id -g) //v4.vansin.top/vansin /tmp/vansin
if [ $? != 0 ]; then
sudo mount -t cifs -o username=vansin,password=Tml768300.,uid=$(id -u),gid=$(id -g) //192.168.4.21/vansin /tmp/vansin
sudo mount -t cifs -o username=vansin,password=Tml768300.,uid=$(id -u),gid=$(id -g) //10.52.130.37/vansin /tmp/vansin
fi

ln -s /tmp/vansin/datasets $(pwd)/data
ln -s /tmp/vansin/work_dirs $(pwd)/work_dirs
sudo ln -s /tmp/vansin/cvmart_data /home/data
