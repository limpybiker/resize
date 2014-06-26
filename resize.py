"""
Script that allows scaling of images
"""

import Image, sys, os, argparse

def scale_down(imageFile, scalePercent):
    """
    Scale image down by given percentage. Will create a new 
    file with the same name plus '_small' in the same dir.
    """
    img = Image.open(imageFile)
    width, height = img.size

    # adjust width and height by percentage
    new_width = width  * scalePercent / 100
    new_height = height * scalePercent / 100


    new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    fileName, ext = os.path.splitext(imageFile)
    new_file_path = fileName + "_" + str(new_width) + "x" + str(new_height) + ext
    new_img.save(new_file_path)
    print "Created " + new_file_path


curDir = os.getcwd()
supportedExtensions = [".jpg", ".png"]

# create argparser
parser = argparse.ArgumentParser(description='Scale down images. Supported are JPG and PNG.')
parser.add_argument('files', type=str, nargs='+', help='The files to scale down.')
parser.add_argument('-p', '--percent', dest='percent', type=int, nargs='?', help='Scale image by this percentage, e.g. 30. Default is 50%%.', default=50)
args = parser.parse_args()

#read command line arguments
for arg in args.files:
    fileName, fileExtension = os.path.splitext(arg)

    if os.path.isfile(arg) and fileExtension.lower() in supportedExtensions:
        # absolute path
        if arg[0] == "/":
            file_path = arg
        # relative path
        else:
            file_path = curDir + os.path.sep + arg
        print "Scaling " + file_path
        scale_down(file_path, args.percent)
    elif os.path.isdir(arg):
        print "Folder " + arg + " cannot be scaled. Please select a file"
    else:
        print "Filetype " + fileExtension + " is not supported"



