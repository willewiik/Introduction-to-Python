#!/usr/bin/env python3
import text_stats
import random
import sys
import numpy as np
from collections import defaultdict


def randomize_text(all_words, starting_word, max_num_of_words):
  
    # Dictionary of word index
    dict_word = defaultdict(list)
    for pos, ele in enumerate(all_words[:-1]):
      dict_word[ele].append(pos)
    
    
    cur_word = starting_word
    msg = [cur_word]
    for itr in range(max_num_of_words):
        if(len(dict_word[cur_word])) > 0:
            index = random.choice(dict_word[cur_word])+1
            cur_word = all_words[index]
            msg.append(cur_word)
        else:
            break
    print(" ".join(msg))


def generate_text_algorithm(filename, starting_word, max_num_of_words):
  
  # Check if the file exists
  try:
    with open(filename, 'r', encoding='utf-8') as file:
      content = file.read()
  except FileNotFoundError:
    print("The file does not exist!")
    return
  
  max_num_of_words = int(max_num_of_words)
  all_words = text_stats.clean_text_to_words(content)
  randomize_text(all_words = all_words, starting_word = starting_word, max_num_of_words = max_num_of_words)




def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Error: requires 3 arguments")
        sys.exit(1)
    
    filename = sys.argv[1]
    starting_word = sys.argv[2]
    max_num_of_words = sys.argv[3]
    
    generate_text_algorithm(filename, starting_word, max_num_of_words)
    
if __name__ == "__main__":
    main()




