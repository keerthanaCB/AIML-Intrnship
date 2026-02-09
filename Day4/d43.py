raw_logs=['id01','id02','id03','id04','id05','id06','id07','id08','id01']
unique_users=set(raw_logs)
is_present='id05' in unique_users
print("Is id05 present?",is_present)
print("Original list length:",len(raw_logs))
print("unique users count:",len(unique_users))
print("unique user ids:",unique_users)