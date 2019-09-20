import os
import re
import random

files_in_test = os.listdir('./test')
for i in files_in_test:
    if i[-8:] == "Suite.py":
        filename = './test/'+i
        suite_content = open(filename, 'r').read()
        header_pos = suite_content.find(':') + 2
        header = suite_content[:header_pos]
        body = suite_content[header_pos:]
        matches = re.findall(r"    def test_.*?,\s*\d{1,3}\)\)", body, re.DOTALL)
        random.shuffle(matches)
        matches=matches[:100]
        try: suite_id = int(matches[0][-5:-4]) * 100
        except: suite_id = 0
        for pi, i in enumerate(matches):
            matches[pi] = re.sub(r",\s*\d+\)\)", ", " + str(pi + suite_id) + "))", i)
        output=header + "\n".join(matches)
        open(filename[:-3]+"_shuffled.py",'w').write(output)

print("Shuffle done")