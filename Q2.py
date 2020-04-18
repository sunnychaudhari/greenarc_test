def show_dishes(input_str, dishes):
	if input_str == "vegitarian":
		final_dishes = [ each for each in dishes if not each.get("type")]
	elif input_str == "non-vegitarian":
		final_dishes = dishes
	else:
		final_dishes = []
	return final_dishes


dishes = [{"name":"Alu Gobi","price":"994.82"},{"name":"Alu Matar","price":"55.61"},
{"name":"Barfi","price":"374.40"},{"name":"Beef Vindaloo","price":"77.62","type":"non-veg"},
{"name":"Butter Chicken","price":"782.52","type":"non-veg"},{"name":"Carrot Halwa","price":"783.73"},
{"name":"Chaat Papri","price":"663.73"},{"name":"Cham-Cham","price":"567.28"},
{"name":"Chana Dal","price":"981.52"},{"name":"Chana Masala","price":"377.18"},
{"name":"Chapati","price":"397.65"},{"name":"Chicken 65","price":"850.09","type":"non-veg"},
{"name":"Chicken Biriyani","price":"617.17","type":"non-veg"},{"name":"Chicken Tikka","price":"63.01","type":"non-veg"},
{"name":"Chili Chicken","price":"575.83","type":"non-veg"},{"name":"Coriander Chutney","price":"633.36"},
{"name":"Dal Makhani","price":"834.69"},{"name":"Date Tamarind Chutney","price":"709.57"},
{"name":"Dhokla","price":"106.84"},{"name":"Gulab Jamun","price":"893.48"},
{"name":"Idili","price":"154.59"},{"name":"Jalebi","price":"344.13"},
{"name":"Mutton Kheema","price":"100.57","type":"non-veg"},{"name":"Kheer","price":"839.09"},
{"name":"Kulfi","price":"409.05"},{"name":"Laddu","price":"547.87"},
{"name":"Chicken Kebabs","price":"786.17","type":"non-veg"},{"name":"Chicken Vindaloo","price":"999.93","type":"non-veg"},
{"name":"Lime Pickle","price":"539.86"},{"name":"Veg Balls With Sauce","price":"819.44"},
{"name":"Mango Lassi","price":"318.21"},{"name":"Masala Chai","price":"112.89"},
{"name":"Masala Dosa","price":"730.88"},{"name":"Masoor Dal","price":"848.79"},
{"name":"Medu Vada","price":"952.15"},{"name":"Naan","price":"883.85"},
{"name":"Missal Pav","price":"138.18"},{"name":"Onion Pakora","price":"971.00"},
{"name":"Papadum","price":"535.06"},{"name":"Egg Pulao","price":"472.54","type":"non-veg"}]

input_str = raw_input("Are you vegetarian or non-vegitarian? : \n") 
final_dishes = show_dishes(input_str, dishes)
print "================Menu================"
if final_dishes:
	for each in final_dishes:
		print final_dishes.index(each)+1,". ", each.get("name")," - Rs.",each.get("price")
else:
	print "Sorry couldn't find menu !"

