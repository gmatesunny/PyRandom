'''
Created on May 11, 2015
@author: kmehta1
'''

import os
import requests
import csv
import re
    
def rater(path, exclude):
    
    regex = re.compile('[^a-zA-Z ]')
    with open('Movies.csv','w') as raterfile:  
        fieldnames = ['Movie', 'Rating', 'Genre']
        writer = csv.DictWriter(raterfile, fieldnames=fieldnames)
        writer.writeheader()
        
        
        for root, dirs, filenames in os.walk(path, topdown=True):
            dirs[:] = [d for d in dirs if d not in exclude]
                    
            for filename in filenames:
                
                a = os.path.splitext(filename)                
                if a[1] not in [".avi",".mkv",".mp4", ".divx", ".mov", ".vob", ".wmv", ".mpeg", ".mpg", ""] or (a[0].lower()).find('sample') != -1:
                    continue
                year = ''
                found =  re.search('\d{4}',a[0])
                if found:
                    year = found.group()
                moviename = re.sub("\.", ' ',a[0].strip())
                moviename = regex.sub('',moviename.strip())
                moviename = re.sub('\s+','+', moviename)
                print moviename,":", year
                try:
                    r = requests.post("http://www.omdbapi.com/?t="+moviename+"&y="+year+"&plot=short&r=json")
                    moviedict =  r.json()
                    if moviedict["Response"] == "False":
                        writer.writerow({'Movie':a[0],'Rating':'N/A','Genre':'Change File Name'})                    
                        continue                    
                    writer.writerow({'Movie':a[0],'Rating':moviedict['imdbRating'],'Genre':moviedict['Genre']})
                except Exception as e:
                    print e
                    pass
                

if __name__ == '__main__':
#     rater('S:/in_eclipse/random/Sample',['TV Serials'])
    rater("./English_Movies",['TV Serials'])