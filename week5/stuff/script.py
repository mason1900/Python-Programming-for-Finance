#!/home/martin/anaconda3 python

# import statements
import sys

#Taking command line arguments
param1 = sys.argv[1]


print("Hello, World {0:s}".format(param1)) 


if __name__ == '__main__':
    print("We are running a script from the command line.")
