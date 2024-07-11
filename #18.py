# This week, we'll experiment with threads. Here's the basic idea: I want to count all of the words in all of the files that match a particular pattern. (We'll use "glob.glob" to retrieve the files matching that pattern.)
#
# The idea is that I can invoke the function
#    count_words('/foo/bar/*.txt')
#
# and all of the words (i.e., strings separated by one or more whitespace characters) will be counted.
#
# I want you to implement this twice:
# count_words goes through each of the matching files sequentially
# count_words opens a thread for each of the files.
#
# In order to implement the second version of count_words, you might need to learn a bit about how threading works in Python.
# In particular, you('ll want to use the "threading" library (and the "Thread" class within it), including the "start" and "join" methods.  '
# 'You')ll also probably want to use a "Queue" (in the "queue" module) to synchronize the information you've found so far.

#you will need files with words as "foo/bar/any_text_files.txt

import glob
import threading
import queue
def count_words_sequential(pattern):
    total_words = 0
    files = glob.glob(pattern)

    for file in files:
        with open(file,'r') as f:
            content =  f.read()
            words = content.split()
            total_words += len(words)
    return total_words

print(count_words_sequential('foo/bar/*.txt'))


def count_words_in_file(file,q):
    with open(file,"r" ) as f:
        content = f.read()
        words = content.split()
        q.put(len(words))


def count_words_threaded(pattern):
    total_words = 0
    files = glob.glob(pattern)
    q= queue.Queue()
    threads = []

    for file in files:
        thread = threading.Thread(target=count_words_in_file, args =(file,q))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    while not q.empty():
        total_words += q.get()

    return total_words

print(count_words_threaded('foo/bar/*.txt'))

