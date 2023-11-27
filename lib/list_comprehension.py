#!/usr/bin/env python3

# Function to return a list of even elements from a sequence of integers
def return_evens(sequence):
    return [num for num in sequence if num % 2 == 0]

# Function to add exclamation marks at the end of each sentence in a list of strings
def make_exclamation(sentences):
    return [sentence + '!' if not sentence.endswith(('!', '.', '?')) else sentence for sentence in sentences]

# Example usage
evens = return_evens([0, 1, 3, 5, 7, 8, 9])
print(evens)  # Output: [0, 8]

exclamations = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(exclamations) 