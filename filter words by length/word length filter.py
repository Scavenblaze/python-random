target_length = 4
input_file = "lyrics.txt"
output_file = "words.txt"

count = 0

with open(input_file, 'r') as infile:
    with open(output_file, 'w') as outfile:
        for line in infile:
            words = line.split()
            
            for word in words:
                
                word_clean = ''.join(x for x in word if x.isalnum()) #remove punctuations
                
                if len(word_clean) == target_length:
                    outfile.write(word_clean + "\n")
                    count = count + 1

print(f"Total number of words: {count}")