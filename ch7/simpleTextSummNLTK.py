# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:23:58 2016
@author: megan squire
"""
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from collections import OrderedDict

# this is a sample of text from the chapter
text = '''
In the academic literature, text summarization is often proposed as a
solution to information overload, and we in the 21st century like to
think that we are uniquely positioned in history in having to deal with
this problem. However, even in the 1950s when automatic text
summarization techniques were in their infancy, the stated goal was
similar. Luhn's 1958 paper "The automatic creation of literature abstracts,"
describes a text summarization method that will "save a prospective
reader time and effort in finding useful information in a given article or
report" and that the problem of finding information "is being aggravated by
the ever-increasing output of technical literature."

With this early work, Luhn proposed a text summarization method where the
computer would read each sentence in a paper, extract the
frequently-occurring words, which he calls significant words, and then
look for the sentences that had the most examples of those significant
words. This is an early example of an extractive method of text
summarization. In an extractive summarization method, the summary is
comprised of words, phrases, or sentences that are drawn directly from
the original text. Ideally, a text will have one or more main ideas or
topic sentences that themselves serve as summaries of some portion of
the text. Then, the extractive summarization algorithm will look for
these important sentences. As long as the amount of text that is
extracted is a subset of the original text, this type of summarization
achieves the goal of compressing the original text into a shorter size.

Alternatively, an abstractive summarization attempts to distill the key
ideas in a text and repackage them into a human-readable, and usually
shorter, synthesis. This task is similar to paraphrasing. However, since
the goal is to create a summary, abstractive methods must also reduce
the length of the text while focusing on only retaining the most
important concepts in it.

In this chapter we will focus on summarization techniques for text
documents, but researchers are also working on summarization algorithms
designed for video, images, sound, and more. Some of these data types
lend themselves better to extractive summarization - for example a video
summary would probably consist of clips taken from the videos
themselves. We will focus on single-document summaries in this chapter,
but there are also summarization techniques that are designed to work
with collections of documents. The idea with multiple document
summarization is that we can scan across a number of similar documents,
picking out the main ideas correctly, while ensuring that the resulting
summary is free of duplicates and is human-readable.

In the next section we will review some of the currently available text
summarization libraries and applications.
'''
summary_sentences = []
candidate_sentences = {}
candidate_sentence_counts = {}
striptext = text.replace('\n\n', ' ')
striptext = striptext.replace('\n', ' ')

# get list of sentences
sentences = sent_tokenize(striptext)
i = 0
for sentence in sentences:
    candidate_sentences[sentence] = [sentence.lower(), i]
    i += 1
# get list of top 20 most frequent words
words = word_tokenize(striptext)
lowercase_words = [word.lower() for word in words
                   if word not in stopwords.words() and word.isalpha()]
word_frequencies = FreqDist(lowercase_words)
most_frequent_words = FreqDist(lowercase_words).most_common(20)

# print out the keywords more nicely
for pair in most_frequent_words:
    print(pair[0],":",pair[1])

# which sentences are these important words found in?
for long, value in candidate_sentences.items():
    score = 0
    for freq_word, frequency_score in most_frequent_words:
        if freq_word in value[0]:
            # score the sentence according its count of important words
            score += frequency_score
            candidate_sentence_counts[long] = [score, value[1]]

# get first 4 results, sorted by score
sorted_sentences = OrderedDict(sorted(candidate_sentence_counts.items(),
                                     key=lambda x: x[1],
                                      reverse=True)[:4])

# now sort the sentences back into 
# the order in which they appeared in the article
finalList = []
for sentence in sorted_sentences:
    ordered = [candidate_sentence_counts.get(sentence)[1],sentence]
    finalList.append(ordered)
for finalSentence in sorted(finalList):
    print(finalSentence)
