# anagrams

import re
import sys
import csv
import kagglehub

# Download latest version of dic
path = kagglehub.dataset_download("kartmaan/dictionnaire-francais")


def cleanUp(expression):
    try:
        cleanExp = re.sub(r"[ \/\?\!\>\:\;\'\"\`\&\.\,]+", '', expression)
        cleanExp = re.sub(r"[éèêëÉÈÊ]", 'e', cleanExp)
        cleanExp = re.sub(r"[àâãäÀ]", 'a', cleanExp)
        cleanExp = re.sub(r"[ïî]", 'i', cleanExp)
        cleanExp = re.sub(r"[öô]", 'o', cleanExp)
        cleanExp = re.sub(r"[ùûü]", 'u', cleanExp)
        cleanExp = re.sub(r"[çÇ]", 'c', cleanExp)
    except:
        cleanExp = ""
    return cleanExp


def listAnagrams(expression, dictionary):
    for word in dictionary:
        if isAnagram(expression, word):
            print("%s: anagram of %s" % (word, expression))
            
def isAnagram(strA, strB):
    cleanA = cleanUp(strA.strip())
    cleanB = cleanUp(strB.strip())
    a = cleanA.upper()
    b = cleanB.upper()
    
    if len(a) != len(b):
        return False
        
    if len(a) == 0:
        return True
        
    c = a[0]
        
    if c in b: 
        aSplit = a.split(c, 1)
        bSplit = b.split(c, 1)
        return isAnagram(aSplit[1], bSplit[0]+bSplit[1])


# main
with open(path, mode='r', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    with open('outputdic.csv', mode='w', encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        pubDict = {rows[0] for rows in reader}

inputs = sys.argv[1:] 

if len(inputs) == 1:
    targetWord = inputs[0] 
    listAnagrams(targetWord, pubDict)
elif len(inputs) == 2: 
    inputExp = inputs[0] + " " + inputs[1]
    targetExp = inputs[0] + inputs[1]
    targetLen = len(targetExp)
    for word1 in pubDict:
        if len(word1) < targetLen:
            for word2 in pubDict:
                if len(word2) == targetLen - len(word1):
                    if isAnagram(targetExp, word1+word2):
                        print("%s %s : %s" % (word1, word2, inputExp))
            