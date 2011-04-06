"""
Mspacman is a makepkg and pacman wrapper/helper with a focus on PKGBUILD.
It accepts several flags that define its' behavior and passes most of the work
to the makepkg and pacman programs. As of right now, mspacman is only
performing limited functions:
    -search both the package database and AUR
    -grab tarballs from the AUR
    -create and install packages from tarballs
    -install from package database via pacman

There is currently no dependency checking, but it will be implemented in the
future as that was a prime motivation for the creation of this tool.

The currenly supported flags are:
    -I  install package according to the following modifiers
        l   local tarball or PKGBUILD file
        r   grab tarball and install from AUR
        p   offically supported package (pacman -S)
    
    -S  search for package or PKGBUILD
        a   AUR
        p   official package database
        b   search both

    -H,--help   print this information
"""

import sys

error = False
error_text = ""

def print_help():
    print("printing help")

    return

def parse_flags(args):
    print("parsing flags:\n", args)

    functions = {   'S':search,
                    'I':install }
    
    if args[1][0] == '-' and args[1][1] in functions:
        functions[args[1][1]]()
        return
    else:
        print("ERROR: Invalid Argument")
        global error
        error = True
        return
    """
    if args[1][0] != '-':
        error = True
        error_text = "first argument must be a flag"

        return

    elif args[1][1] == 'I':
        if len(args[2]) >= 1:
            install()
        else:
            error = True
            error_text = "installation requires package name"

            return
        """
    
    return

def search():
    print("searching...")

def install():
    print("installing...")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_help()
    else:
        parse_flags(sys.argv)

    if error == True:
        print_help()
