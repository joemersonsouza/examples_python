import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random
import os.path
from os import path

def loadIntents(words, documents, classes):
    data_file = open('intents.json').read()
    intents = json.loads(data_file)

    for intent in intents['intents']:
        for pattern in intent['patterns']:

            # take each word and tokenize it
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            # adding documents
            documents.append((w, intent['tag']))

            # adding classes to our class list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

def trainningData(words, documents, classes, model):
    # initializing training data
    training = []
    output_empty = [0] * len(classes)
    for doc in documents:
        # initializing bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # lemmatize each word - create base word, in attempt to represent related words
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
        # create our bag of words array with 1, if word match found in current pattern
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)

        # output is a '0' for each tag and '1' for current tag (for each pattern)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1

        training.append([bag, output_row])
    # shuffle our features and turn into np.array
    random.shuffle(training)
    training = np.array(training)

    # create train and test lists. X - patterns, Y - intents
    train_x = list(training[:,0])
    train_y = list(training[:,1])

    # Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
    # equal to number of intents to predict output intent with softmax
    model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    # Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    #fitting and saving the model
    return model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

def clean():
    if(path.exists('words.pkl')):
            os.remove('words.pkl')
    if(path.exists('classes.pkl')):
        os.remove('classes.pkl')
    if(path.exists('chatbot_model.h5')):
        os.remove('chatbot_model.h5')

def init():

    words=[]
    classes = []
    documents = []
    ignore_words = ['?', '!']

    loadIntents(words, documents, classes)

    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))

    classes = sorted(list(set(classes)))

    pickle.dump(words,open('words.pkl','wb'))
    pickle.dump(classes,open('classes.pkl','wb'))

    model = Sequential()
    hist = trainningData(words, documents, classes, model)
    model.save('chatbot_model.h5', hist)

if __name__ == "__main__":
    clean()
    init()