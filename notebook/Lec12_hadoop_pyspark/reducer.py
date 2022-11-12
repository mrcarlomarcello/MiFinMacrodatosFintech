import sys

from operator import itemgetter

current_word = None
current_count = 0 

word = None
# input to reducer comes from console
for line in sys.stdin:
	# remove any leading and trialing spaces
	line = line.strip()
	# split the line recieved from mapper using '\t'	
	word,count = line.split()

	try:
		# if count is convertable to number
		count = int(count)
	except ValueError:
		continue

	if current_word == word:
		current_count += count
	else:
		if current_word:
			print '%s\t%s' %(current_word, current_count)
		current_count = count
		current_word = word

# finally output the word to the console
if current_word == word:
	print '%s\t%s' %(current_word,current_count)
