import sys

filename = sys.argv[1]

f = open(filename, "rt")
text = f.read()
chunks = text.split("\n")
plaintext = ""
for c in chunks:
	plaintext = plaintext + " " + c

outfile = open(filename+"_split","w")
prev = ""
for t in plaintext:
	if (prev == "." and t == "."):
		continue

	if (t in (".","?","!",":")):
		outfile.write(t+"\n")
	else:
		outfile.write(t)
	prev = t

outfile.close()
