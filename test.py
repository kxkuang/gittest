#def test(info):
    #if info.username=="root"and info.passwd=="1223":
        #print("你有权限")
    #else:
        #print("你没有权限")
        #return
    #return"123"
#def test2(info):
    #if info.username=="root"and info.passwd=="1223":
      # print("你有权限")
    #else:
       #print("你没有权限")
     #  return
   # return"456"
#@permit
#def test2(info):
    #return"456"

#permit
#def test(info):
    #return"123"
------------------------------------------
def permit():
    def log(username,passwd):
        if username=="root"and passwd=="1223":
            print("你有权限")
        else:
            print("你没有权限")
            return
        return"123"

@permit()
def log(root,"1223"):
     return "123"

def test2(info):
    return"456"

def test(info):
    return"123"









