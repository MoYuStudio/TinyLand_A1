
import json

class JsonManager:
    def __init__(self,path):
        self.path = path

    def read(self):
        with open(self.path,'r') as f:
            self.read_data = json.load(f)
        
        return self.read_data

    def write(self,write_data):
        self.write_data = write_data
        with open(self.path,'w') as f:
            dumps_data = json.dumps(self.write_data,indent=4,separators=(',',':'),ensure_ascii=False,skipkeys=True,sort_keys=False)
            f.write(dumps_data)