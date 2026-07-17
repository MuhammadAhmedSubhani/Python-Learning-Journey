"""
In a file called playback.py, implement a program in Python that prompts the user for input and then outputs
that same input, replacing each space with ... (i.e., three periods).
"""

prompt = input("Enter a sentence: ").replace(" ", "...").upper()

print(prompt)