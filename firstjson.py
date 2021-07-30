import json
f =open('firstprogram.py')
data =json.load(f)
for i in data['firstprogram_detail']:
  print(i)
  f. close()


