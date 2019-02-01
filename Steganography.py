#!/usr/bin/python36

import subprocess as sp
#ch=int(input("""
#Choose one of the options:
#1. Video Steganography
#2. Image Steganography
#	"""))
#if ch==1:
#	print("Video Steganography using Caesar Cypher")
#	ccvs=sp.getstatusoutput('python /root/Desktop/CCVS/main.py')
#	print(ccvs[1])
#elif ch==2:
ch1=int(input("""
	Choose an option:
	1. Encode
	2. Decode
		"""))
	
if (ch1==1):
	inpath=input("Enter the complete path of image to be encrypted :")
	outpath=input("Enter the complete path of the output image :")
	ch2 = int(input("""
		Do you want the message to come from a file or a string:
		1> File
		2> Message
		"""))
	if ch2==1:
		filename=input("Enter full path of the file:")
		ch3=int(input("""
		Enter the algorithm to use:
		1. DCT
		2. LSB
			"""))
		if ch3==1:
			final=sp.getstatusoutput('python36 /root/Desktop/dctlsb/stego.py -i {} -o {} -f {}'.format(inpath,outpath,filename))
		elif ch3==2:
			final=sp.getstatusoutput('python36 /root/Desktop/dctlsb/stego.py -i {} -o {} -f {} -a'.format(inpath,outpath,filename))
	elif ch2==2:
		message=input("Enter the message to hide:")
		ch3=int(input("""
		Enter the algorithm to use:
		1. DCT
		2. LSB
			"""))
		if ch3==1:
			final=sp.getstatusoutput('python36 /root/Desktop/dctlsb/stego.py -i {} -o {} -s "{}"'.format(inpath,outpath,message))
		elif ch3==2:
			final=sp.getstatusoutput('python36 /root/Desktop/dctlsb/stego.py -i {} -o {} -s "{}" -a'.format(inpath,outpath,message))
elif ch1==2:
	inpath=input("Enter the complete path of image to be decrypted :")
	ch2=int(input("""
			Enter the algorithm to use:
			1. DCT
			2. LSB
			"""))
	if ch2==1:
		final=sp.getstatusoutput('python36 /root/Desktop/dctlsb/stego.py -i {} -d'.format(inpath))
	elif ch2==2:
		final=sp.getstatusoutput('python36 /root/Desktop/dctlsb/stego.py -i {} -a -d'.format(inpath))
	print(final[1])
