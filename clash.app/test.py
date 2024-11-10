import os
import subprocess
import tempfile
import requests
from urllib.request import urlretrieve
import sh


def run():
    subprocess.run(['sudo', '-v'], check=True)
    app_path = os.path.dirname(os.path.realpath(__file__))
    subprocess.run(['ls'], check=True) 
    print(sh.pwd())
    print(sh.mkdir("test"))
    # subprocess.run(['sudo', 'chmod', 'a+x', os.path.join(app_path, 'bin', 'clash')], check=True)
    # subprocess.run(['sudo', 'python3', os.path.join(app_path, 'src', 'config.py')], check=True)
    # subprocess.run(['sudo', 'systemctl', 'enable', 'clash'], check=True)
    # subprocess.run(['sudo', 'systemctl', 'restart', 'clash'], check=True)
    # subprocess.run(['sudo', 'systemctl', 'status', 'clash'], check=True)


if __name__ == '__main__':
    run()