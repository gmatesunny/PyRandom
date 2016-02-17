'''
Created on 23-May-2014

@author: roshan
'''
import os
def renamer(dirname):
    for root,dirs,files in os.walk(dirname):
        for onefile in files:
            org = os.path.join(root,onefile)
            name = str(onefile).split('.')[0]
            os.rename(org, org+'_Answer')         
if __name__ == '__main__':
    renamer(r'/home/roshan/Downloads/ManhattanGREPrepOnlineChallengeProblemArchive/Answers')
