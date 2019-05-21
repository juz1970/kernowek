#!/usr/bin/python3.6

#Author: J T Roberts

import re, cgi, cgitb; cgitb.enable()

def mutation():
    a1=[i for i, xx in enumerate(glist2) if xx == ('(f),')]

    try:
        for i in range(len(glist1)):
            mut1=(glist1[a1[i]])
            fnoun=(mut1[0])
            if fnoun in mutlist1:
                word1=(mut1[0:(len(mut1))])
                mut2= ( smut[(mutlist1.index(fnoun))] + (mut1[1:(len(mut1))]))
                if word1 in f:
                    a2=(f.index(word1))
                    if e[a2-1] == 'art,':
                        f.pop(a2)
                        f.insert(a2,mut2)
    except:
        IndexError
    a2=[i for i, zz in enumerate(f) if zz == ('ha')]
    for z in range(len(a2)):
        a3=a2[z]+1
        a4=(f[a3])
        if a4[0] in vowels:
            f.pop(a3-1)
            f.insert(a3-1,'hag')

def get(a):
    
    try:
        x=0
        b=a.split()
        length=len(b)
        while(x<length):
            if(b[x]=='a'):
                b.remove(b[x])
                length=length-1  
                continue
            x+=1
        for y in range(len(b)):
            c=b.pop(0)
            match(c)
    except:
        AttributeError

def match(c):

    txt=open('glossary.txt','r', encoding='utf-8')

    global lines
    for lines in txt:

        if re.match(c, lines,re.IGNORECASE):
            c=((lines).split('.')[0])
            global d
            d=list(c.split())
            e.append(d[1])
            f.append(d[2])
            break

    txt.close()

    if d[1]=='n,':
        glist1.append(d[2])
        glist2.append(d[3])
     
def transform():

    a0=list(enumerate(e))

    try:
        for i in range(len(e)-1):
            if 'adj,' in a0[i] and 'n,' in a0[i+1]:
                b1=f.pop(i)
                b2=e.pop(i+1)
                f.insert(i+1,b1)
                e.insert(i,b2)

            if 'art,' in a0[i] and 'n,' in a0[i+1] and 'vb,' in a0[i+2]:
                c1=f.pop(i+2)
                c2=e.pop(i+2)
                f.insert(i,c1)
                e.insert(i,c2)

            if 'art,' in a0[i] and 'n,' in a0[i+1] and 'vb,' in a0[i+2] and 'adj,' in a0[i+3]:

                d1=f.pop(i+3)
                d2=e.pop(i+3)
                f.insert(i,d1)
                e.insert(i,d2)
                
            if 'n,' in a0[i] and 'n,' in a0[i+1]:
                e1=f.pop(i)
                e2=e.pop(i+1)
                f.insert(i+1,e1)
                e.insert(i,e2)
    except:
        IndexError
		
def main():

    form = cgi.FieldStorage()
    a = form.getvalue('chars')
   
    if a == None:
        a=''
    elif a != None:

        get(a)
        transform()
        mutation()
        
    print('<font size="+0.7">Enter English text / Entra tekst Sowesnak:<br><form name="f" action="http://www.knok.cymru/cgi-bin/test.py" method="post"><textarea name="chars" rows="10" cols="50">'+a+'</textarea><br><br><input type="submit" value="Treylya / Translate";><br>')

    print('<br><font size="+0.7">Treylyans Kernewek / Cornish translation:<br><textarea name="chars" rows="10" cols="50">'+' '.join(f)+'</textarea></font></form></font><br>')

print("Content-Type: text/html\n\n")

print('<html><head></head><body><img src="http://www.knok.cymru/knok.jpg" alt="no image"><br><font size=".5">Medhelweyth treylyans yeth Sowesnak/Kernewek</font><br><font size=".5">English/Cornish language translation software</font></body></html><br><br>')

glist1=[]
glist2=[]                                                
e=[]
f=[]

mutlist1=['b','c','k','ch','d','g','gw','m','p','t']
smut=['v','g','g','j','dh','w','w','v','b','d']
amut=['b','c','h','ch','d','g','gw','m','f','th']
hmut=['p','c','k','ch','t','k','kw','m','p','t']
mmut=['f','c','k','ch','t','hw','hw','f','p','t']
vowels=['a','e','i','o','u','w','y','h']

main()

glist1=[]
glist2=[]
e=[]
f=[]






