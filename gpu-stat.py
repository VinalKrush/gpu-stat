#!/usr/bin/env python3
import os
import time
import sys

def main():
    # Is This A Nvidia System Or Not
    if not os.path.exists('/usr/bin/nvidia-smi'):
        print("Error: Nvidia Driver Not Detected!")
        print("Please make sure NVIDIA drivers are installed by running:")
        print("")
        print('"sudo pacman -S nvidia-dkms"')
        sys.exit(1)


    while True:
        os.system('clear')
        os.system('nvidia-smi')
        time.sleep(2)

if __name__ == "__main__":
    main()
