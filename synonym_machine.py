import nltk
import urllib
import json
import urllib2
from urllib import urlopen
from simplenlp import get_nl
from nltk.corpus import wordnet
import random
import sys

#this method replaces adjectives with a random synonym
def replace_adjectives_strip_pos(token):
  if(token[1] in ("JJ", "JJR", "JJS")):
    syn = [lemma.name for lemma in sum([ss.lemmas for ss in wordnet.synsets(token[0], wordnet.ADJ)],[])]
    if(len(syn)>0):
      return random.choice(syn)
    else:
      return token[0]
  else:
    return token[0]

# download Moby Dick by Herman Melville from Project Gutenberg
url = "http://www.gutenberg.org/cache/epub/2701/pg2701.txt"
raw_text = urlopen(url).read()

print "downloaded text..."
sys.stdout.flush()

# tokenize the story
tokens = nltk.word_tokenize(raw_text)
# apply part of speech tags to the tokens
pos_tokens = nltk.pos_tag(tokens)
print "labeled tokens..."
sys.stdout.flush()

#replace all adjectives with a synonym
adj_replaced_tokens = [replace_adjectives_strip_pos(x) for x in pos_tokens]
print "replaced adjectives..."
sys.stdout.flush()

#untokenize the text to create a single string. Clean up some of the dashes, which confuse reporting script
en_nl = get_nl('en')
replaced_text = en_nl.untokenize(" ".join(adj_replaced_tokens))#.replace(".",".\n")
replaced_text = replaced_text.replace("- -","--").replace(" --","--").replace("-- ","--")

# write modified literature to file
f = open(sys.argv[1], 'w')
f.write(replaced_text)
f.close()
