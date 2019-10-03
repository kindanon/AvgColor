import cv2
import sys
import numpy
import Image

def spit(video, start):
	#todo

def do(video):
	success,image = video.read()
	avg_img = numpy.array(image)
	count = 1
	while success:
		#testing
		#cv2.imwrite("frame%d.jpg" % count, image)
		success,image = video.read()
		avg_img = avg_img+numpy.array(image)
		count += 1
	
	#todo literally all testing
	#todo convert cv2 from bgr to rgb
	avg_img = [x / count for x in avg_img]
	img = Image.fromarray(avg_img)
	img.save("final.png")


def main():
	#for now
	print "put this python file into the same directory as the video, \
	use shift+right-click to open a terminal window there, \
	run the script as \"python avg_color.py <file name>\""
	
	#for later
#    if len(sys.argv) > 1:
#        
#    else:
#        #print "input path to file"
#        user_path = raw_input("input path to file:\n")
	video = cv2.VideoCapture(sys.argv[1])
	#TODO error checking
	#split(video, 0)
	do(video)

if __name__ == "__main__":
	main()
