import sys
import json
import datetime

print(json.load(sys.stdin)["createdAt"])




#print(datetime.datetime.fromtimestamp(1398703304).strftime('%Y-%m-%d %H:%M:%S'))