alphabet = [i for i in "abcdefghijklmnopqrstuvwxyz"]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
text = input("Type your message\n").lower()
shift = int(input("Type the shift number\n"))

def ceaser(text, shift, direction):
    output_string = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        pos = alphabet.index(letter)
        new_pos = (pos + shift) % 26
        output_string += alphabet[new_pos]
    return output_string
print(ceaser(text,shift,direction))


