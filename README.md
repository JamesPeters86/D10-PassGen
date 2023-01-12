# D10-PassGen
A D10 based phonetic password generator similar to diceware. Instead of using english words it uses phonetic tokens like "sus" or "af" These offer a bit higher entropy per digit. So they are little easier to type at the expense of being a bit harder to remember. 
## Usage
```
./passGen
```
Then you just a roll a D-10 4 times for each token. Since it is a little shy of 3333 words, you have to reroll if you get higher than 9983. A password containing 5 tokens, will take about 6 years to guess assuming 1 billion guesses per second.

You can also generate random special characters. You only need to roll the dice twice for special characters. 
```
./special
```

### Project Goals
- Produce a password generator that was:
  - Readily verifiable even by noivce programmers
  - Trustworthy to be random
### Verifiability. 
- The two relavent scripts total less than 100 lines of code, and are very straightforward.
- Verifyng that all tokens on the list are 2 or 3 digits can easily be done with stats scripts
- Verifying the uniqueness of every entry can be done by comparing the output of wc with sort -u | wc
