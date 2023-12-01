# PyEnchant: This library provides spellchecking
# functionality and supports multiple languages. It is easy to use and can be integrated with various Python applications.
import enchant

wordDict = enchant.Dict("en_US")

inputWords = ['wtr','bwlingbl','bsktball','btl','st']
for word in inputWords:
    print (wordDict.suggest(word))

def correct_address_spelling(address):
    words = address.split()
    correct_words = []
    for word in words:
        if enchant.Dict("en_US").check(word):
            correct_words.append(word)
        else:
            suggestions = enchant.Dict("en_US").suggest(word)
            if suggestions:
                correct_words.append(suggestions[0])
            else:
                correct_words.append(word)
    return " ".join(correct_words)

# address = "1234 main stret, New York, NY 10001"
address = "1234 main streeet, New Yrok, NY 10001, Unti 5B"
corrected_address = correct_address_spelling(address)
print(corrected_address)