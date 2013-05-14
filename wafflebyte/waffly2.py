import sys
import re # regex library
#import random

# testing modules!!!
# import test
# test.x()
# print test

# IMPORTING THE URLLIB2 LIBRARY
import urllib2
# from xml.dom.minidom import parseString

# IMPORTING BEAUTIFULSOUP LIBRARY
# from bs4 import BeautifulSoup

# IMPORTING HTML5 LIBRARY
# import html5lib
# from html5lib import treebuilders


meatball_set = set()
words = set()
articles = set()

########### urllib2 
# file = urllib2.urlopen('http://www.nytimes.com/RSS')
# data = file.read()
# file.close()
# articles = set()

# # # trying to read the body of the articles coming in
# dom = parseString(data)
# tmp = dom.getElementsByTagName("body")
# tmp = len(tmp)

# for index in range(1,tmp):
# xmlTag = dom.getElementsByTagName("body")[index].toxml()
# xmlData = xmlTag.replace('<description>','').replace('</description>', '')
# # this should add it to my set
# articles.add(xmlData.strip()) 
# print xmlData


########### beautiful soup

# soup = BeautifulSoup(open("nytimes.com"))


# HERE'S THE PART OF THE MIDTERM THAT WORKS

# look at this document for word extractors
for line in open('meatballs.txt'): 
  line = line.strip()
  line_words = line.split()
  for word in line_words:
    words.add(word)

  #for word in words:
    # print word
    # print words # this gives a huge error (sets of sets)
    # print line # this gives an error (printing multiple lines of same word)

text = sys.stdin.read()
textWords = re.split(r"(\W+)", text)
#print textWords


word_re = re.compile(r"^\w+$")
space_re = re.compile(r"^\s+$")


def f(triple):
  prev, curr, next = triple
  # determine if each string is a word
  is_c_word = word_re.match(curr)
  is_p_space = space_re.match(prev) if prev is not None else False
  is_next_space = space_re.match(next) if next is not None else False

  if is_c_word and is_p_space and is_next_space: # it's a real word and it is neighbored by spaces (not punctuation)
    return "&nbsp;" * len(curr)
  else:
    return curr

#FRAME SHIFT FUNCTION
def prev_curr_next_triples(seq):
  prev = [None] + seq[:-1]
  next = seq[1:] + [None]
  return zip(prev, seq, next)
#print prev_curr_next_triples(textWords)


rep_words = [f(triple) for triple in prev_curr_next_triples(textWords)]
print "".join(rep_words)





sys.exit(0)


# for all the lines in standard input (this provided text)
# for articleLine in sys.stdin:
#   articleLine = articleLine.strip()
#   articleLine = re.sub(r"\w", " ", articleLine)
#   print articleLine

#   for punct_match in re.findall(r'\w+\W \w+', articleLine):
#     print punct_match
  #articleLine = re.sub(r"\W", "A", articleLine) # debugging here



  #punctuation = [x for x in line.split(" ") if x in punctuation_set]
  # for x in line.split(" "):
  # 	if len(x)>0:
	 #  	if x[-1] in punctuation_set:
	 #  		punctuationList.append(x[-1])

  # for word in words 
  # meatballs = [x for x in line.split(" ") if x.lower() in words]
  # if len(words) > 0:
  #   print ' '.join(words)


