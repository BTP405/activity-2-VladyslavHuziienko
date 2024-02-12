def wordCount(t):
    """Openning a file"""
    file = open(t)
    words_cnt = {}
    if file.closed == False:
        line = file.readline()
        line_cnt = 0
        """Reading line by line"""
        while len(line):
            """"In this loop set is used to get unique words"""
            unique_line_words = set()

            words_line = line.split(' ')
            for word in words_line:
                if(word != '\n'):
                    unique_line_words.add(word)

            """Appending a line number to the key of corresponding word"""
            for unique_word in unique_line_words:
                if unique_word in words_cnt:
                    words_cnt[unique_word].append(line_cnt)
                else:
                    words_cnt[unique_word] = [line_cnt]

            line_cnt += 1
            line = file.readline()

        return words_cnt
    else:
        print("Error opening a file")

results = wordCount('./q3_data.txt')
print(results)