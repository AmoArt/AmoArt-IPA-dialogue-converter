# coding: latin1
import os
import os.path
import re
import sys

gTESTfile = open('TEST_g_val.txt', "r")
dictIPA={}

file = open('raw_IPA.txt', 'r', encoding='utf-8') #latin-1 #utf-8-sig
lines = file.readlines()

xxx=""
for line in lines:
    y = str(line.strip())
    m = re.compile('(.*?( ))(.*\/)')
    g = m.search(y) 

    if g:
    #    print(g.group(1))
    #    print(g.group(3))
        a = str(g.group(1)).strip() #.encode('utf_32').decode('utf_32') #word
        
        b = str(g.group(3)).strip() #.encode('latin1') #.encode('utf_32').decode('utf_32') #pronacation
        b = re.sub('\u200d', '', b)
        b = b.encode('UTF-8')

       # print(a)
        #print(b)
        
        dictIPA[a]=b.decode('UTF-8')  #.decode('latin1')
#print(str(dictIPA))


#####################################################################################################
def wordSwap(sentence, dictionary):
    sentence = sentence.upper() #convert all letters to upper for dictionary
    sentence = sentence.replace(',', ' -comma- ') #remove comma
    sentence = sentence.replace('.', ' -dot- ')
    sentence = sentence.replace(':', ' -colon- ') 
    sentence = sentence.replace('!', ' -exclamation- ')
    sentence = sentence.replace('?', ' -question- ')
    sentence = " ".join([dictionary.get(w,w) for w in sentence.split()]) #normal words to ARPAbet words
    sentence = sentence.replace(' -comma- ', ',') #get comma (and all other junk) back 
    sentence = sentence.replace(' -colon- ', ':')
    sentence = sentence.replace(' -exclamation- ', '!')
    sentence = sentence.replace(' -question- ', '?')
    sentence = sentence.replace(' -dot- ', '.')
    sentence = sentence.replace('-comma-', ',')
    sentence = sentence.replace('-colon-', ':') 
    sentence = sentence.replace('-exclamation-', '!')
    sentence = sentence.replace('-question-', '?')
    sentence = sentence.replace('-dot- ', '. ')
    sentence = sentence.replace(' -dot-', ' .')
    return sentence
####################################################################################################

print("""paste directory to your taining text file, Example: C:\Folder\training.txt""")
getFile = open(input(), "r").read()


#smallWords = gTESTfile.read()
smallWords = getFile

getSplit = re.split(r'(?<=\|)(.*?)(?=\;)', smallWords)

y = 1
for lines in getSplit:
    if not lines.strip(): continue
    y = y+1

textPrint = ""
x=1
for lines in getSplit:
    if not lines.strip(): continue
    
    if not x % 2:
        lines = lines.upper()
        lines = wordSwap(lines, dictIPA)
        textPrint = textPrint + lines
        #print(lines)
    ###print(lines, x)
    if x % 2:
        textPrint = textPrint + lines
    x = x+1
    
    #print(textPrint)
    if x == y:
        print(textPrint)
        f = open("OUTPUT_IPA.txt", "w", encoding='utf-8')
        f.write(textPrint)
        f.close()

###############newIPAout = gTESTfile.readlines()


file.close()
####newIPAout.close()

