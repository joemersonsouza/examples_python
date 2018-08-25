import os
import scipy as sp
import sys
import argparse
from bag_words.stemmer import StemmedCountVectorizer


# Argument parser
def build_arg_parser():
    parser = argparse.ArgumentParser(description='Word to be find')
    parser.add_argument('--find', dest='new_post',
                        required=False, help="Post to be find")
    return parser


def dist_raw(v1, v2):
    delta = v1-v2
    return sp.linalg.norm(delta.toarray())


def get_best_distance_from_post(post_train, posts, new_post, new_post_vec):

    best_distance = sys.maxsize
    best_position = None
    best_post = None

    for position, post in enumerate(posts):

        if post == new_post:
            continue

        post_vec = post_train.getrow(position)
        distance = dist_raw(post_vec, new_post_vec)

        if distance < best_distance:
            best_distance = distance
            best_position = position
            best_post = post

    return best_position, best_distance, best_post


if __name__ == '__main__':

    # Parse the input arguments
    args = build_arg_parser().parse_args()
    new_post = args.new_post

    dir = "files"
    vectorizer = StemmedCountVectorizer(min_df=1, stop_words="english", decode_error="ignore")

    posts = [open(os.path.join(dir, f)).read() for f in os.listdir(dir)]

    posts_train = vectorizer.fit_transform(posts)
    num_samples, num_features = posts_train.shape

    if new_post is None :
        new_post = "Imaging databases"

    new_post_vec = vectorizer.transform([new_post])

    best_position, best_distance, best_post = get_best_distance_from_post(posts_train, posts, new_post, new_post_vec)

    if not new_post in best_post:
        print("value not found")
    else:
        print("Best post in the position %i\nwith dist=%.2f %s"%(best_position, best_distance, best_post))
