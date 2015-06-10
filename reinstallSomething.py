#!/usr/bin/python

# ** reinstallSomething by Edgar ** 
#
# USAGE:
# 	input filename, and then find the file path in $OUT/system/, then reinstall this file in your mobile phone.

import os 
import sys
import time
import datetime
from subprocess import call, Popen, PIPE
import argparse

######################
##     function     ##
######################

def getDevices():
	adbStdout, err = Popen(["adb", "devices"], stdout=PIPE).communicate()
	adbStdoutList = adbStdout.splitlines()
	adbDevices = []
	for item in adbStdoutList:
		temp = item.split('\t')
		if len(temp) == 2 and temp[1] == "device":
			adbDevices.append(temp[0])
			
	if len(adbDevices) > 1:
		while(1):
			for device in adbDevices:
				print adbDevices.index(device)+1, ")" , device
			deviceInput = sys.stdin.readline()
			if int(deviceInput) < len(adbDevices)+1 and int(deviceInput) >= 1:
				break	
		return adbDevices[int(deviceInput)-1]
	elif len(adbDevices) == 1:
		return adbDevices[0]
	else:
		print "No devices is connected."
		exit()

def somethingAction(serial, action):
	something_action = ["adb", "-s", serial] + action
	call(something_action)


def pushSomething(serial, source_path, dest_path):
	# push something into mobile
	print "push " + source_path + " to " + serial + ":" + dest_path
	action = ["push", source_path, dest_path]
	somethingAction(serial, action)

def removeSomething(action, path):
	# rm something from mobile
	print "remove " + serial + path
	action = ["shell", "rm", path]
	somethingAction(serial, action)
	
def pullSomething(action, path):
	# pull something from mobile
	print "pull " + serial + path
	action = ["pull", path, "./"]
	somethingAction(serial, action)


# 1. parse arguments
#	-i: interactive commit message
#	-c: comment in code
parser = argparse.ArgumentParser(description='Reinstall Something in your $OUT/system')
group = parser.add_mutually_exclusive_group(required=True)
parser.add_argument('something_name_list', default='', nargs='*', help='ex: Camera2.apk, library_name.so')
group.add_argument('-i', help='install something', action='store_const', const=1)
group.add_argument('-r', help='remove something', action='store_const', const=2)
group.add_argument('-p', help='pull something', action='store_const', const=3)
group.add_argument('-I', help='overly path in env $OUT_OVERLAY', action='store_const', const=4)

args = parser.parse_args()
use_overlay = False;
if args.I != None:
    use_overlay = True;
    
something_name_list = args.something_name_list

#print args.something_name_list
#exit();
serial = getDevices()
# get $OUT path
env_out_path = os.environ.copy()["OUT"]
if use_overlay == True:
    try:
        overlay_path = os.environ.copy()["OUT_OVERLAY"]
        if overlay_path:
            env_out_path = overlay_path
    except:
        pass

# search path=$OUT/system
something_root_path = env_out_path + '/system'

for something_name in something_name_list:
    # find something path 
    something_path, err = Popen(["find", something_root_path, "-name", something_name], stdout=PIPE).communicate()
    if something_path == '':
    	print "Error: Can not find " + something_name + " in " + something_root_path
    	break
    # something_path=$OUT/system/something_dest_path
    something_path = something_path.strip()
    something_path_list = something_path.split('\n')
    push_operation = False
    
    for something in something_path_list:
       push_operation = True
       something = something.strip()
       something_dest_path = something.replace(env_out_path,'')
       
       # push something
       if args.i != None or args.I != None:
       	pushSomething(serial, something, something_dest_path)
    
    # pull something
    if args.p != None:
       pullSomething(serial, something_dest_path)
    # remove something
    elif args.r !=None:
       removeSomething(serial, something_dest_path)
    elif push_operation == False:
       parser.print_help()
       exit()


