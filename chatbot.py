import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow
import random
import json

stemmer = LancasterStemmer()

with open('dataset.json') as file:
	data = json.load(file)

words = []
labels = []
docs_y = []
docs_x = []

for disease_symptom in data['DiseaseSymptom']:
    for symptom in disease_symptom['Symptoms']:
        wrds = nltk.word_tokenize(symptom)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(disease_symptom["Disease"])
        
    if disease_symptom['Disease'] not in labels:
        labels.append(disease_symptom['Disease'])

print(labels)