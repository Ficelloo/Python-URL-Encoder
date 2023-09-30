def encode_char_charset_ref(char):
    return f"%{ord(char):02X}"

input_string = input("String to encode in URL : ")
encoded_string = ''.join(encode_char_charset_ref(char) for char in input_string)

print("Output :")
print(encoded_string)
