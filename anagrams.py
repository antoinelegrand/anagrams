# anagrams

import re
import sys
import csv
import kagglehub

# Download latest version
path = kagglehub.dataset_download("kartmaan/dictionnaire-francais")

#print("Path to dataset files:", path)


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
 #   exp = cleanUp(expression)
 #   print(exp)
    for word in dictionary:
 #       print(word)
        if isAnagram(expression, word):
            print("%s est un anagramme de %s" % (word, expression))
            
def isAnagram(strA, strB):
    cleanA = cleanUp(strA.strip())
    cleanB = cleanUp(strB.strip())
    a = cleanA.upper()
    b = cleanB.upper()

#    print("%s: %s" % ('a', a))
#    print("%s: %s" % ('b', b))
    
    if len(a) != len(b):
        return False
        
    if len(a) == 0:
        return True
        
    c = a[0]
#    print("%s: %s" % ('c', c))
        
    if c in b: 
        aSplit = a.split(c, 1)
        bSplit = b.split(c, 1)
        return isAnagram(aSplit[1], bSplit[0]+bSplit[1])


# main
path2 = r"C:\Users\alegr\Documents\data\archive\dico.csv"

with open(path2, mode='r', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    with open('outputdic.csv', mode='w', encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
#        for rows in reader:
#            mydict = {cleanUp(rows[0]):cleanUp(rows[1])}
        pubDict = {rows[0] for rows in reader}

#testDictionary = {'albert', 'etienne', 'einstein', 'klein', 'claudine', 'legrand', 'antoine'}
#testWord = 'antoine'

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
            
    
    
    
        
    
    
            
        
        

