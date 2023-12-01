import spacy

# Load a pre-trained NLP model with part-of-speech tagging and named entity recognition
nlp = spacy.load("en_core_web_sm")

# Define a function to expand abbreviations in an address string
def expand_abbreviations(address):
    # Parse the input address using the NLP model
    doc = nlp(address)
    # Define a dictionary of known abbreviations and their corresponding full words
    abbreviations = {
        "st": "street",
        "ave": "avenue",
        "blvd": "boulevard",
        "rd": "road",
        # Add any additional abbreviations and their full words here
    }
    # Iterate over each token in the parsed address
    for token in doc:
        # Check if the token is an abbreviation and if it is in the dictionary
        if token.text.lower() in abbreviations:
            # Replace the abbreviation with its corresponding full word
            address = address.replace(token.text.lower(), abbreviations[token.text.lower()])
    # Return the updated address string
    return address
# address = "123 main st,18th av, new york, ny"
address = "1234 main streeet, New Yrok, NY 10001, Unti 5B"

print(expand_abbreviations(address))