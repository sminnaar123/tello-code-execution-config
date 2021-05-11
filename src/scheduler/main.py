'''
    1. Add all ready-files to list

    2. Get random ready-file

    3. Execute ready-file

    4. Remove ready-file (from list and file)

    5. No files in list?
       goto 1
       else go to 2
'''

import os
from pathlib import Path


paths = sorted(Path("./ready-files/").iterdir(), key=os.path.getmtime)
print(paths)