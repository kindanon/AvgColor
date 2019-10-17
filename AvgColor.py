
#3hr movie has 15mil frames
#1920*1080 has 2mil pixels
#30,000,000,000,000 total pixels

#MEAN
#add all rg&b values to a 2d array divide by total frame count
#do not append, just add

#MEDIAN
#middle 
#probably have to split the movie into chunks because ram is finite

#MODE
#most common

#functions
#need to read in movie
#need to split movie into chunks
#need to split chunks into frames
#need to convert frames cv2
#need to calculate MMM

#main call import with file name
#import call chunk with file
#& chunk call frames with chunks
#frames call mean calc
#frames call median & mode calc
#main call printer

import cv2
import sys
import numpy
import Image

movie_pixels = np.empty((0,3), int)

def split(video, start):
	#todo
	return 0

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
	print ("\n1. put this python file into the same directory as the video\n"+
	"2. use shift+right-click to open a powershell window there\n"+
	"3. run the script as \"python AvgColor.py <file name>\"\n")
	
	#for later
#    if len(sys.argv) > 1:
#        
#    else:
#        #print "input path to file"
#        user_path = raw_input("input path to file:\n")
	#video = cv2.VideoCapture(sys.argv[1])
	#TODO error checking
	#split(video, 0)
	#do(video)

if __name__ == "__main__":
	main()
