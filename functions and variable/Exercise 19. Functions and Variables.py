def cheese_and_crackers(cheese_count,boxes_of_cracker):
	print(f"You have {cheese_count} cheese!")
	print(f"You have {boxes_of_cracker} boxes_of_cracker")
	print("Man taht's enough for party!")
	print("Get a blanket.\n")

print("WE can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amt_of_cheese=10
amt_of_Crack=50

cheese_and_crackers(amt_of_cheese,amt_of_Crack)

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

print("And we can combine the two, variables snd math:")
cheese_and_crackers(amt_of_cheese+100,amt_of_Crack+1000)
