#!/usr/bin/env python

import platform

WINDOWS_PLATFORM = 'Windows'
OSX_PLATFORM = 'Darwin'
LINUX_PLATFORM = 'Linux'

ARCH_64 = '64bit'
ARCH_32 = '32bit'

def show_platform():

    os_type = platform.system()
    os_arch = platform.architecture()[0]

    if os_type == WINDOWS_PLATFORM and os_arch == ARCH_64:
        return 'windows-amd64'
    
    if os_type == OSX_PLATFORM and os_arch == ARCH_64:
        return 'darwin-amd64'

    if os_type == LINUX_PLATFORM and os_arch == ARCH_64:
        return 'linux-amd64'
    
    raise Exception('cannot identified os type')

def main():
    print(show_platform())

if __name__ == '__main__':
    main()
