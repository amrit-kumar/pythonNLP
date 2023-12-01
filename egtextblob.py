from textblob import TextBlob

address = "1234 main streeet, New Yrok, NY 10001, Unti 5B"

# Split the address into words
words = address.split()

# Correct the spelling mistakes in the address
corrected_words = []
for word in words:
    # Get the TextBlob object for the word
    blob = TextBlob(word)

    # Check if the word is misspelled
    if blob.correct() != word:
        # Get the corrected word
        corrected_word = blob.correct().string
    else:
        corrected_word = word

    # Append the corrected word to the list
    corrected_words.append(corrected_word)

# Join the corrected words back into a string to obtain the corrected address
corrected_address = ' '.join(corrected_words)

# Print the original and corrected addresses
print("Original address: ", address)
print("Corrected address: ", corrected_address)
