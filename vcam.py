import imageio
import cv2
from config import RESIZE_WIDTH, RESIZE_HEIGHT, FRAME_RATE, TOPMOST

def visualization():

    DELAY = int(1000 / FRAME_RATE)

    reader = imageio.get_reader('<video1>')
    cv2.namedWindow('the great depression', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('the great depression', RESIZE_WIDTH, RESIZE_HEIGHT)
    cv2.setWindowProperty('the great depression', cv2.WND_PROP_TOPMOST, TOPMOST)

    window_x = 0
    window_y = 0

    cv2.moveWindow('the great depression', window_x, window_y)

    for frame in reader:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow('the great depression', frame)
        if cv2.waitKey(DELAY) == ord('q'):
            break

    reader.close()
    cv2.destroyAllWindows()