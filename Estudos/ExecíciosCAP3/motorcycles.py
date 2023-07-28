motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('suzuki')
motorcycles.insert(0, 'ducati')
del motorcycles[0]
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
motorcycles.remove('ducati')