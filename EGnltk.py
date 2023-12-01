import nltk
from nltk.corpus import gutenberg
from nltk.probability import LidstoneProbDist
from textblob import TextBlob

# Load and preprocess text data
corpus = gutenberg.raw('shakespeare-hamlet.txt')
sentences = nltk.sent_tokenize(corpus)
tokens = [nltk.word_tokenize(s) for s in sentences]

# Correct spelling mistakes using TextBlob
corrected_tokens = []
for sentence in tokens:
    corrected = ''
    for word in sentence:
        corrected_word = TextBlob(word).correct()
        corrected += str(corrected_word) + ' '
    corrected_tokens.append(corrected.strip())

# Split data into training and testing sets
split_ratio = 0.8
split_idx = int(len(corrected_tokens) * split_ratio)
train_data = corrected_tokens[:split_idx]
test_data = corrected_tokens[split_idx:]

# Build bigram language model with Lidstone smoothing
vocab = set([word for sentence in train_data for word in sentence.split()])
freq_dist = nltk.FreqDist([word for sentence in train_data for word in sentence.split()])
prob_dist = LidstoneProbDist(freq_dist, 0.1, bins=len(vocab))
bigram_model = nltk.lm.models.NgramModel(2, train_data, estimator=lambda fdist, bins: prob_dist)

print("hii")
# Evaluate the language model
perplexity = bigram_model.perplexity(test_data)
print('Perplexity:', perplexity)

# Use the language model to generate text
generated_text = bigram_model.generate(50, random_seed=42)
print('Generated text:', ' '.join(generated_text))
