import numpy as np
from sklearn import preprocessing

if __name__ == '__main__':

    input_colors = ['red', 'blue', 'green', 'gray', 'black', 'white']

    # Creating an encoder and transforming the colors into a number
    # store the number into encoder
    encoder = preprocessing.LabelEncoder()
    encoder.fit(input_colors)

    # Print the mapping
    print("\nLabel mapping:")
    for i, item in enumerate(encoder.classes_):
        print(item, '-->', i)

    # Casting number to color encoded
    number_colors = [0, 2, 5]
    decode_list = encoder.inverse_transform(number_colors)
    print("\nEncoded values = ", number_colors)
    print("\nDecoded values = ", list(decode_list))

    # Casting color to encoded number
    sample = ['blue', 'green', 'yellow']
    for color in sample:
        if(not input_colors.__contains__(color)):
            print("\nColors = ", sample)
            print("Color not found in the list ", color)
            sample.remove(color)

    enconded_list = encoder.transform(sample)
    print("\nColors = ", sample)
    print("\nEncoded values = ", list(enconded_list))

