# Module that is responsible for analyzing and getting statistical results from shakespeare.txt file
# about letter frequency, total number of words, number of unique words and five most common words
# along with the words that most commonly follow them

import sys
import re
import os.path
import pandas as pd
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
from collections import Counter

def main():
    if len(sys.argv[1]) >= 1:                                       # sys.argv[1] means the argumetns ; check whether at least entered one argument
        if os.path.isfile(sys.argv[1]):                             # os.path.isfile is used to check whether the specified path is an existing file or not 
            header = " Voltage, WL1, WL2, WL3, WL4, WL5, NTC, EC, Time, Percentage"
            with open("output_data.txt", "w") as out: 
                print(header+ "\r\n")                
                out.write(header + "\r\n")
                with open(sys.argv[1], "r") as file:
                    line = file.readline()
                    while line != '':
                        search_word(line, out)
                        # print(output_data) 
                        line = file.readline()
        else:
            print("The file does not exist!")
            sys.exit(1)
    else:
        print("No argument provided. Please provide at least the shakespeare.txt.")
        sys.exit(1)

def search_word(line, out):
    # substring = re.search("<ADC>(.+?)</ADC>", doc)
    # regex = re.compile(r'<ADC>(.+-*.*)</ADC>')
    regex = re.compile(r"<ADC>(.*)</ADC>")
    match = regex.search(line)
    if match:
        output_data = match.group(1)
        output_data += "\r\n"            
        print(output_data)
        out.write(output_data)

        # with open('output_data.txt', 'w') as fhandle:
        #     for line in output_data:
        #         fhandle.write(f'{line}\n')

        # TESTDATA = StringIO(output_data)
        # print(TESTDATA)  
        # df = pd.read_csv(TESTDATA)
        # print(df)  
        # df.to_csv(r'/Users/ricky/Desktop/output.csv', index = True, header = True)
    # else:
    #     print('x')

if __name__ == '__main__':
    main()