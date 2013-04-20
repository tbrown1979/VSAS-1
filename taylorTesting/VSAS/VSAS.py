from VSASmainScreen import *
from MotionDetector import *
from MotionDetectorTest import *
from VideoRecorder  import *

def main():
    motion = MotionDetector() #video )
    motionThread = threading.Thread(None, motion)
    motionThread.daemon = True #daemon threads are background task threads
    motionThread.start()

    # video = VideoRecorder()
    # motion = MotionDetectorTest()
    # motionThread = threading.Thread(None, motion)
    # motionThread.daemon = True #daemon threads are background task threads
    # motionThread.start()

    vsas = Application(motion, root)
    vsasThread = threading.Thread(None, vsas)
    vsasThread.start()

    
main() 
