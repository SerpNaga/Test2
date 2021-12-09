from api import PetFriends

pf = PetFriends()
status, result = pf.get_api_key("elirichsss@mail.ru", "ala123456")
auth_key = result['key']
print(status, result, auth_key)

status, res = pf.post_api_create_pet(auth_key,"Шарик", "hellhound", 'longer than you')
print(status, " + ", res)

status, res = pf.get_api_pet_list(auth_key, "my_pets")
pet_id = res['pets'][0]['id']
pet_id2 = res['pets'][1]['id']
pet_id3 = res['pets'][2]['id']
print(status, res, "\n HHHHHHHHHHHH " + pet_id)

status, res = pf.delete_api_pet(auth_key, pet_id)
print(status, " + ", res)