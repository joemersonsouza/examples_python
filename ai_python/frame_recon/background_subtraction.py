import cv2
import numpy as np

def get_frame(cap, scaling_factor):

    _,frame = cap.read()

    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame

if __name__=='__main__':

    cap = cv2.VideoCapture(0)

    #Create a new background subtractor
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Define the number of previous frames to use to learn
    # This factor controls the learning rate of algorithm.
    # Higher value for history, indicates a slower learning rate and less assertive
    # Slower value for history, indicates a fast learning rate and high assertive
    history = 80

    # Setting a learning rate considering the history
    learning_rate = 1.0/history

    while True:

        frame = get_frame(cap, 0.5)

        # Compute the mask using learning rate int he background subtractor
        mask = bg_subtractor.apply(frame, learningRate=learning_rate)

        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        cv2.imshow('INPUT', frame)
        cv2.imshow('Detected Movement', mask & frame)

        # Verify if the user hit the escape key
        key = cv2.waitKey(5)
        if key == 27:
            break

    #Release capture video
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()

