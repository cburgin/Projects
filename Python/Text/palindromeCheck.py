__author__ = "Colin Burgin"
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Colin Burgin"
__email__ = "cburgin707@gmail.com"
__status__ = "Complete"


#I am following 'http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/' list of projects in order to learn Python3
#Palindrome Check - This program is deisgned to check if a word is a palindrome, that is
#it is the same work if it is reversed.

inputVar = input("Enter a word: ")
if inputVar.lower() == inputVar[::-1].lower():
	print( inputVar + " is a palindrome.\n")
else:
	print( inputVar + " is not a palindrome.\n")