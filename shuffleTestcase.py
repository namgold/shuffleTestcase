import os
import re
import random
import sys

sf = False
def init():
    global sf
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        pass
    else:
        sf = True if input("Shuffle testcase? (N): ").lower() in ['y','yes'] else False
        # sf = True if input("Shuffle testcase? (N): ").lower() in ['y','yes'] else False
init()

suiteLst = {"LexerSuite": 100, "ParserSuite": 200, "ASTGenSuite": 300, "CheckerSuite":400, "CheckSuite":400, 'CodeGenSuite':500}
files_in_test = os.listdir('./test')
for filename in files_in_test:
    if filename[:-3] in suiteLst:
        suite_content = open('./test/' + filename, 'r').read()
        header_pos = suite_content.find(':') + 2
        header = suite_content[:header_pos]
        body = suite_content[header_pos:]
        matches = re.findall(r"    def test_.*?,\s*\d{1,3}\)\)", body, re.DOTALL)
        print("Found", len(matches), "testcases in", filename)
        if sf: random.shuffle(matches)
        matches=matches[:100]
        suite_id = suiteLst[filename[:-3]]
        for pi, i in enumerate(matches):
            matches[pi] = re.sub(r",\s*\d+\s*\)\)", ", " + str(pi + suite_id) + "))", i)
        output=header + "\n\n".join(matches)
        open('./test/' + filename[:-3]+"_shuffled.py",'w').write(output)
        print(filename[:-3],"done")