import multiprocessing
import wordcount

results = {}

def get_a():
    wordcount.most_common_words()

def get_b():
    wordcount.most_common_word_of_quarter()

process_a = multiprocessing.Process(target=get_a)
process_b = multiprocessing.Process(target=get_b)

process_b.start()
process_a.start()

process_b.join()
process_a.join()
