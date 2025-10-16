#  CaesarCipher brute-force
### This is part of university of Bahrain Assignment in ITNE341 Network security with Dr. Ebrahim Abdulrahman Janahi


### In this app we can encrypted any CaesarCipher code by trying all shifting combination, the special thing in this code is the logic of choices the real key automatically by scoring method to know which one is the real message, the most one have meaningful words its the right one.

### Project Summary 

This script automatically **decrypts Caesar cipher messages**.
It tries **all 26 alphabet shifts**, checks which version contains the most **real English words** using the `wordfreq` library, and then **selects the most likely original text**.

**Main steps:**

1. **Shift()** → Generates 26 shifted versions of the message.
2. **is_word()** → Checks each version for real English words and gives it a score.
3. **max_in_array_of_dictionary()** → Finds the version with the highest score (the most meaningful result).

Finally, the program prints the **best shift key** and the **decoded message**.


### Requirements
```bash
$ pip install wordfreq


