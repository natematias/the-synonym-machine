import sys

f = open(sys.argv[1], "r")
text = f.read()
#text = text.replace(".",".\n")
f.close()
text = text.replace("\r\n","").replace("\t"," ").replace("  "," ").replace("  "," ").replace("  ", " ").replace("  "," ").replace("  "," ")

f = open(sys.argv[2],"w")
f.write(text)
f.close()
