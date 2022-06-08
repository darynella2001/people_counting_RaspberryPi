from mylib.centroidtracker import CentroidTracker
from mylib.trackableobject import TrackableObject
from imutils.video import VideoStream
from imutils.video import FPS
from mylib.mailer import Mailer
from mylib import config, thread
import time, schedule, csv
import numpy as np
import argparse, imutils
import time, dlib, cv2, datetime
from itertools import zip_longest
from image_processing import start_image_processing
import threading


class CameraModuleWrapper:
	def __init__(self):
		self.write_aborted = False
		self.video_file_name = 'passengers_recording.mp4'

	
	def enable(self):
		self.capture = cv2.VideoCapture(1)

		self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
		self.output_video = cv2.VideoWriter(self.video_file_name, self.codec, 30, (self.frame_width, self.frame_height))

		while True:
			if self.capture.isOpened():
				(self.status, self.frame) = self.capture.read()
			
				self.output_video.write(self.frame)


	def disable(self):
		self.capture.release()
		self.output_video.release()

		threading.Thread(target=start_image_processing, args=(self.video_file_name,))


t0 = time.time()

