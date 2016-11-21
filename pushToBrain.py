import os
from datetime import datetime

os.chdir('toBrain')
os.system('git add .')
nowdate = datetime.now().strftime("%Y_%m_%d %H-%M-%S")
os.system('git commit -m "PushToBrain' + nowdate + '"')
os.system('git push origin master')