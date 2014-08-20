import nltk
import urllib
import json
import urllib2
from urllib import urlopen
from simplenlp import get_nl
from nltk.corpus import wordnet
import random
import sys
import string
import pickle
import readline

#this method replaces adjectives with a random synonym
def replace_adjectives_strip_pos(token):
  if(token[1] in ("JJ", "JJR", "JJS")):
    syn = ["<strong>" + lemma.name.replace("_"," ") + "</strong>" for lemma in sum([ss.lemmas for ss in wordnet.synsets(token[0], wordnet.ADJ)],[])]
    if(len(syn)>0):
      return random.choice(syn)
    else:
      return token[0]
  else:
    return token[0]

def replace_nouns_strip_pos(token):
  if(token[1] in ("NN", "NNS")):
    syn = ["<strong>" + lemma.name.replace("_"," ") + "</strong>" for lemma in sum([ss.lemmas for ss in wordnet.synsets(token[0], wordnet.NOUN)],[])]
    if(len(syn)>0):
      return random.choice(syn)
    else:
      return token[0]
  else:
    return token[0]

# if there's punctuation, split off the punctuation along with the final word
# otherwise just split off the final word
def split_final_word_from_line(pos_tokens):
  length = len(pos_tokens)
  if(length == 0):
    return [],[]
  if pos_tokens[-1][0] in string.punctuation:
    if(length>1):
      n = pos_tokens[0:-2],pos_tokens[-2:]
      return n
    else:
      return [], [pos_tokens[-1]]
  else:
    return pos_tokens[0:-1],[pos_tokens[-1]]

# download Moby Dick by Herman Melville from Project Gutenberg
url = "http://www.gutenberg.org/cache/epub/2701/pg2701.txt"
# download Heart of Darkness by Joseph Conrad from Project Gutenberg
url = "http://www.gutenberg.org/cache/epub/526/pg526.txt"
# download the collected works of Emily Dickinson
url = "http://www.gutenberg.org/cache/epub/12242/pg12242.txt"
# download the Tractatus by Wittgenstein (known transcription errors)
#url = "http://natematias.com/medialab/tractatus.txt"
# download Don Quixote by Cervantes
url = "http://www.gutenberg.org/cache/epub/996/pg996.txt"

raw_text = urlopen(url).read()

print "downloaded text..."
sys.stdout.flush()
f = open(sys.argv[1], 'w')
for line in raw_text.split('\n'):

# tokenize the story
  tokens = nltk.word_tokenize(line)
# load a brill tagger trained by nltk-trainer
# https://github.com/japerk/nltk-trainer
  #tagger = pickle.load("/Users/nathan/nltk_data/taggers/treebank_brill_aubt.pickle")
# apply part of speech tags to the tokens
  pos_tokens = nltk.pos_tag(tokens)

# for rhyming poetry, split final word from line:
  front_tokens, end_tokens = split_final_word_from_line(pos_tokens)

  #print "labeled tokens..."

#replace all adjectives with a synonym
  #adj_replaced_tokens = [replace_adjectives_strip_pos(x) for x in pos_tokens]
  noun_replaced_tokens = [replace_nouns_strip_pos(x) for x in front_tokens]
  #print "replaced nouns..."
  sys.stdout.flush()

#untokenize the text to create a single string. Clean up some of the dashes, which confuse reporting script
  en_nl = get_nl('en')
  #replaced_text = en_nl.untokenize(" ".join(adj_replaced_tokens))#.replace(".",".\n")
  replaced_text = en_nl.untokenize(" ".join(noun_replaced_tokens + [x[0] for x in end_tokens]))
  #print sys.stdout.write(".")
  sys.stdout.flush()

# write modified literature to file
  f.write("<pre>\n")
  f.write(replaced_text + "\n")
  f.write("</pre>\n")
f.close()
