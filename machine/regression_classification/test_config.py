from sklearn import datasets

if __name__ == '__main__':

    iris_values = datasets.load_iris()

    print(iris_values.data)

    digits = datasets.load_digits()

    print(digits.images[4])