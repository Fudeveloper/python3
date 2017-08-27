import pymongo

client = pymongo.MongoClient('123.207.68.28',27017)
db = client.test
stu = db.stu
print( stu.find_one())
