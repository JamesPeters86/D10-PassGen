#!/usr/bin/python3
#phonetGen.py Generate phonetic tokens of various lengths based on combinations
#of vowels and consonants, prefixes, and/or suffixes

#Token Components
vowels = {"a","e","i","o","u","y"}
cons = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m","n", "p", "r", "s", "t", "v", "w", "x", "y", "z"}

presufs = {"sh", "ch", "st"}
prefs = { "tr", "qu", "str", "br", "gr", "fr", "kr", "pr", "vr", "pl", "kl", "sle"}
sufs = {"rt", "rst", "rb", "rg", "rf", "rk", "rm", "rn", "rp", "rs", "rv", "rz", "lp" "rx"}

tokens = []
#assemble tokens
# non-vowel, vowel
for vowel in vowels:
	for con in cons:
		tokens.append(con + vowel)

	for pref in prefs:
		tokens.append(pref + vowel)

	for pref in presufs:
		tokens.append(pref + vowel)

# vowel, non-vowel
for vowel in vowels:
	for con in cons:
		tokens.append(vowel + con)

	for suf in sufs:
		tokens.append(vowel + suf)

	for suf in presufs:
		tokens.append(vowel + suf)

# non-vowel, vowel, non-vowel
for vowel in vowels:
	for con1 in cons:
		for con in cons:
			tokens.append(con1 + vowel + con)

		for suf in sufs:
			tokens.append(con1 + vowel + suf)

		for suf in presufs:
			tokens.append(con1 + vowel + suf)

	for pref in prefs:
		for con in cons:
			tokens.append(pref + vowel + con)
	
		for suf in sufs:
			tokens.append(pref + vowel + suf)

		for suf in presufs:
			tokens.append(pref + vowel + suf)


	for pref in presufs:
		for con in cons:
			tokens.append(pref + vowel + con)

		for suf in sufs:
			tokens.append(pref + vowel + suf)

		for suf in presufs:
			tokens.append(pref + vowel + suf)

#print(len(tokens))
#trim doubles (should only be y's and u's)
lengs = [0,0,0,0,0,0,0,0]
for token in tokens:
	prev = None
	for letter in token:
		if None == prev:
			prev = letter
			continue
		
		if prev == letter:
			tokens.remove(token)
			break
		
		prev = letter

	lengs[len(token) - 1] += 1

for token in tokens:
	print(token)

quit()

#print(len(tokens))
idx = 0
for leng in lengs:
	idx += 1
	#print(str(idx) + ": " + str(leng))

#remove real words
fptr = open("english3.txt")
while True:
	line = fptr.readline()
	if "" == line:
		break

	line = line.strip()
	linelen = len(line)
	#we don't care about words that arelonger we are using and
	# The word database as false positives on two letter words
	if ( linelen > 7 or linelen <=2):
		continue

	for token in tokens:
		if line == token:
			tokens.remove(token)


#print(len(tokens))
lengs = [0,0,0,0,0,0,0,0]
for token in tokens:
	lengs[len(token) - 1] += 1

idx = 0
for leng in lengs:
	idx += 1
	print(str(idx) + ": " + str(leng))

