import os,re,sys,platform
os.system('git pull')
os.system('pkg install play-audio')
import requests

bit = platform.architecture()[0]
if bit == '64bit':
    from crack64 import majn
    Main()
elif bit == '32bit':
    from crack import main
    main()