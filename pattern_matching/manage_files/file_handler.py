# devoriales.com, 2022
# Path: pattern_matching/manage_files/file_handler.py
# Description: Handling files using switch case and match statement

'''
command is the parameter of the commander function
*file gets unpacked and is used as a parameter for the os.system function
'''
import os

command = input("Enter a command and a file: ")


def commander(command):
    match command.split():
        case ["help" | "h" | "?", *file ] if "--ask" in command: # if --ask is in the command then print the help message
            print("Commands: cat, rm, ls, mv, cp, touch, mkdir, rmdir, pwd, cd")
        case ["cat", *file]: # if cat is in the command then print the file
            files = [print(os.system(f"cat {x}")) for x in file] # prints the file if it exists by using list comprehension 
        case ["rm" | "remove" | "delete", *file]:
            print(os.system(f"rm {file}"))
        case ["ls" | "list", *file]:
                print(os.system(f"ls {file}"))
        case ["mv" | "move", *file]:
                print(os.system(f"mv {file}"))
        case ["cp" | "copy", *file]:
            print(os.system(f"cp {file}"))
        case ["touch", *file]:
            for x in file:
                print(os.system(f"touch {x}"))
        case ["mkdir" | "make directory", *file]:
            print(os.system(f"mkdir {file}"))
        case ["rmdir" | "remove directory", *file]:
            print(os.system(f"rmdir {file}"))
        case ["pwd" | "print working directory", *file]:
            print(os.system(f"pwd {file}"))
        case ["cd" | "change directory", *file]:
            print(os.system(f"cd {file}"))
        case _:
            print("Command not found")


commander(command)
