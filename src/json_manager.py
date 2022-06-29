
import os
import json

class JsonManager:
    def __init__(self,path='json',read_data={}):
        self.path = path
        self.read_data = read_data
        self.write_path = {}

        self.read()

    def read(self):
        path_folder = os.path.split(self.path)[-1] # 获取指定文件夹名
        for parent,dirnames,filenames in os.walk(self.path): # 遍历路径 parent:父目录 dirnames:子目录 filenames:文件
            for file_name in filenames: # 遍历文件列表
                folder_name = os.path.basename(parent) # 获取文件夹名
                var_name = (os.path.splitext(file_name))[0] # 拆解文件名 去除后缀
                with open(parent+'/'+file_name,'r') as f: # with 打开文件
                    if folder_name == path_folder: # 如果 当前文件夹名 == 指定文件夹名
                        self.write_path[var_name] = parent # 将 变量：文件路径 存入写入字典
                        self.read_data[var_name] = json.load(f) # 将文件内容加载到 read_data 文件名为 var_name
                    else: # 如果 当前文件夹名 != 指定文件夹名
                        self.write_path[folder_name+'_'+var_name] = parent # 将 文件夹名+_+变量：文件路径 存入写入字典
                        self.read_data[folder_name+'_'+var_name] = json.load(f) # 将文件内容加载到 read_data 文件名为 folder_name+'_'+var_name
            
        return self.read_data

    def write(self,data_name,write_data):
        with open(self.path+'/'+self.write_path+'/'+data_name,'w') as f:
            dumps_data = json.dumps(write_data,indent=4,separators=(',',':'),ensure_ascii=False,skipkeys=True,sort_keys=False)
            f.write(dumps_data)

if __name__ == '__main__':
    jm = JsonManager('data/json')
    print(jm.read_data)
    print(jm.write_path)