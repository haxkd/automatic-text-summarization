from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.kl import KLSummarizer
import time
from django.conf import settings
dir = settings.STATICFILES_DIRS[0]

def mainKLsum(saved_files):
	filename = saved_files[0]
	start_time = time.time()
	summary_words = 0 
	summary_characters = 0
	generated_summary = ''
	data = open(str(dir)+"\KL-Sum.csv", "a")
	op = open(str(dir)+"\output_KL-Sum.txt", "a")
	LANGUAGE = "english"
	SENTENCES_COUNT = 5		
	parser=PlaintextParser.from_file(filename,Tokenizer("english"))
	summarizer = KLSummarizer()
	summary = summarizer(parser.document,SENTENCES_COUNT)
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