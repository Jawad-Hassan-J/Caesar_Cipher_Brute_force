# BY Ali

# We designed this code to decrypt Caesar cipher message by testing all 25 possible shifts (Brute Force).

# We used this formula #𝐶 = 𝐸 (𝐾, 𝑝) = 𝑝 + 𝐾 mod 26, ord (). chr () a built in method in python to change letters to ASCII number and vice versa, However, all of this was in for loop in range of 1 to 26 and we use append method to add the letter to the new text (plaintext), In addition,  we used join to convert the list into a string.

# To sum up, the code decrypts a Caesar cipher using brute-force to find the original message.



letter= "AOPZ SHI AHRLZ BZ PUAV HU VIZLYCHAPVU AOHA PZ RUVDU HZ ZBMMPJPLUA RLF ZWHJL WYPUJPWSL AOHA ZAHALZ HUF ZLJBYL LUJYFWAPVU ZJOLTL TBZA OHCL H RLF ZWHJL AOHA PZ ZBMMPJPLUA SHYNL AV THRL HU LEOHBZAPCL ZLHYJO HAAHJR PUMLHZPISL"

#letter=input("Enter the cipher text: ")

#𝐶 = 𝐸(𝐾,𝑝) = 𝑝 + 𝐾 mod 26

#str=["A","B","C","D",'E','F','G','H','I','J','K',"L","M","N","O",'P','Q','R','S','T','U','V','W',"X","Y","Z"] from 65 to 90

#ord change letter to ascii number

#chr change number to ascii letter

for shift in range(1,26): #enter the loop from 1 to 26

 plaintext=[]

 for i in letter.upper(): # enter the loop for the letter or the ciphertext and to make sure that all small letter converted to upper case letter

 if 'A' <= i <= 'Z': #the range for the letters from A to Z

  num = ((ord(i) - 65 - shift) % 26 )# this is the formula change the letter from the cipher to a number -65 - shift 

  plaintext.append(chr(num + 65))

 else:

  plaintext.append(" ") # put a spcae if the is no letter

 print ("shift",shift, ":",''.join(plaintext)) #use join to make the list as sentence

 print() # new line|