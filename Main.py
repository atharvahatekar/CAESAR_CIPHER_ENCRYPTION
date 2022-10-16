from Logo import logo

print(logo)

alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm',              #this is twi times to eliminate the error "list indes out of range"
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]


def caesar(start_text, shift_amount, cipher_direction):
    
    end_text= ""

    for letter in start_text:
        position = alphabets.index(letter)

        if cipher_direction == 'encode':
            new_position = position + shift_amount
        elif cipher_direction == 'decode':
            new_position = position - shift_amount
        
        new_letter = alphabets[new_position]
        end_text += new_letter

    print(f"the {cipher_direction} text is {end_text}")



should_continue = True

while should_continue:
    direction = input("type 'encode' to encrypt or type 'decode' to Decrypt:\n")
    text = input("type your message: \n").lower()
    shift = int(input("Type the Shift Number: \n"))
    shift= shift % 26                                             #reuse alphabets after 'z'
    
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

    result= input("Type 'yes' if you want to go again , otherwise type 'no'. \n")
    if result == 'no' :
        should_continue = False
        print("goodbye")

#--------------------Combined encode and Decode Function into One Function above-------------------------


# def encrypt(plain_text,shift_amount):               # Indix func is used to find out the index of letter in alphabet list
#     cipher_text = ""
#     for letter in plain_text:                              #For ex, plain_text = "hello"
#         position = alphabets.index(letter)                  #shift = 5
#         new_position = position + shift_amount              #cipher Text = "mjqqt"
#         new_letter = alphabets[new_position]                
#         cipher_text += new_letter
#     print(f"the encoded text is {cipher_text}")   


# encrypt(plain_text=text,shift_amount=shift)


# def decrypt(cipher_text,shift_amount):
#     decrypt_text=" "
#     for letter in cipher_text:
#         position = alphabets.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabets[new_position]
#         decrypt_text += new_letter
#     print(f"The Decoded Text is {decrypt_text}")

# decrypt(cipher_text=text,shift_amount=shift)

# if direction=='encode':
#     encrypt(plain_text=text,shift_amount=shift)

# if direction=="decode":
#     decrypt(cipher_text=text,shift_amount=shift)
