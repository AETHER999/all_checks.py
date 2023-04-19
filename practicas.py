#!/usr/bin/env python3
import os
import sys



def main():
    if check_reboot():
        print("pending reboot.")
        sys.exit(1)
    print("everythin ok.")
    sys.exit(0)

    main()
