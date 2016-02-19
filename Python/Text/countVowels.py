__author__ = "Colin Burgin"
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Colin Burgin"
__email__ = "cburgin707@gmail.com"
__status__ = "Complete"


#I am following 'http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/' list of projects in order to learn Python3
#Count Vowels - This program is deisgned to count all of the vowels in a string

inputVar = input("Enter a string and learn how many vowels it contains: ")

aCount = 0
eCount = 0
oCount = 0
iCount = 0
uCount = 0
totalCount = 0

for character in inputVar:
	if character == 'a' or character == 'A':
		aCount = aCount + 1
	elif character == 'e' or character == 'E':
		eCount = eCount + 1
	elif character == 'i' or character == 'I':
		iCount = iCount + 1
	elif character == 'o' or character == 'O':
		oCount = oCount + 1
	elif character == 'u' or character == 'U':
		uCount = uCount + 1
		
totalCount = aCount + eCount + iCount + oCount + uCount

print( "In the string '" + inputVar + "', there are:\n"
		, aCount , " occurence(s) of the vowel A\n"
		, eCount , " occurence(s) of the vowel E\n"
		, iCount , " occurence(s) of the vowel I\n"
		, oCount , " occurence(s) of the vowel O\n"
		, uCount , " occurence(s) of the vowel U\n"
		, totalCount , " vowels total in the stirng.\n")