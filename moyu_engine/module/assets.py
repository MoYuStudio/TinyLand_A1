
import glob

class Assets:
    def __init__(self,path):
        self.path = path
        
    def one_folder(self):
        '''
            读取一个文件夹下的所有文件
        '''
        num = []
        for filename in glob.glob(r'tinyland/assets/tile/*.png'):
            num.append(filename)
        file_num = len(num)
        
        return file_num
        
        for parent,dirnames,filenames in os.walk(self.path):
            print(parent,dirnames,filenames)
            print(len(filenames))

if __name__ == '__main__':
    a = Assets('tinyland/assets/tile')
    print(a.one_folder())