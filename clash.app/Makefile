# Variables
APP_PATH := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


.PHONY: all
all: run 

run:
	@sudo -v
	@sudo chmod a+x $(APP_PATH)/bin/clash
	sudo python3 $(APP_PATH)/src/config.py
	@sudo systemctl enable clash
	@sudo systemctl restart clash
	@sudo systemctl status clash