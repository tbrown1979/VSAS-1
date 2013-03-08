from VideoCapture import Device
import time
from Motion import *
import cv2

def totalChange( greenScaleImage ):
    count = 0
    for pixel in greenScaleImage.getdata():
        if pixel != (0, 255, 0, 0):
            count += 1
    return count

def adjustCamera( cam ):
    for x in xrange(3):
        initialImage = cam.getImage()
        initialImage.save('image.jpg')
        time.sleep(5)
    return initialImage

def main():
    
    cam = Device()

    print "Getting initial image, and adjusting camera..."
    initialImage = adjustCamera( cam )
    initialImage.save('initialImage.jpg')
    print "initial image saved and webcam adjusted..."


    recordedImages = [totalChange]
    end            = False

    while True:
        time.sleep(.5)
        newImage = cam.getImage()
        compared = compare_images( initialImage, newImage, 70, ANY_2RGB )

        amtPxChanged = totalChange( compared )
        if amtPxChanged > 30000:
            print "Recording..."
            recordedImages.append( newImage )
            time.sleep(.5)
            compared.save('recording.jpg')#' + str(imgNum) + '.jpg')

            amtPxChanged = totalChange( compared )
            end = True
            print amtPxChanged
        else:
            print "not recording..."
        # if end:
        #     break

        compared.save('notRecording.jpg')


main()
