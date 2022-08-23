import shutil
from time import sleep

if __name__ == '__main__':
    while True:
        shutil.rmtree('data')
        sleep(24 * 3600)