#!/usr/bin/env python
# coding: utf-8

# In[2]:


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
  
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ':  
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:  
            cipher += ' '
    return cipher 
  
def decrypt(message1): 
    message1 += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message1: 

        if (letter != ' '): 
            i = 0

            citext += letter 
  
        else:  
            i += 1
  
            if i == 2 : 
  
                 
                decipher += ' '
            else: 
  
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
  
    return decipher


# In[4]:


def main(): 
    opt = int(input("Enter your mode of translation : \n 1. Normal text to Morse Code \n 2. Morse Code to Normal text"))    
    if opt==1:   
        while True:
            message = input("Enter any message ")
            if message.lower() == "end":
                print("connection is closed")
                break
            else:
                result = encrypt(message.upper()) 
                print (result)

    elif opt==2:          
        while True:
            message = input("Enter message in morse code ")
            try:
                result = decrypt(message) 
            except ValueError:
                print("Sorry desired morse code isn't defined in dictionary ")
                break
            print (result)
    else:
        print("Please select a valid option ")


if __name__ == '__main__': 
    main() 


# In[2]:


MORSE_CODE_DICT


# In[3]:


from random import shuffle


# In[4]:


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 


# In[5]:


a=MORSE_CODE_DICT.values()


# In[22]:


a


# In[6]:


a=list(a)


# In[25]:


a


# In[5]:


import random


# In[31]:


random.shuffle(a)


# In[32]:


a


# In[7]:


b=MORSE_CODE_DICT.keys()


# In[8]:


b


# In[9]:


b=list(b)


# In[36]:


b


# In[10]:


MORSE_CODE_DICT1 = dict(zip(b,a))


# In[12]:


MORSE_CODE_DICT1


# In[ ]:




