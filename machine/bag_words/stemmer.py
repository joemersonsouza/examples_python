import nltk.stem
import scipy as sp

from sklearn.feature_extraction.text import TfidfVectorizer


class StemmedCountVectorizer(TfidfVectorizer):

    def build_analyzer(self):
        english_stemmer = nltk.stem.SnowballStemmer('english')

        analyzer = super(StemmedCountVectorizer, self).build_analyzer()

        return lambda doc: (english_stemmer.stem(w) for w in
                    analyzer(doc))