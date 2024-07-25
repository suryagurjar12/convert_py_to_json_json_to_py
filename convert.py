import json 
json.dumps

# python_data={
#     'name':'neeraj',
#     'quali':'m.tech',
#     'city_bhopal':True,
#     'blong_to_sgrl':False,
#     'activity':None
# }
json_data= '{"name": "neeraj", "quali": "m.tech", "city_bhopal": true, "blong_to_sgrl": false, "activity": null}'
print(json.loads(json_data))
# print (type(json.dumps(python_data)))