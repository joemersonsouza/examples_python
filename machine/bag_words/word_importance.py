import scipy as sp


def word_importance(term, docs, corpus):
    frequency = docs.count(term) / len(docs)
    num_doc_with_terms = len([doc for doc in corpus if term in doc])
    inverse_frequency = sp.log(len(corpus) / num_doc_with_terms)
    return frequency * inverse_frequency


if __name__ == '__main__':
    a, abb, abc = ["a"], ["a", "b", "b"], ["a", "b", "c"]
    D = [a, abb, abc]
    print("\nImportance of a in abc value ",word_importance("a", a, D))
    print("\nImportance of b in abc value ", word_importance("b", abb, D))
    print("\nImportance of c in abc value ", word_importance("c", abc, D))

