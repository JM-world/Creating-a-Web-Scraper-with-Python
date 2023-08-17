player = {
    'name': 'nico',
    'age': 12,
    'alive': True,
    'fav_food': ["Pizza","Hamberger"]
}
print(player)
print(player.get("age"))
print(player.get("fav_food"))
print(player['fav_food'])
player.pop('age')
print(player)
player['xp'] = 1500
print(player)
player['fav_food'].append("noodle")
print(player['fav_food'])
