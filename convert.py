import matplotlib.image as mpimg
from re import sub
import numpy as np
from os import system
from PIL import Image
import sys

# ASCII characters used..
# Adjusted based on brightness
ASCII_CODES = [' ', '.', '_', '~', '"', '=', 
                '*', '>', '?', '|', ']', '#', 
                '$', '@','A', 'B', 'C', 'X', 'W', 'M']

MAX_SIZE = len(ASCII_CODES)
KERNEL_SIZE = 2 # for image compression
PIXEL_SIZE = 512

def image_to_ascii( img_file, save_file ):
	try:
		#Ensure that KERNEL_SIZE divides PIXEL_SIZE evenly
		if PIXEL_SIZE % KERNEL_SIZE != 0:
			raise ValueError("PIXEL_SIZE must be divisible by KERNEL_SIZE")

        # laod and covert to grayscale...
		image = mpimg.imread( img_file )
		gray_image_255 = np.dot( image[..., :3], [0.2989, 0.5870, 0.1140] )
       	
		# if gray scale values if between 0 and 1 convert to 0 - 255 (standared)..
		if gray_image_255.max() <= 1.0:
			gray_image_255 = gray_image_255 * 255 

		pil_img = Image.fromarray( gray_image_255 )
		# resize image ( PIXEL_SIZE x PIXEL_SIZE )        
		resized = pil_img.resize( ( PIXEL_SIZE, PIXEL_SIZE ), Image.LANCZOS )
		resized = np.clip( np.array(resized), 0, 255 ).astype("uint8")
       
		with open( save_file, "w" ) as file:
			for row in range( 0, PIXEL_SIZE, KERNEL_SIZE ):
				for col in range( 0, PIXEL_SIZE, KERNEL_SIZE ):
					#take average in kernal block
					block = resized[ row:row+KERNEL_SIZE, col:col+KERNEL_SIZE ]           
					average_pixel = block.mean()
					# get the index for ASCII_CODES                  
					a_index = int( (average_pixel / 255) * (MAX_SIZE - 1 ) )	
					#take the char and write to file
					final_code = ASCII_CODES[ a_index ]
					file.write( final_code )
				file.write( '\n' )

		print( "DONE!" )
		## THIS COMMAND IS ONLY FOR LINUX CHANGE BEFORE RUNNING ##        
		system( f"xdg-open '{save_file}'" )
	except Exception as error:
		print( error )

if __name__ == "__main__":
	if len( sys.argv ) != 2:
		print( "provied image file" )
		sys.exit( 0 )
	# take image from agrs and save in .txt format
	fmts = r"\.(png|jpg|jpeg)$"
	img_file = sys.argv[1]
	save_file = sub(fmts, ".txt", img_file)

	image_to_ascii( img_file, save_file )
