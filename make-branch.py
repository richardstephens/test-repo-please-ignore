#!/usr/bin/env python3

import os
import random
import string
import webbrowser
from datetime import datetime

now = datetime.now()
letters = string.ascii_lowercase

branch_name = "branch-" + ''.join(random.choice(letters) for i in range(4))

fn = './logs/' + ''.join(random.choice(letters) for i in range(2)) + '.txt'

os.system("git checkout -b " + branch_name)
os.system("date >> " + fn)
os.system("echo 'test log line' >> " + fn)
os.system("git add " +fn)
os.system("git commit -m 'test commit at " + now.strftime("%m/%d/%Y, %H:%M:%S")+"'")
os.system("git push  --set-upstream origin " + branch_name)
webbrowser.open("https://github.com/richardstephens/test-repo-please-ignore/pull/" + branch_name)

