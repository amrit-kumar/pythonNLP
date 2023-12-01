import kenlm

model_path = 'path/to/language/model'  # Path to the language model file
lm_model = kenlm.LanguageModel(model_path)

address = "1234 main streeet, New Yrok, NY 10001, Unti 5B"

# Split the address into words
words = address.split()

# Correct the spelling mistakes in the address
corrected_words = []
for word in words:
    # Use the language model to correct the word
    corrected_word = lm_model.correct(word)

    # Append the corrected word to the list
    corrected_words.append(corrected_word)

# Join the corrected words back into a string to obtain the corrected address
corrected_address = ' '.join(corrected_words)

# Print the original and corrected addresses
print("Original address: ", address)
print("Corrected address: ", corrected_address)
