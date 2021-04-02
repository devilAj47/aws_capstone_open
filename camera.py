import cv2 as cv
class VideoCamera(object):

    def __init__(self):
        self.video = cv.VideoCapture(0)
        #self.video = cv.VideoCapture('Video.mp4')        

    def __del__(self):
        self.video.release()
        
    def get_image(self):
        ret, img = self.video.read()
        return img
