import os
from datetime import datetime
from subprocess import run

os.chdir('/Users/rokumura/Documents/programming/Knock100/toBrain')
run(['git', 'add', '.'])
run(['git', 'commit', '-m', ' "PushToBrain' + datetime.now().strftime("%Y_%m_%d %H-%M-%S") + '"'])
run(['git', 'push', 'origin', 'master'])
