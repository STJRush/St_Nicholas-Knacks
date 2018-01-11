age_groups = ["0-4", "5-9", "10-12", "13-17", "18-59", "60->"]
type_of_person = ["Creative", "Car-Lover", "Thoughtful", "Trendy", "Music", "None of These"]
t_categories = ["Toys", "Clothes", "Lego"]
k_categories = ["Lego", "Clothes", "Toys", "Sports", "Bikes", "Creativity", "Devices"]
pt_categories = ["Clothes", "Lego", "Sports", "Bikes", "Creativity"]
te_categories = ["Clothes", "Sports", "Bikes", "Electronics", "Creativity"]
a_categories = ["Clothes", "Sports", "Vehicles", "Electronics", "Creativity"]
e_categories = ["Clothes", "Electronics"]
tb_creative = ["Aquadoodle Set", "Mega Bloks Big Building Bag", "Duplo- My Fist Cars and Trucks", "Duplo- Family House", "Duplo- Preschool Set"]
tg_creative = ["Aquadoodle Set", "Fashion Colour Books", "Mega Bloks Building Bag", "Duplo- All in One Gift Set", "Duplo- Disney Princess Castle", "Duplo- Minnie Mouse Bow Tique", "Disney Princess SnowGlobe Maker"]
tb_CarLover = ["Toy Cars", "Remote Control Cars", "Duplo- My First Cars and Trucks"]
tb_thought = ["Jigsaw", "Build-n-Learn Table"]
tg_thought = ["Jigsaw", "Build-n-Learn Table"]
tb_trendy = ["RainJackets", "Fancy Dress"]
tg_trendy = ["Dresses", "Fancy Dress"]
tb_music = ["Kid Instruments", "Musical Workbench"]
tg_music = ["Kid Instruments", "Musical Workbench"]
tb_toys = ["Kid Instruments", "Toy Cars", "Musical Workbench", "Jigsaw", "Aquadoodle Set", "Remote Control Cars", "Walkie Talkies", "Toy Animals", "JCB Tool Case"]
tg_toys = ["Picnic Basket", "PlayTent Castle", "Tea PartySet", "Aquadoodle Set", "Fashion Colour Books", "Toy Animals", "Fairy Gardens", "Hairdressing Kit", "Disney Princess SnowGlobe Maker"]
gender = ["Male", "Female"]
tb_clothes = ["Shirt with Bow Tie", "Puffer Jackets", "Pyjamas", "Suit Jacket", "Onesie", "SwimSuits", "WaistCoats", "RainJackets", "Fancy Dress", "Shoes"]
tg_clothes = ["Pyjamas", "Onesie", "SwimSuits", "RainJackets", "Skirts", "Dresses", "Fancy Dress", "Leggings", "Tights", "Shoes"]
tb_lego = ["Mega Bloks Big Building Bag", "Build-n-Learn Table", "Duplo- My First Cars and Trucks", "Duplo- Family House", "Duplo- Preschool Set"]
tg_lego = ["Mega Bloks Big Building Bag", "Build-n-Learn Table", "Duplo- All in One Gift Set", "Duplo- Disney Princess Castle", "Duplo-Minnie Mouse Bow Tique"]
kb_toys = ["Mini Drone for Kids", "Remote Control BMW", "Ultimate Wind-Up Robot Toy", "Interactive Talking World Map", "Robot Building Kit"]
kg_toys = ["Hair Chalk", "Zen Colouring Book", "Temporary Flash Tattoos", "Mini Drone for Kids", "Interactive Talking World Map", "No Crease Hair Ribbon Ties"]
kb_legos = ["Lego Creator: The Mighty Dinosaurs", "Lego Ninjago", "Lego City", "Lego Batman", "Lego Starwars", "Lego Speed"]
kg_legos = ["Lego Friends", "Lego Juniors", "Lego Disney", "Lego Disney Princess", "Banbao", "Lego Creator", "Lego City"]

kb_creative = ["Lego Creator: The Mighty Dinosaurs", "Lego Ninjago", "Lego City", "Lego Batman", "Lego Starwars", "Lego City"]

def Intro():
	print("-----------------------------------------------------------------------------------------------------------")
	print("\t\t\t\t\t\t\t\t\tWelcome to the Christmas Present Finder")
	print("Here we will give you a list of age groups, catagories for said age groups and presents for each age group")
	print("Just type in the age groups that are given to you, then the given categories, then the given presents!")
	print("-----------------------------------------------------------------------------------------------------------")

