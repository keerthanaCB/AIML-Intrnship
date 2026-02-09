friend_a={"python","cooking","Hiking","moive"}
friend_b={"Hiking","gaming","photography","python"}
common_intrests=friend_a & friend_b
all_intrests=friend_a | friend_b
unique_to_a=friend_a - friend_b
print("common intrests:",common_intrests)
print("all intrests:",all_intrests)
print("intrests unique to friend A:",unique_to_a)