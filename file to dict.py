dic={}
with open("pavani.txt")as f:
    for i in f:
        key,desc=i.strip().split(None,1)
        dic[key]=desc.strip()