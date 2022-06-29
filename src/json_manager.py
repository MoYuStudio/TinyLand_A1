
import json

class JsonManager:
    def __init__(self,path='json'):
        self.path = path
        self.read_data = {}

        self.lookup_table()
        self.read()

    def lookup_table(self):
        with open(self.path+'/lut.json','r') as f:
            self.lut_data = json.load(f)

        return self.lut_data

    def read(self):
        self.lut_data_list = list(self.lut_data.keys())
        for data_name in self.lut_data_list:
            with open(self.path+'/'+self.lut_data.get(data_name),'r') as f:
                self.read_data[data_name] = json.load(f)
        
        return self.read_data

    def write(self,write_data):
        self.write_data = write_data
        with open(self.path,'w') as f:
            dumps_data = json.dumps(self.write_data,indent=4,separators=(',',':'),ensure_ascii=False,skipkeys=True,sort_keys=False)
            f.write(dumps_data)

if __name__ == '__main__':
    jm = JsonManager()