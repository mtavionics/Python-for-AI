# Python-for-AI
Study projects

Word analysis project

The project will use some modules which have not been covered in the class. Please google and try them out. Here is the requirement:

1). Read the PDF file, SampleCh7.pdf, which is also in the folder, and extract all the text from the pdf file. You will need to use the PyPDF2 module. The PyPDF2 module is not in the Anaconda’s default installation, and you need to use the following command to install the module:

conda install -c conda-forge pypdf2
(execute the command in the Anaconda command window)

Or you can install in the google colab environment:
!pip install PyPDF2

2). Build a WordAnalysis Class to do the analysis work. The class should include the following methods (please define the attribute yourself):

class WordAnalysis:
	def __init__(self):
	def __str__(self):
	def AddRemovedWords(self, word):
	def DelRemovedWords(self, word):
	def ExtractWords(self, text):
	def Show(self, freq):
	
For ExtractWords(self, text):
It should:
	1). Strip off all punctuations, numbers, and symbols, only words are kept, and try to remove non-words as much as you can, for example, single letter words.
	2). Convert the plurals to singular words, and convert the capitalized words to lowercase words. You can use the pattern module to convert the plurals to singular words. Again, you need to install the pattern module as follows:

conda install -c conda-forge pattern
pip install Pattern
	
3). Count the frequency of the words, and save them in a dictionary (internal attribute).

For AddRemovedWords(self, word),
it  will add a word to be filtered out, so that the dictionary will not save the frequency of the world, for example, ‘the’.


For DelRemovedWords(self, word):
It can remove a word from the filter list, and add the word back to the dictionary for frequency count.

For Show(self, freq):
It will show the words with frequency higher than specified frequency, freq, and show them in descending order.

in  __str__(self):
It prints out all the words in the dictionary. It should print out the words and frequency 4 pairs in a row.

In  __init__(self)
It should construct all the internal attributes of the class.

Here are the sample testing code:

# you can find find the pdf file with complete code in below
pdfFileObj = open('Samplech7.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
pages=pdfReader.numPages
#remove the words that are not meaningful. You can add back any word. Please test yourself.
wordAnalysis = WordAnalysis()
wordAnalysis.AddRemovedWords("and")
wordAnalysis.AddRemovedWords("a") 'sampleStrip.txt'
wordAnalysis.AddRemovedWords("the")
# analys 4 pages. max pages is pages calculated above
for i in range(4):
    pageObj = pdfReader.getPage(i)
    # extracting the words from page.into database
    wordAnalysis.ExtractWords(pageObj.extractText())
# show words with frequency > 10
wordAnalysis.Show(10)
#print out all the words in the dictionary
print (wordAnalysis)
#close the file.
pdfFileObj.close() 

The Output should as follows (the output should align nicely as shown in the output file, project-output.txt, also in the folder): 
word --     number      -- frequency: 31 
word --        is        -- frequency: 25 
word --       to        -- frequency: 24 
word --      phone      -- frequency: 24 
word --       you       -- frequency: 22 
word --       in        -- frequency: 22 
word --     regular     -- frequency: 19 
word --   expression    -- frequency: 19 
word --      text       -- frequency: 19 
word --       of        -- frequency: 19 
word --       for       -- frequency: 18 
word --     pattern     -- frequency: 17 
word --  isphonenumber  -- frequency: 15 
word --       if        -- frequency: 14 
word --     string      -- frequency: 13 
word --      that       -- frequency: 12 
word --      chunk      -- frequency: 12 
word --      with       -- frequency: 11 
word --     return      -- frequency: 11

pattern        17 matching       3  with           11 regular        19 
expression     19 you            22 may            2  be             6  
familiar       1  searching      1  for            18 text           19 
by             4  pressing       1  ctrl           1  entering       1  
word           4  re             4  looking        1  go             2  
one            2  step           3  further        1  they           1  
