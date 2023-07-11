with open('my_text.txt') as my_text:
    for text in my_text:
        text = text.replace('.', '').replace(',', '')
        text_list = [x for x in text.split()]
my_dict = {}
for words in text_list:
    if words in my_dict:
        my_dict[words] += 1
    else:
        my_dict[words] = 1
sorted_word_count = sorted(my_dict.items(), key=lambda x: x[1])
for i, counts in sorted_word_count:
    print(f'{i}: {counts}')
