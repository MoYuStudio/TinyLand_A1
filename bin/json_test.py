
import json

with open('config.json','r') as f:
     j = json.load(f)

print(type(j))  # Output: dict
print(j.keys())

print(j['window']['size'][1])

j['window']['size'][1] = 1080

print(j['window'])

with open('config.json','w') as f:
    a = json.dumps(j,indent=4,separators=(',',':'),ensure_ascii=False,skipkeys=True,sort_keys=False)
    f.write(a)

