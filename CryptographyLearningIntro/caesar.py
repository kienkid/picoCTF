#use this python script to run through all the combination of Caesar Cipher (25 possible key)
def caesar_cipher(text, shift):
    result = ''
    for i in range(0, len(text)):
        a = text[i]
        if a in [' ', '\'', '!', '"']:
            result += a
        else:
            new = ord(str(a)) + shift
            if new > 90:
                new = chr(new - 26)
            elif new < 65:
                new = chr(new + 26)
            else:
                new = chr(new)
            result += new
    return result


def main():
    message = str.upper(input("Your message? "))
    #key = int(input("Encoding key? "))
    for i in range(0, 26):
            print(caesar_cipher(message, i).lower())

main()
