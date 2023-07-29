import cv2


def generate_frame():
    # Accessing the camera 
    cap = cv2.VideoCapture(0)

    # Defining the codec and creating the VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    file_name = 'output'
    output = cv2.VideoWriter((file_name+'.avi'), fourcc, 24.0, (640,  480))

    # Defining the variables save and c
    save = 'Frame1'
    c = 2;
    while cap.isOpened():

        res, frame = cap.read()
        if not res:
            print("Frame Cannot Be Received")
            break
        
        # Flipping the frame horizontally to get correct orientation
        frame = cv2.flip(frame, 90)

        # Displaying the current frame
        output.write(frame)
        cv2.imshow('Frame', frame)

        # Saving the frames
        cv2.imwrite(save+'.png', frame )
        save = "Frame"+ str(c)
        c = c+1

        # If no input is received for 1ms, or if the key 'x' is pressed, interpreter goes outside of the loop
        if cv2.waitKey(1) == ord('x'):
            break

    # Releasing everything after coming out of loop
    cap.release()
    output.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    generate_frame()
