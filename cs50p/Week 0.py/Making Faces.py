"""
In a file called faces.py, implement a function called convert that accepts a str as input and returns 
that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( 
converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.
"""

def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon

def main():
    symbol_enter = input("Enter anything with an emoticon: ")
    print(convert(symbol_enter))

main()