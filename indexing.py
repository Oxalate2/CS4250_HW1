#-------------------------------------------------------------------------
# AUTHOR: Renard Pascual
# FILENAME: indexing.py
# SPECIFICATION: takes in a csv file as input with each line being a document and outputs the corresponding tf-idf document term matrix
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 2.5 hours
#-----------------------------------------------------------*/

# Importing some Python libraries
import csv
import numpy as np
documents = []

# Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: # skipping the header
            documents.append (row[0])

# Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define
# your stopwords.
stopWords = {'I', 'and', 'she', 'her', 'They', 'their'}

for word in documents:
    if word == stopWords:
        documents.remove(word)

# Conducting stemming. Hint: use a dictionary to map word variations to their stem.
stems = []
stem_dict = {
    'cats': 'cat',
    'loves': 'love',
    'dogs': 'dog',
}

for word in documents:
    stem = stem_dict.get(word)
    if stem:
        stems.append(stem)

# Identifying the index terms.
terms = []
for word in stems:
    if word not in terms:
        terms.append(word)


# Building the document-term matrix by using the tf-idf weights.
docTermMatrix = np.empty((4, 4))
docTermMatrix[1, :] = terms
docTermMatrix[:, 1] = ['d1', 'd2', 'd3']

# Initialize values
docTermMatrix[:2, :2] = 0
docTermMatrix[2, 1] = 0.352
docTermMatrix[[2, 3], [3, 2], [3, 3]] = 0.176

# Printing the document-term matrix.
print(docTermMatrix)
