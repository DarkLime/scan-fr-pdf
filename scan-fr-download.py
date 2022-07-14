from fpdf import FPDF
import requests
import os
name= "onepeice_chap_1053_6"
fform = ".jpg"
folname = "onepeice_chap_1053_6"
nameform = "0"
os.makedirs(folname)
os.chdir(folname)
# URL of the image not of the page 
url = "https://cdn.statically.io/img/opfrcdn.xyz/uploads/manga/one-piece/chapters/1053.6/"

def toPDF(filename, list):
    pdf = FPDF()
    for image in list:
        pdf.add_page()
        pdf.image(image,0,0,210)
    pdf.output(filename+".pdf", "F")
    
    
def error(i,req):
    if req.status_code == 200:
        return 0
    else:
        if i < 10:
            fname = nameform+str(i)+"-"+str(i+1)
            fullfname = fname+fform
            tmplink = url
            tmplink += fullfname
            req = requests.get(tmplink)
        else:
            fname = nameform[0:len(nameform)-1]+str(i)+"-"+str(i+1)
            fullfname = fname+fform
            tmplink = url
            tmplink += fullfname
            req = requests.get(tmplink)
        if req.status_code == 200:
            return 1
        else: 
           return 3


def download0x() :
    i = 1
    tmplink = url
    lstImg = []
    while 0<5 : 
        if i < 10:
            fname = nameform+str(i)
            fullfname = fname+fform
            tmplink = url
            tmplink += fullfname   
        else:
            fullfname = nameform[0:len(nameform)-1]+str(i)+fform
            tmplink = url
            tmplink += fullfname
        print(tmplink)


        r = requests.get(tmplink)


        err = error(i,r)
        if err == 0:
            i=i+1
            lstImg.append(fullfname)
            open(fullfname, 'wb').write(r.content)
        elif err == 1 :
            if i < 10:
                fname = nameform+str(i)+"-"+str(i+1)
                fullfname = fname+fform
                tmplink = url
                tmplink += fullfname
                r = requests.get(tmplink)
            else:
                fname = nameform[0:len(nameform)-1]+str(i)+"-"+str(i+1)
                fullfname = fname+fform
                tmplink = url
                tmplink += fullfname
                r = requests.get(tmplink)
            i=i+2
            lstImg.append(fullfname)
            open(fullfname, 'wb').write(r.content)
        else:
            toPDF(name,lstImg)
            break
        


download0x()