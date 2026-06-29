# ----------------------------------------------------------------------------------------------------------
# Last modified: 29 June 2026
# 
# Printing a sentence
#
#   Usage:
#       python3.12 hello.py argument
#
#   Developed and tested with Python 3.12; other versions may work but are untested.
# ----------------------------------------------------------------------------------------------------------

# Import module sys, which is a very standard one
import sys

# sys.argv[0] is the script name itself and can be ignored
word = sys.argv[1] # Calls the first argument

# Gather the code in a main() function
def main():
    print ('Hello there', word) 
    
# Standard boilerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()
