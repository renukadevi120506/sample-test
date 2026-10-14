myd={
    "name":"red",
    "age":29,
    "loc":"Italy",
    "enroll": 23
}
#print (dir(myd))
#print(help(myd))

print(myd.get("name"))

if myd.get("Edu"):
    print("Exist")

else:
    print("Not Exist")

myd.update({"blood_group":"O+ve"})
print(myd)


keys=myd.keys()
print(keys)

val=myd.values()
print(val)

item=myd.items()
print(item)
