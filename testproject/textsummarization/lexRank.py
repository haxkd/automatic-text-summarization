#Import library essentials
from lib2to3.pgen2.pgen import generate_grammar
from sumy.parsers.plaintext import PlaintextParser 
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer 
import time

from django.conf import settings
dir = settings.STATICFILES_DIRS[0]


def mainlexRank(saved_files):
	filename = saved_files[0]
	start_time = time.time()
	summary_words = 0 
	summary_characters = 0
	generated_summary = ''
	data = open(str(dir)+"\lexrank.csv", "a")
	op = open(str(dir)+"\output_lexrank.txt", "a")
	parser = PlaintextParser.from_file(filename, Tokenizer("english"))
	summarizer = LexRankSummarizer()
	summary = summarizer(parser.document, 5) 
	for sentence in summary:
		generated_summary+=str(sentence)
		op.write(str(sentence))
	new_time = time.time() - start_time
	summary_words = len(generated_summary.split())
	summary_characters = len(generated_summary)
	string = str(summary_characters)+" , "+str(summary_words)+" , "+str(new_time)+"\n"
	data.write(string)
	data.close()
	op.close()