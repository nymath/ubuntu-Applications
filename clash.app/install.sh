#!/bin/sh

APP_PATH=$(dirname $(realpath $0))

sudo -v

sudo chmod a+x $APP_PATH/bin/clash

sudo python3 $APP_PATH/src/config.py

sudo systemctl enable clash
sudo systemctl restart clash
sudo systemctl status clash