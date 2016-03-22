# reinstallSomething
#
# usage: reinstallSomething.py [-h] (-i | -r | -p)
#                             [something_name_list [something_name_list ...]]
#
# Reinstall Something in your $OUT/system
#       Linux / Mac OS X: export $OUT into env
#       Windows         : create a file with absolute OUT path under "C:\Users\[Username]\OUT_PATH"
#
# positional arguments:
#   something_name_list  ex: Camera2.apk, library_name.so
# 
# optional arguments:
# 
#   -h, --help           show this help message and exit
#   -i                   install something
#   -r                   remove something
#   -p                   pull something
