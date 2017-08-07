import pymongo
client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

# path = 'C:/Users/samsung1/Desktop/test.txt'
# with open(path,'r') as f:
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         data = {
#             'index':index,
#             'line':line,
#             'words':len(line.split())
#         }
#         sheet_tab.insert_one(data)

# $lt/$lte/$gt/$gte/$ne .一次等价于 < / <= / > />=  l表示less g 表示 grester   e 表示 equal  n 表示 not
#for item in sheet_tab.find():
for item in sheet_tab.find({'words':{'$lte':2}}):
    #print(item['line'])
    print(item)