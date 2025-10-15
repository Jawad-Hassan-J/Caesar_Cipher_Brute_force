# import dictionary to check word exist or not
from wordfreq import zipf_frequency

# All letters A-Z
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#simple test
S =""
user_input=input("enter any CaesarCipher message to decrypt, press 'Enter' to see default ")

if (S == ""):
    S = """AOPZ SHI AHRLZ BZ PUAV HU VIZLYCHAPVU AOHA PZ RUVDU HZ ZBMMPJPLUA RLF ZWHJL
    WYPUJPWSL AOHA ZAHALZ HUF ZLJBYL LUJYFWAPVU ZJOLTL TBZA OHCL H RLF ZWHJL AOHA PZ
    ZBMMPJPLUA SHYNL AV THRL HU LEOHBZAPCL ZLHYJO HAAHJR PUMLHZPISL"""
else:
    S = user_input





# This function take array of array have words as a value [['word1','word2']['word1','word2']], and check if this word is in the dictionary or not if its there we count +! then take the max score so its have the most meaning words is the original
def is_word(array_of_words):

    # result is empty dictionary of size the original array
    result = [{} for _ in range(len(array_of_words))]

    # Loop with first inside array [[]] to end
    for row_index, words in enumerate(array_of_words):

        # Start count form zero
        count = 0

        # This nested loop search for the words in the dictionary or not
        for index, word in enumerate(words):

            # zipf_frequency(word.lower(),'en')
            # is a function in wordfreq that take the word with laguage then return how many this word is reputed  
            freq = zipf_frequency(word.lower(),'en')

            # first we make variable called result of size the array of array, now we arsine in this object index to label the row and the words it self.
            # "".join() take list string and separated by "" in this case
            result[row_index]["row_index"]= row_index
            result[row_index]["Words"] =" ".join(array_of_words[row_index])

            # if freq more than 1 this mean this word in dictionary so its has meaning 
            # we save in result index[row_index] label["score"] to next can easy find the max
            if(freq > 0):
                count= count+1
        result[row_index]["score"] = count
                

    return result


# in this function we send the result form is_word function to find the maximum
def max_in_array_of_dictionary(array_of_dictionary):

    # in classical max/min we start from any index in array but usually start with first index
    max_index = 0
    max_score = array_of_dictionary[0]["score"]

    # in this loop we search index by index in label "score" to find max score "Traditional search function"
    # then return the dictionary with max index
    for i in range(len(array_of_dictionary)):
        if array_of_dictionary[i]["score"] > max_score:
            max_score = array_of_dictionary[i]["score"]
            max_index = i

    return array_of_dictionary[max_index]


# this is the hart of code how to shift
def Shift(letters,S):

    # we create empty array of size from 0...25, size 26, because we need to compute all combination with shift one index in letters, an example first 0:A 1:B 2:C ... to end, then A:1 B:2 C:3 ... to end, the idea each character will shift one index to hes adjacent . 
    # we have normal loop from 0 to 25 each time we shift depend on the key.
    all_split_result = []
    for key in range(26):
        
        new_Array =[]
        result = ""
        
        # Create empty array location to add this value later
        for i in range(len(letters)):
            new_Array.append(None)

        # the logic here is complex liter bit, in example we have litters A,B,C and empty array ["None","None","None"] with key=0 this mean first Character will append to index key=0, and stop in len(letters) which is equal to 25, in this case the letter is 3 ["A","B","C"]
        # but what the key is 1? this mean we start A in index 1, ["None","None","None"] become ["None","A","B"], the remaining element is second loop responsibility.
        for i in range((len(letters)-key)):
            new_Array[i+key]=letters[i]

        # Now we have letter ABC, key= 1, and from previous loop the new_Array is = ["None","A","B"], we need to attach the reminding element in begging of the array, in this case we must append C in index 1
        # The loop start from 0 to key in this case is 1 and letter is 3, so new_Array[i]= letters[3-1+0]= 2 when we back to the letters the original is 0:A, 1:B, 2:C, in this case we add the C in begging of the array
        for i in range(key):
            new_Array[i] = letters[len(letters) - key + i]

        # in each character in String
        for char in S:
            # if char is in letters
            if char in letters:
                """ we assign index by the new shift new_array is 
                new_shifted_array_position 
                ["A","B","C"] shift key=1 ["None","None","None"] then ["None,"A","B"] finally ["C","A","B"]
                index = new_Array.index(char) 
                append all this to result 
                """
                index = new_Array.index(char) 
                result += letters[index]

            else:
                # else is space so just add space
                result += char
    
        # we split the result for this iteration as array of words, we use split because the function is_word accept array of array
        split_result=result.split()
        # we append all combination of array
        all_split_result.append(split_result)
        
    
        print()

       
    return all_split_result



""" 
the order is
1. shift: compute all companion, return array of array have all companion shift A one index
2. is_word: accept array of array and add some label such scoring to calculate real word, row_index and others.
3. max_in_array_of_dictionary: accept array of dictionary and find the max score, return the max score object.
"""

# for requirement i must print all companion
First_call = Shift(letters,S)
for index, row in enumerate(First_call):
    print(index,row,'\n')



Second_call = is_word(First_call)
Third_call = max_in_array_of_dictionary(Second_call)

print()
print("key:",Third_call['row_index'], "is the real message")
print(Third_call)

