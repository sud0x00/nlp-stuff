from nltk.tokenize import sent_tokenize, word_tokenize

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec tristique purus"
test_sentence = sent_tokenize(text)
for sentence in test_sentence : 
  print(sentence)
  print(word_tokenize(sentence))
