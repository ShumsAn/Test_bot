data = {'name_user':'andrey','choleric':0,'melancholic':5,'sanguine':7,'phlegmatic':8,'number_v':1100}

values = [x for x in data.values() if x != data['name_user'] if x != data['number_v'] if x != 0]
keys = [x for x in data.keys() if x != 'name_user' if x != 'number_v' if data[f'{x}'] != 0]


print(values)
print(keys)

