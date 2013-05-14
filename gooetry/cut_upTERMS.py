import sys
import random
 
article = list()
 
for line in open('commentsterms.txt'):
	# strip the lines of carriage returns etc
	line = line.strip()
	# add this data to the set
	article.append(line)
 
random.shuffle(article)
 
comments = list()
 
for line in open('william_comment.txt'):
	line2 = line.strip()
	comments.append(line2)
 
random.shuffle(comments)
 
for line, line2 in zip(article, comments):
	print line, line2