def Toddlers():
	print(gender)
	t_gender=input("Which are they? ")
	print(type_of_person)
	t_person=input("What kind of person are they? ")
	if t_gender == "Male" and t_person == "Creative":
		print(tb_creative)
		well=input("Is this what you were looking for? Yes or No. ")
		if well == "Yes":
			wanna=input("Do you want to check our other categories? Yes or No. ")
			if wanna == "Yes":
				ToddlerCategories()
			elif wanna == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	elif t_gender == "Female" and t_person == "Creative":
		print(tg_creative)
		well2=input("Is this what you were looking for? Yes or No. ")
		if well2 == "Yes":
			wanna2=input("Do you want to check our other categories? Yes or No. ")
			if wanna2 == "Yes":
				ToddlerCategories()
			elif wanna2 == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well2 == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	elif t_gender == "Male" and t_person == "Car-Lover":
		print(tb_CarLover)
		well3=input("Is this what you were looking for? Yes or No. ")
		if well3 == "Yes":
			wanna3=input("Do you want to check our other categories? Yes or No. ")
			if wanna3 == "Yes":
				ToddlerCategories()
			elif wanna3 == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well3 == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	elif t_gender == "Female" and t_person == "Car-Lover":
		print("Sorry we don’t have anything for this type of person\n\n")
		return Intro
	if t_gender == "Male" and t_person == "Thoughtful":
		print(tb_thought)
		well4=input("Is this what you were looking for? Yes or No. ")
		if well4 == "Yes":
			wanna4=input("Do you want to check our other categories? Yes or No. ")
			if wanna4 == "Yes":
				ToddlerCategories()
			elif wanna4 == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well4 == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	if t_gender == "Female" and t_person == "Thoughtful":
		print(tg_thought)
		well5=input("Is this what you were looking for? Yes or No. ")
		if well5 == "Yes":
			wanna5=input("Do you want to check our other categories? Yes or No. ")
			if wanna5 == "Yes":
				ToddlerCategories()
			elif wanna5 == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well5 == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	if t_gender == "Male" and t_person == "Trendy":
		print(tb_trendy)
		well6=input("Is this what you were looking for? Yes or No. ")
		if well6 == "Yes":
			wanna6=input("Do you want to check our other categories? Yes or No. ")
			if wanna6 == "Yes":
				ToddlerCategories()
			elif wanna6 == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well6 == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	if t_gender == "Female" and t_person == "Trendy":
		print(tg_trendy)
		well7=input("Is this what you were looking for? Yes or No. ")
		if well7 == "Yes":
			wanna7=input("Do you want to check our other categories? Yes or No. ")
			if wanna7 == "Yes":
				ToddlerCategories()
			elif wanna7 == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well7 == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	if t_gender == "Male" and t_person == "Music":
		print(tb_music)
		well8=input("Is this what you were looking for? Yes or No. ")
		if well8 == "Yes":
			wanna8=input("Do you want to check our other categories? Yes or No. ")
			if wanna8 == "Yes":
				ToddlerCategories()
			elif wanna8 == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well8 == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	if t_gender == "Female" and t_person == "Music":
		print(tg_music)
		well9=input("Is this what you were looking for? Yes or No. ")
		if well9 == "Yes":
			wanna9=input("Do you want to check our other categories? Yes or No. ")
			if wanna9 == "Yes":
				ToddlerCategories()
			elif wanna9 == "No":
				return Intro
			else:
				print("Please answer Yes or No. ")
		elif well9 == "No":
			print("Please check our categories then")
			ToddlerCategories()
		else:
			print("Please answer Yes or No. ")
	elif t_gender == "Male" and t_person == "None of These":
		ToddlerCategories()
	elif t_gender == "Female" and  t_person == "None of These":
		ToddlerCategories()
	else:
		print("Please answer Yes or No. ")
				
def ToddlerCategories():
	print(gender)
	t_gender2=input("Which are they? ")
	print(t_categories)
	t_choose=input("Choose a category. ")
	if t_choose == "Toys":
		if t_gender2 == "Male":
			print(tb_toys)
		elif t_gender2 == "Female":
			print(tg_toys)
	elif t_choose == "Clothes":
		if t_gender2 == "Male":
			print(tb_clothes)
		elif t_gender2 == "Female":
			print(tg_clothes)
	elif t_choose == "Lego":
		if t_gender2 == "Male":
			print(tb_lego)
		elif t_gender2 == "Female":
			print(tg_lego)
		
def Kids():
	print(type_of_person)
	k_person=input("What kind of person are they? ")
	print(gender)
	k_gender=input("Which are they? ")
	if k_gender == "Male" and k_person == "Creative":
		print(kb_creative)
	
def KidsCategories():
	print(gender)
	k_gender=input("Which are they? ")
	print(k_categories)
	k_choose=input("Choose a category. ")
	if k_choose == "Toys":
		if k_gender == "Male":
			print(kb_toys)
		elif k_gender == "Female":
			print(kg_toys)
	elif k_choose == "Clothes":
		if k_gender == "Male":
			print(kb_clothes)
		elif k_gender == "Female":
			print(kg_clothes)
	elif k_choose == "Lego":
		if k_gender == "Male":
			print(kb_lego)
		elif k_gender == "Female":
			print(kg_lego)
	elif k_choose == "Sports":
		if k_gender == "Male":
			print(kb_sports)
		elif k_gender == "Female":
			print(kg_sports)
	elif k_choose == "Bikes":
		if k_gender == "Male":
			print(kb_bikes)
		elif k_gender == "Female":
			print(kg_bikes)
	elif k_choose == "Creativity":
		if k_gender == "Male":
			print(kb_creativity)
		elif k_gender == "Female":
			print(kg_creativity)
	
def PreTeens():
	print(pt_categories)
	pt_choose=input("Choose a category. ")
	
def Teens():
	print(te_categories)
	te_choose=input("Choose a category. ")
	
def Adults():
	print(a_categories)
	a_choose=input("Choose a category. ")
	
def Elders():
	print(e_categories)
	e_choose=input("Choose a category. ")

Intro()
print("Type the exact number given. E.G '0-4'")
choose=input(age_groups)
if choose == "0-4":
	Toddlers()
elif choose == "5-9":
	Kids()
elif choose == "10-12":
	PreTeens()
elif choose == "13-17":
	Teens()
elif choose == "18-59":
	Adults()
elif choose == "60->" or choose == "60>":
	Elders()
