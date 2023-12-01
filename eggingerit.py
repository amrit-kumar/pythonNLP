#nope
from gingerit.gingerit import GingerIt

address = "1234 main streeet, New Yrok, NY 10001, Unti 5B"

# Create a GingerIt object
parser = GingerIt()

# Correct the spelling mistakes in the address
corrected_text = parser.parse(address)['result']

# Print the original and corrected addresses
print("Original address: ", address)
print("Corrected address: ", corrected_text)
