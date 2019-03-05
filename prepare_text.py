# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:28:32 2019

@author: Prasanna Sritharan

Splits the text into sentences and writes to new output file

"""


from nltk import tokenize


# source file (txt)
source_file = 'walkersmanlyexer00walk_0_djvu.txt'

# output file (txt)
token_file = 'walkersmanlyexer00walk_0_djvu_tokenised.txt'

# open file and read entire contents
indata = open(source_file,'r')
fulltext = indata.read()

# tokenise text
sentences = tokenize.sent_tokenize(fulltext)

# write tokenised text
outdata = open(token_file,'w')
for sentence in sentences:
    # convert multi-line text into a single line by removing internal newlines
    sentence = sentence.replace('\n',' ').strip() + '\n'
    # join words split in original text
    sentence = sentence.replace('-  ','')
    # write the output file
    outdata.write(sentence)
    
# close output file
outdata.close()    