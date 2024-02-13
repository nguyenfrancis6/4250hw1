#-------------------------------------------------------------------------
# AUTHOR: Francis Nguyen
# FILENAME: indexing.py
# SPECIFICATION: Program reads a csv file and cleans it through stopword removal and stemming. Index terms are then created and the tf-idf values are derived from the stemmed documents.
# FOR: CS 4250- Assignment #1
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {'and', 'her', 'their', 'I', 'She', 'They'}
documents_without_stopwords = []
for document in documents:
    words = document.split()
    filtered_words = [word for word in words if word not in stopWords]
    documents_without_stopwords.append(' '.join(filtered_words))

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    's':''
}

def stem_word(word): 
  for ending, replacement in stemming.items(): 
    if word.endswith(ending):
      return word[:-len(ending)] + replacement
  return word

stemDocs = [] 
for document in documents_without_stopwords:
   words = document.split()
   stemWords =  [stem_word(word) for word in words]
   stemDocs.append(' '.join(stemWords))

#Identifying the index terms.
#--> add your Python code here
terms = list(set([word for document in stemDocs for word in document.split()]))

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

def tf(term, document): 
  return document.split().count(term) / len(document.split())

def idf(term, documents):
  termCount = 0 
  for document in documents: 
     if term in document:
        termCount += 1
  return (math.log(len(documents)/termCount, 10))

for document in stemDocs:
  tfidf = {}
  for term in terms: 
    tfidf[term] = tf(term, document) * idf(term, stemDocs)
  docTermMatrix.append(tfidf) 

# Printing the document-term matrix.
# --> add your Python code here
print("Document-Term Matrix:")
# Print the headers
header = "\t\t" + "\t".join(terms)
print(header)

# Print each document and its corresponding tf-idf values
for i, document in enumerate(documents):
  row_values = [f"{docTermMatrix[i].get(term, 0):.2f}" for term in terms]
  row = f"Document {i + 1}:\t" + "\t".join(row_values)
  print(row)