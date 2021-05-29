# prepare english tokenizer
eng_tokenizer = create_tokenizer(dataset[:, 0])
eng_vocab_size = len(eng_tokenizer.word_index) + 1
eng_length = max_length(dataset[:, 0])
print('English Vocabulary Size: %d' % eng_vocab_size)
print('English Max Length: %d' % (eng_length))

# prepare french tokenizer
fre_tokenizer = create_tokenizer(dataset[:, 1])
fre_vocab_size = len(fre_tokenizer.word_index) + 1
fre_length = max_length(dataset[:, 1])
print('French Vocabulary Size: %d' % ger_vocab_size)
print('French Max Length: %d' % (ger_length))