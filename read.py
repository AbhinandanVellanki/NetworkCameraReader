import cv2, queue, threading, time
import numpy as np

# bufferless VideoCapture
class VideoCapture:

    def __init__(self,username,password,ip_address):
        #pipeline = "rtspsrc location=rtsp://admin:Aiacademy2021@192.168.50.7:554 latency=0 ! rtph265depay ! queue ! h265parse ! omxh265dec ! videoconvert ! appsink"
        #gst = "rtspsrc location=rtsp://admin:Aiacademy2021@192.168.50.7:554/test latency=0 ! rtph265depay ! h265parse ! omxh265dec ! videoconvert ! appsink"
        self.cap = cv2.VideoCapture(f"rtsp://{username}:{password}@{ip_address}:554/cam/realmonitor?channel=1@subtype=1")
        #self.cap = cv2.VideoCapture(pipeline)
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()

    # read frames as soon as they are available, keeping only most recent one
    def _reader(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Reading Error!")
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()   # discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put(frame)

    def read(self):
        return self.q.get()

if __name__ == '__main__':

    cap = VideoCapture('admin','Aiacademy2021','192.168.50.7')
    while True:
        try:
            frame = cap.read()
            cv2.imshow("img",frame)
            cv2.waitKey(1)
            print(f'Camera read, Size of frame is {np.shape(frame)}')
        except KeyboardInterrupt:
            print("Stopping Stream")
            break


