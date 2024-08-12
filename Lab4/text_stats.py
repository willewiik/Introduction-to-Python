#!/usr/bin/env python3
import sys
import numpy as np
import string


def clean_text_to_words(text):
  
    # Create translation table to remove punctuation and digits
    translator = str.maketrans('', '', string.punctuation.replace('-', '') + string.digits)
    
    # Remove punctuation and digits
    text_cleaned = text.translate(translator)  
    
    # Split text into words and convert to lowercase
    words = text_cleaned.lower().split()
    
    # Return words as tuple
    return tuple(words)


def get_following_words(all_words, word):
  
        following_words = []
        # "len(all_words) - 1" so we do not go out of bounds when running all_words[i + 1]
        for i in range(len(all_words) - 1):
            if all_words[i] == word:
                # If word is found in all_words then append the next word in to the list
                following_words.append(all_words[i + 1]) 
        
        
        unique_following_words, following_word_counts = np.unique(following_words, return_counts=True)
        
       
        return unique_following_words, following_word_counts    


def print_stats_from_text(input_filename, output_filename = None):
    # Check if the file exists
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("The file does not exist!")
        return

    if output_filename:
        # Redirect the standard output to the output file
        sys.stdout = open(output_filename, 'w')

    # Frequency table for alphabetic letters ===================================

    # Filter out non-alphabetic characters and convert to lowercase
    letters = ''.join(filter(str.isalpha, content.lower()))
    unique_letters, letter_counts = np.unique(list(letters), return_counts = True)

    # Sort in descending order of frequency
    letter_freq_sorted_indices = np.argsort(-letter_counts)

    print("Frequency table for alphabetic letters:")
    for idx in letter_freq_sorted_indices:
        print(f"{unique_letters[idx]}: {letter_counts[idx]}")


    # Number of words ==========================================================

    # A word is a sequence of characters from a text after removing
    # punctuation marks and digits. It consists of alphabetic characters only
    # and is converted to lowercase. Each word is separated from the next by whitespace.
    words = clean_text_to_words(content)
    num_words = len(words)

    print(f"Number of words: {num_words}")


    # Number of unique words ===================================================
  
    unique_words = np.unique(words)
    num_unique_words = len(unique_words)
    print(f"Number of unique words: {num_unique_words}")


    # Five most common word ====================================================
    unique_words, word_counts = np.unique(words, return_counts=True)

    # Sort in descending order of frequency
    word_freq_sorted_indices = np.argsort(-word_counts)

    top_five_words = unique_words[word_freq_sorted_indices[:5]]
    print("Five most commonly used words and their followers:")

    for word_idx in word_freq_sorted_indices[:5]:
        print(f"{unique_words[word_idx]} ({word_counts[word_idx]} occurrences)")

        # Get following words of the top 5 words and count
        unique_following_words, following_word_counts = get_following_words(all_words=words, word=unique_words[word_idx])

        # Sort in descending order of frequency
        following_freq_sorted_indices = np.argsort(-following_word_counts)

        for following_word_idx in following_freq_sorted_indices[:3]:
            print(f"-- {unique_following_words[following_word_idx]}, {following_word_counts[following_word_idx]}")

    if output_filename:
        sys.stdout.close()   # Close the output file and restore the standard output
        sys.stdout = sys.__stdout__  # Restore stdout

    


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 2:
        print("Error: No input_filename argument was found")
        sys.exit(1)
        
    if len(sys.argv) > 3:
        print("Error: Too many arguments")
        sys.exit(1)
    
    if len(sys.argv) == 3:
        print(f"Printing output to file: {sys.argv[2]}")
    
    
    input_filename  = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) == 3 else None
    
    print_stats_from_text(input_filename = input_filename, output_filename = output_filename)
    
if __name__ == "__main__":
    main()
    

