from . import KLsum, lexRank, lsa, TFIDF, ComparisonGraphCharacters, ComparisonGraphWords
from django.conf import settings

dir = settings.STATICFILES_DIRS[0]


def calculateIt(saved_files):
    # print('called')
    KLsum.mainKLsum(saved_files)
    lexRank.mainlexRank(saved_files)
    lsa.mainlsa(saved_files)
    TFIDF.mainTFIDF(saved_files)
    ComparisonGraphCharacters.compareByChar()
    ComparisonGraphWords.CompareByWord()


def getAllData():
    data = []
    files = [
        str(dir)+"\output_KL-Sum.txt",
        str(dir)+"\output_lexrank.txt",
        str(dir)+"\output_lsa.txt",
        str(dir)+"\output_TF-IDF.txt",
    ]
    for file in files:
        f = open(file,"r")
        data.append(f.read())
    return data
