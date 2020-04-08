#Importing packages
from spellchecker import SpellChecker

#Making a checker class
class SpellerChecker:

    #method ot correct typos
    def correctTypos(text):
        speller=SpellChecker()
        words=speller.split_words(str(text))
        result=""
        corrected = []
        for word in words:
            corrected.append(speller.correction(word))
        for word in corrected:
            if result=="":
               result=word
            else:
                result=result+" "+word
            
        return result
    
    #method to check typos without correcting
    def check(text):
        i=0
        speller=SpellChecker()
        words=speller.split_words(str(text))
        result="Typo:------"
        corrected = []
        for word in words:
            corrected.append(speller.correction(word))
        while(i<len(words)):
            if(words[i]==corrected[i]):
                i+=1
            elif(words[i]!=corrected[i]):
                result="Typo: "+words[i]
                break 
        return result
        
        
        


