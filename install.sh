#!/bin/bash

pacman -S --needed python3 python-pip

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Move the script to /usr/bin/ and make it executable
touch /usr/bin/gpu-stat
cp gpu-stat.py /usr/bin/gpu-stat
chmod +x /usr/bin/gpu-stat

echo "gpu-stat installed successfully"