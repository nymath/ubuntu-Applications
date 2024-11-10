# Variables
APP_PATH := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# FRP_VERSION := $(shell curl -s https://api.github.com/repos/fatedier/frp/releases/latest | grep tag_name | cut -d '"' -f 4)
# FRP_VERSION_NUM := $(shell echo $(FRP_VERSION) | cut -c 2-)
# FRP_DOWNLOAD_URL := https://github.com/fatedier/frp/releases/download/$(FRP_VERSION)/frp_$(FRP_VERSION_NUM)_linux_amd64.tar.gz
# TEMP_DIR := $(shell mktemp -d)

.PHONY: all
all: run update

# update:
# 	@echo "Downloading frp version $(FRP_VERSION)..."
# 	@wget -q --show-progress $(FRP_DOWNLOAD_URL) -P $(TEMP_DIR)
# 	@echo "Extracting..."
# 	@tar -xzvf $(TEMP_DIR)/frp_$(FRP_VERSION_NUM)_linux_amd64.tar.gz -C $(TEMP_DIR)
# 	@echo "Installing..."
# 	@sudo mv -f $(TEMP_DIR)/frp_$(FRP_VERSION_NUM)_linux_amd64/frpc "$(SCRIPT_DIR)/bin/frpc"
# 	@sudo mv -f $(TEMP_DIR)/frp_$(FRP_VERSION_NUM)_linux_amd64/frps "$(SCRIPT_DIR)/bin/frps"
# 	@echo "Cleaning up..."
# 	@rm -rf $(TEMP_DIR)

run:
	@sudo -v
	@sudo chmod a+x $(APP_PATH)/bin/clash
	sudo python3 $(APP_PATH)/src/config.py
	@sudo systemctl enable clash
	@sudo systemctl restart clash
	@sudo systemctl status clash