import os
import time
import re
import linecache

to_file='temp.log'
from_date = '2019-07-22 23:59:00'
to_date = '2019-07-22 23:59:59'
regexString = r"(\[\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}\])"
pq = re.compile(regexString, re.I)
isBetween = False

def get_content(path):
    global isBetween
    if os.path.exists(path):
        content = ''
        cache_data = linecache.getlines(path)
        for line in range(len(cache_data)):  
            mat = pq.search(cache_data[line])
            if mat is None: 
                if isBetween is False:
                    continue
                else: 
                    content += cache_data[line]
            else:
                date = mat.group(0).strip('[]')
				 
                if date >= from_date and date <= to_date:
                    isBetween = True
                    content += cache_data[line]
                elif date > to_date: 
                    isBetween = False
                    
        return content
    else:
        print('the path [{}] is not exist!'.format(path))

def main():
    path = 'aa.log'
    start =  time.time()
    content = get_content(path)
    with open(to_file, 'a') as file_:
        file_.write(content)

    seconds = time.time() - start
    print(seconds)

if __name__ == '__main__':
    main()
