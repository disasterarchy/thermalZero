from leanuvc import *
import time

#np.set_printoptions(linewidth=np.nan) #Don't add newlines!
np.set_printoptions(threshold='nan')	 #Output whole matrix

number_of_frames = 2  	#Collect this many frames
time_to_sleep = 0	#Wait this long in between

while True:
	for i in range(0,number_of_frames):
		rw  = GetData()
		rw1d = np.reshape(rw,-1)
		tempsF =ktof(rw1d)
		x_arrastr = np.char.mod('%f',tempsF)
		ss = " ".join(x_arrastr)
	#	ss = np.array2string(tempsF, separator = ' ')
	print ss
	time.sleep(time_to_sleep)
