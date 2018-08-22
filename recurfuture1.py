from __future__ import absolute_import
import os
for root, dirs, files in os.walk("/home/erik/omf"):
    for file in files:
        if file.endswith(".py"):
             #print(os.path.join(root, file))
             file_to_convert = os.path.join(root, file)
             os.system("futurize --stage1 -w " + file_to_convert)