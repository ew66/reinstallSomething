# reinstallSomething

###### usage: 
            reinstallSomething.py [-h] (-i | -r | -p) [something_name_list [something_name_list ...]]

###### Reinstall Something in your $OUT/system
#### Environment configuration:
        Linux / Mac OS X: export [Your AOSP out path/system] into your system environment variable $OUT
> ex: export OUT /AOSP/LINUX/Android/out/target/product/new_build/system

        Windows         : create a file with absolute OUT path under "C:\Users\[Username]\OUT_PATH"
> ex: write "/AOSP/LINUX/Android/out/target/product/new_build/system" into "C:\Users\[Username]\OUT_PATH"

###### positional arguments:
   something_name_list
> ex: Camera2.apk, library_name.so
 
###### optional arguments:
``` 
   -h, --help           show this help message and exit
   -i                   install something
   -r                   remove something
   -p                   pull something
```
