from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import time

from django.conf import settings
dir = settings.STATICFILES_DIRS[0]

def mainlsa(saved_files):
	filename = saved_files[0]
	start_time = time.time()
	summary_words = 0 
	summary_characters = 0
	generated_summary = ''
	data = open(str(dir)+"\lsa.csv", "a")
	op = open(str(dir)+"\output_lsa.txt", "a")

	LANGUAGE = "english"
	SENTENCES_COUNT = 5
	parser = PlaintextParser.from_file(filename, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)
	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)
	summary = ''
	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		generated_summary+=str(sentence)
		op.write(str(sentence))
	new_time = time.time() - start_time
	summary_words = len(generated_summary.split())
	summary_characters = len(generated_summary)
	string = str(summary_characters)+" , "+str(summary_words)+" , "+str(new_time)+"\n"
	data.write(string)
	data.close()
	op.close()