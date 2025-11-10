#------------------------------------------------------------------------------------------------------
# You run this script as follows:
#
# python3.* hello.py argument
#
# where * is the version of Python
# where "argument" is your argument
#------------------------------------------------------------------------------------------------------

#import module sys which is a very standard one
import sys

#sys.argv[0] is the script name itself and can be ignored
word = sys.argv[1] #calls the first argument

#gather the code in a main() function
def main():
    print ('Hello there', word) 
    
#standard boilerplate to call the main() function to begin the program
if __name__ == '__main__':
    main()    
