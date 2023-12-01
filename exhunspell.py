import hunspell

address = "1234 main streeet, New Yrok, NY 10001, Unti 5B"

# Create a Hunspell object
hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')

# Correct the spelling mistakes in the address
corrected_address = ''
for word in address.split():
    if not hobj.spell(word):
        suggestions = hobj.suggest(word)
        if len(suggestions) > 0:
            corrected_word = suggestions[0]
        else:
            corrected_word = word
    else:
        corrected_word = word
    corrected_address += corrected_word + ' '

# Print the original and corrected addresses
print("Original address: ", address)
print("Corrected address: ", corrected_address.strip())
