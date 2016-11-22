import os
from datetime import datetime

os.chdir('/Users/rokumura/Dropbox/programming/Knock100/toBrain')
os.system('git add .')
os.system('git commit -m "PushToBrain' + datetime.now().strftime("%Y_%m_%d %H-%M-%S") + '"')
os.system('git push origin master')
