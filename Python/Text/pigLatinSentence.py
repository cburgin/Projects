__author__ = "Colin Burgin"
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Colin Burgin"
__email__ = "cburgin707@gmail.com"
__status__ = "Complete"


#I am following 'http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/' list of projects in order to learn Python3
#Pig Latin – Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

words = str(input("Enter a sentence to be converted to Pig Latin: ")).split()
for word in words:
	print( word[1:] + word[0] + "ay", end = " ")
print()