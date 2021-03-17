# -*- coding: utf-8 -*-
"""
Word analysis project
Created on Thu Aug 27 13:32:21 2020
@author: Mikhail Terentev

"""

import PyPDF2
import re
from pattern.text.en import singularize
from collections import Counter

class WordAnalysis:
      
    # This method should construct all the internal attributes of the class.
    def __init__(self, sampleFile):  
        self.sampleFile = sampleFile

    
    # It prints out all the words in the dictionary. 
    # It should print out the words and frequency 4 pairs in a row.
    def __str__(self):
        
        # Count the frequency of the words, and save them in a dictionary (internal attribute)
        def WordCount(fname):
            with open(fname) as f:
                return Counter(f.read().split())
        
        k = WordCount('sampleStrip.txt') 
        dictToList = list(k.items())            # convert dictionary to list
        
        writefile=open('outputFile.txt', 'a', encoding='utf-8', errors='replace')
        
        for grp in range(0, len(dictToList), 4):
            # For debug:
            # print(''.join("{:<20}".format(elm[0]) + "{:<4}".format(elm[1]) for elm in dictToList[grp:grp+4]))
            tup = ("{:<20}".format(elm[0]) + "{:<4}".format(elm[1]) for elm in dictToList[grp:grp+4])
            line = ''.join(tup)
            writefile.write(line + '\n')
        
        return "Done"
    
    
    def ExtractWords(self, text):

        for line in text:
            line = re.sub(r'[^a-zA-Z]', ' ', line) + " "        # strip off non-ABC symbols
            line = re.sub(r'\b\w\b', ' ', line) + " "           # strip off single letter words
            # Convert the plurals to singular words:
            plurals = [line.strip()]                            # convert string to list
            singles = [singularize(plural) for plural in plurals]
            
            line = ' '.join(singles) + " "                      # convert list to string
            line = line.lower()                                 # Convert the capitalized words to lowercase words      
            
            writefile.write(line)                               # print to file
            
   
    def AddRemovedWords(self, word):
        
        # Count the frequency of the words, and save them in a dictionary (internal attribute)
        def WordCount(fname):
            with open(fname) as f:
                return Counter(f.read().split())
        
        r = WordCount('sampleStrip.txt')        
        del r[word]
        return r
        
        
    def DelRemovedWords(self, word):
        
        # Count the frequency of the words, and save them in a dictionary (internal attribute)
        def WordCount(fname):
            with open(fname) as f:
                return Counter(f.read().split())
        
        r = WordCount('sampleStrip.txt')
        r.update(word)
        return r
      
        
    # --- Show words with frequency ---   
    def Show(self, freq):
        
        # Count the frequency of the words, and save them in a dictionary (internal attribute)
        def WordCount(fname):
            with open(fname) as f:
                return Counter(f.read().split())
        
        r = WordCount('sampleStrip.txt')
        r = {k: v for k, v in r.items() if v >= freq}
        writefile=open('outputFile.txt', 'w', encoding='utf-8', errors='replace')
        
      #  -- print
        for v in r.items():
            name, val = v
            # For debug:
            print("word -- ", "{:^15}".format(name), "-- frequency: ", "{:<3}".format(val))
            
            tup = ("word -- ", "{:^15}".format(name), "-- frequency: ", "{:<3}".format(val))
            line = ''.join(tup)
            writefile.write(line + '\n')

    

# For debug
# print("Number of words in the file :", WordCount('sampleStrip.txt'))

WordAnalysis = WordAnalysis('sample.txt')
# pdf reader object    
with open('SampleCh7.pdf','rb') as pdf_file, open('sample.txt', 'w', encoding='utf-8', errors=' ') as text_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    # analys 4 pages. max pages is pages calculated above
    #number_of_pages = read_pdf.getNumPages()     # number of pages in pdf (all pages)
    number_of_pages = 4
    for page_number in range(number_of_pages):   
        page = read_pdf.getPage(page_number)
        page_content = page.extractText()
        text_file.write(page_content)
openfile=open('sample.txt','r', encoding='utf-8')    
writefile=open('sampleStrip.txt', 'w', encoding='utf-8', errors='replace')
writefile.close()

# extracting the words into database
writefile=open('sampleStrip.txt', 'w', encoding='utf-8', errors='replace')
WordAnalysis.ExtractWords(openfile)
writefile.close()

WordAnalysis.AddRemovedWords("and")
WordAnalysis.AddRemovedWords("a")
WordAnalysis.AddRemovedWords("the")

WordAnalysis.DelRemovedWords("the")

# show words with frequency > 10
WordAnalysis.Show(10)
#print out all the words in the dictionary
print (str(WordAnalysis))


#print("New dict after removed word: ", AddRemovedWords(input("Add removed word: ")))
#print("New dict after removed word from filter: ", DelRemovedWords(input("Delete removed word: ")))
#print(Show(int(input("Enter specified frequency: "))))       

# close the files:
writefile.close()  
openfile.close() 
        
    

        
    