# Unigram and Bigram Counter

## Overview

This C program implements a simple Unigram and Bigram counter using hash tables. It reads text from a file, processes the text to count the occurrences of individual words (unigrams) and pairs of consecutive words (bigrams), and allows the user to interactively update and display the counts. The program converts all words to lowercase before counting to ensure that "Word" and "word" are treated as the same. This functionality is particularly useful in text analysis, natural language processing, and data mining applications.

The program is designed to be efficient and scalable, utilizing dynamic memory management to handle varying sizes of input text. It employs a hash table to store the counts, which allows for quick lookups and updates.

## Features

- **Unigram Counting**: Counts the occurrences of each word in the input text, providing insights into word frequency.
- **Bigram Counting**: Counts the occurrences of each pair of consecutive words, which can help identify common phrases and patterns in the text.
- **Dynamic Memory Management**: Uses dynamic memory allocation to handle varying sizes of input, ensuring efficient use of resources.
- **Interactive Menu**: Provides a user-friendly console menu for updating and displaying unigram and bigram counts, making it easy to use for non-technical users.
- **File Input**: Reads text from a specified file, allowing for easy analysis of large datasets without manual input.
- **Case Insensitivity**: Converts all words to lowercase to ensure consistent counting, which is essential for accurate text analysis.

## Usage

1. **Compile the Program**: Use a C compiler (e.g., `gcc`) to compile the program.
   ```bash
   gcc -o unigram_bigram_counter unigram_bigram_counter.c