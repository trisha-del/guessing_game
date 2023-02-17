cars = {
    "model":"ford",
    "year" :1998,
    "color":"purple",
    "country":"kenya"
}
# accessing dictionary items
print(cars["color"])
print(cars["model"])
print(cars["country"])
person ={
    "name":"tess",
    "age" :"18",
    "pets":{
        "dog":"x",
        "cat":"y"
    }
    }
print(person["pets"])

profile={}
profile["username"]="user123"
profile["age"]=20
profile["email"]="user123@gmail.com"
print(profile)

profile={}
def register():
    username=input("enter username")
    email=input("enter email")
    password=input("enter password:")
    profile["username"]=username
    profile["email"]=email
    profile["password"]=password
register()
def get_profile():
    print (profile)
def change_username():
    new_username=input("enter new user")
    profile["username"]=new_username
    


register()
get_profile()





