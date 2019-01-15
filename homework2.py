"""homework on functions"""



#functions with return

def Artist():
    name = "Octoppizo"
    return name

def Genre():
    name = "trap music"
    return name

def Texture():
    name = "Mezzo plano"
    return name
def Duration_time():
    name = 300.90
    return name
#calling each function and storing it in a variable to use it later if needed

artistname=Artist()
genrename=Genre()
texturename=Texture()
durationtime=Duration_time()

#printing the data which we get from the fanctions

print(artistname)
print(genrename)
print(texturename)
print(durationtime)
