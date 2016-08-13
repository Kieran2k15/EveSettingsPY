#!/usr/bin/python

import sys, getopt, glob, os, shutil

def getMasterUserFile(userID):
	return glob.glob("core_user_" + userID + "*.dat")

def getMasterCharFile(charID):
	return glob.glob("core_char_" + charID + "*.dat")
	
def getUserIdArray():
	userIdArray = []
	for file in glob.glob('core_user_[0-9]*.dat'):
		userIdArray.append(file)
		
	return userIdArray
		
def getCharIdArray():
	charIdArray = []
	for file in glob.glob('core_char_[0-9]*.dat'):
		charIdArray.append(file)
		
	return charIdArray
		
def updateUsingMasterAccount(masterUserId, masterCharId, folder):
	print("Updating settings using master account")
	os.chdir(folder)
	masterUserFilename = getMasterUserFile(masterUserId)[0]
	masterCharFilename = getMasterCharFile(masterCharId)[0]
	
	userFileArray = getUserIdArray()
	userFileArray.remove(masterUserFilename)

	charFileArray = getCharIdArray()
	charFileArray.remove(masterCharFilename)
	
	for file in userFileArray:
		os.remove(file)
		shutil.copy(masterUserFilename, file)
		
	for file in charFileArray:
		os.remove(file)
		shutil.copy(masterCharFilename, file)
		
# py EveSettings.py -u 424242 -c 4242424242 -f 
def main(argv):
	print("Updating EVE Settings")
	if (len(sys.argv) < 2):
		print("Invalid IDs")
	
	masterUserId = ''
	masterCharId = ''
	folder = ''
	
	try:
		opts, args = getopt.getopt(argv,"hu:c:f:",["masterUserId=","masterCharId=","folder="])
	except getopt.GetoptError:
		print ('EveSettings.py -u <UserID> -c <CharID> -f <settings folder location>')
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print ('EveSettings.py -u <UserID> -c <CharID> -f <settings folder location>')
			sys.exit()
		elif opt in ("-u", "--masterUserId"):
			masterUserId = arg
		elif opt in ("-c", "--masterCharId"):
			masterCharId = arg
		elif opt in ("-f", "--folder"):
			folder = arg
	
	updateUsingMasterAccount(masterUserId, masterCharId, folder)

if __name__ == "__main__": main(sys.argv[1:])