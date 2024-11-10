import os
import sys

abs_config_path = os.path.abspath(__file__)
clash_path = os.path.dirname(os.path.dirname(abs_config_path))
config_path = os.path.join(clash_path, "config")
clash_exe_path = os.path.join(clash_path, "bin/clash")


def generate_clash_service_file():
    service_content = f"""[Unit]
Description=Clash daemon, A rule-based proxy in Go.
After=network.target

[Service]
Type=simple
Restart=always
ExecStart={clash_exe_path} -d {config_path}

[Install]
WantedBy=multi-user.target"""
    return service_content


if __name__ == "__main__":
    service_file_content = generate_clash_service_file()

    service_directory = '/etc/systemd/system/'
    os.makedirs(service_directory, exist_ok=True)
    with open('/etc/systemd/system/clash.service', 'w') as file:
        file.write(service_file_content)
