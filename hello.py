#!/usr/bin/env python3

#python3.* hello.py argument
#where * is the version of Python
#where "argument" is your argument

#import module sys which is a very standard one
import sys

#gather the code in a main() function
def main():
    print ('Hello there', sys.argv[1]) #sys.argv[1] calls the first argument
                                       #sys.argv[0] is the script name itself and can be ignored
    
#standard boilerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()    
