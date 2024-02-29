#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Returns true if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("pending reboot.")
        sys.exit(1)
# Agregar print y luego sys.exit(0)
    print("Everything ok.")
    sys.exit(0)

main()
