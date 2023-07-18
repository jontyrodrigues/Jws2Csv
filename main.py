import os
from extractor import Extractor


# read all files in jws folder
def main():
    for filename in os.listdir('JWS'):
        if filename.endswith('.jws'):
            print(filename)
            extractor = Extractor(filename)
            extractor.read_header()
            unpacked_data = extractor.read_data()
            csv_data = list(zip(*unpacked_data))
            with open('CSV/'+filename+'.csv', 'w') as f:
                for row in csv_data:
                    f.write(','.join(map(str, row)) + '\n')

if __name__ == '__main__':
    main()