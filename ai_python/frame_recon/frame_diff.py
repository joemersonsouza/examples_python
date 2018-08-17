import cv2

#Compute the ai_python differences
def frame_diff(prev_frame, cur_frame, next_frame):

    # Get the difference between the current ai_python and the next ai_python
    first_diff_frame = cv2.absdiff(next_frame, cur_frame)

    # Get the difference between the current ai_python and the previous ai_python
    second_diff_frame = cv2.absdiff(next_frame, prev_frame)

    # Return the difference between first and second diff ai_python
    return cv2.bitwise_and(first_diff_frame, second_diff_frame)

def get_frame(cap, scalling_factor):

    # Read the current ai_python from the camera
    _, frame = cap.read()

    # Resize the captured image
    frame = cv2.resize(frame, None, fx=scalling_factor, fy=scalling_factor, interpolation=cv2.INTER_AREA)

    # Convert to grayscale
    return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

if __name__=='__main__':

    # Define the vide capture object
    cap = cv2.VideoCapture(0)

    # Define the scaling factor for the images
    scaling_factor = 0.5

    # Grab the previous ai_python
    prev_frame = get_frame(cap, scaling_factor)

    # Grab the current ai_python
    cur_frame = get_frame(cap, scaling_factor)

    # Grab the next ai_python
    next_frame = get_frame(cap, scaling_factor)

    # Keep the reading frames alive from the webcam
    # until the user hits the 'Esc' key

    while True:

        #Start a new window with ai_python diff detection
        cv2.imshow('Detecting Movements', frame_diff(prev_frame, cur_frame, next_frame))

        # Update the variables
        prev_frame = cur_frame
        cur_frame = next_frame

        # Grab the next ai_python
        next_frame = get_frame(cap, scaling_factor)

        # Verify if the user hit the escape key
        key = cv2.waitKey(10)
        if key == 27:
            break

    # Close all windows
    cv2.destroyAllWindows()