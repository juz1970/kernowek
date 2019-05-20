#!/usr/bin/python3.6

#Author: J T Roberts

import cgi, cgitb; cgitb.enable()

def mutations():

    for i in range(len(d)-1):
        if 'art' in e[i] and 'n' in e[i+1] and 'f' in g[i+1]:
            aa1=d.pop(i+1)
            if aa1[0] in mutlist1:
                aa2=(( smut[(mutlist1.index(aa1[0]))] ))
                aa3=(aa2+aa1[1:])
                d.insert(i+1,aa3)
        
    for i in range(len(d)-1):
        if ('ha' in d[i]):
            if (d[i+1][0]) in vowels:
                d.pop(i)
                d.insert(i,'hag')

def get(a):
  
    try:
        b=a.split()
        x=0
        length=len(b)
		
        while(x<length):
            if b[x] == 'a':
                b.remove(b[x])
                length=length-1
                continue
            x=x+1

        for i in range(length):
            c=b.pop(0)
            match(c)

    except:
        AttributeError



def match(c):
    #gloss=open("http://www.knok.cymru/cgi-bin/gloss2.txt", "r")
    aa=['woman','benyn','man','den','and','ha','the','an','small','bian','is','yma']
    bb=['woman','n','f','man','n','m','and','cnj','n','the','art','n','small','adj','n','is','vb','n']

    if c in aa and bb:
        aa1=(aa[(aa.index(c))+1])
        aa2=(bb[(bb.index(c))+1])
        aa3=(bb[(bb.index(c))+2])
    e.append(aa2)
    d.append(aa1)
    g.append(aa3)
   
def transform():
    
    try:
        for i in range(len(e)-1):
    
            if 'adj' in e[i] and 'n' in e[i+1]:
                b1=d.pop(i)
                b2=g.pop(i)
                d.insert(i+1,b1)
                g.insert(i+1,b2)
           

            if 'art' in e[i] and 'n' in e[i+1] and 'vb' in e[i+2]:
                c1=d.pop(i+2)
                c2=g.pop(i+2)
                d.insert(i,c1)
                g.insert(i,c2)
            

            if 'art' in e[i] and 'n' in e[i+1] and 'vb' in e[i+2] and 'adj' in e[i+3]:
            	d1=d.pop(i+3)
            	d2=g.pop(i+3)
            	d.insert(i,d1)
            	g.insert(i,d2)
            
           
    except:
        IndexError

    mutations()


def main():

    form = cgi.FieldStorage()
    a = form.getvalue('chars')
   
    if a == None:
        a=''
  
    get(a)
    transform()

    print('<font size="+0.7">Enter English text / Entra tekst Sowesnak:<br><form name="f" action="http://www.knok.cymru/cgi-bin/test.py" method="post"><textarea name="chars" rows="10" cols="50">'+a+'</textarea><br><br><input type="submit" name="submit" value="Treylya / Translate";><br>')

    print('<br><font size="+0.7">Treylyans Kernewek / Cornish translation:<br><textarea name="chars" rows="10" cols="50">'+(' '.join(d))+'</textarea></font></form></font><br>')
    
mutlist1=['b','c','k','ch','d','g','gw','m','p','t']
smut=['v','g','g','j','dh','w','w','v','b','d']
amut=['b','c','h','ch','d','g','gw','m','f','th']
hmut=['p','c','k','ch','t','k','kw','m','p','t']
mmut=['f','c','k','ch','t','hw','hw','f','p','t']
vowels=['a','e','i','o','u','w','y','h']


print("Content-Type: text/html\n\n")

print('<html><head></head><body><img src="http://www.knok.cymru/knok.jpg" alt="no image"><br><font size=".5">Medhelweyth treylyans yeth Sowesnak/Kernewek</font><br><font size=".5">English/Cornish language translation software</font></body></html><br><br>')

d=[]
e=[]
g=[]
h=[]

main()

d=[]
e=[]
g=[]
h=[]






