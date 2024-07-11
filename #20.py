#
# This week, we're going to spend a bit of time exploring a useful module in Python's standard library: argparse. This module allows you to create command-line programs that take arguments from the user.  You can, of course, do that with sys.argv, but then you need to parse the arguments yourself. argparse does a lot of that work for you.
#
# For this week's exercise, I want you to implement a single program that combines two classic Unix command-line programs, "head" and "tail".  The "head" command shows you the first few lines of a file, and the "tail" command shows you the final two lines of a file. Our "headtail" program will show you the first few *and* the last few lines of a file. If the user doesn't specify the number of lines he or she wants to see from the start and end, then the default number will be 3.
#
# For the purposes of this exercise, we'll assume that the file can fit into memory.
#
# The program will have three command-line arguments:
# -s or --start, indicating how many lines to show from the start (default = 3)
# -e or --end, indicating how many lines to show from the end (default = 3)
# -f or --file, indicating the name of the file we want to display the start end of
#
# There is no default filename; it's OK for the program to die if the user fails to provide one.  Better, of course, would be to trap the error and inform the user of the problem.
#


import argparse
import sys

def read_lines(file_path,start_lines,end_lines):

    try:
        with open(file_path,'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File {file_path} doesn't exist")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

    start_part = lines[:start_lines]
    end_part = lines[-end_lines:] if end_lines !=0 else []
    return start_part, end_part


def main():
    parser = argparse.ArgumentParser(description="Display the first and last few lines of a file")
    parser.add_argument('-s','--start',type=int,default=3,help="Number of lines to show from the top (default 3)")
    parser.add_argument('-e','--end',type=int,default=3,help='Number of lines to show from the bottom (default 3)')
    parser.add_argument('-f','--file',required=True, help="File name to display lines from")

    args = parser.parse_args()

    start_lines = args.start
    end_lines = args.end
    file_path = args.file

    start_part, end_part = read_lines(file_path,start_lines, end_lines)

    print("".join(start_part))
    if start_part and end_part:
        print("...")
    print("".join(end_part))


if __name__ == "__main__":
    main()
