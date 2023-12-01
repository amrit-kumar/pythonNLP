import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define the training data
training_data = pd.DataFrame({
    'abbreviation': ['CSE', 'ECE', 'IT', 'EEE', 'MECH'],
    'word': ['Computer Science Engineering', 'Electronics and Communication Engineering', 'Information Technology', 'Electrical and Electronics Engineering', 'Mechanical Engineering']
})

# Define the testing data
testing_data = ['CSE', 'ECE', 'IT', 'EEE', 'MECH']

# Create the feature vectors
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 3))
X_train = vectorizer.fit_transform(training_data['abbreviation'])
X_test = vectorizer.transform(testing_data)

# Create the labels
y_train = training_data['word']

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Print the results
for i in range(len(testing_data)):
    print(testing_data[i] + ': ' + predictions[i])
