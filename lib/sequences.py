#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length < 0:
        print("Length must be a positive integer.")
        return
    
    sequence = [0, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    print(sequence[:length])