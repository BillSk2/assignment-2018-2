import sys
import pprint
path=sys.argv[1]
lat=[]
#ΑΝΟΙΓΜΑ ΑΡΧΕΙΟΥ ΚΑΙ ΔΗΜΙΟΥΡΓΙΑ ΠΙΝΑΚΑ
with open(path) as input_file:
    for line in input_file:
        line=line.replace(",","")
        line=line.rstrip('\n')
        parts=line.split()
        #print(parts)
        lat.append(parts)
pprint.pprint(lat)
#ΔΕΙΚΤΗΣ ΓΡΑΜΜΗΣ
i=0
#ΔΕΙΚΤΗΣ ΣΤΗΛΗΣ
j=0
#ΑΡΙΘΜΟΣ ΜΟΝΟΠΑΤΙΩΝ ΠΟΥ ΠΡΕΠΕΙ ΝΑ ΒΡΕΘΟΥΝ(ΜΠΟΡΕΙ ΝΑ ΕΙΝΑΙ ΚΑΙ ΜΙΚΡΟΤΕΡΟΣ )
#ΚΑΛΥΤΕΡΑ ΜΕ FOR ΑΝΤΙ ΓΙΑ WHILE
n=len(lat)-2
#ΑΡΙΘΜΟΣ ΜΟΝΟΠΑΤΙΩΝ
nt=0
#ΛΙΣΤΑ ΜΕ ΤΑ ΜΟΝΟΠΑΤΙΑ
trans=[]
#ΠΡΕΠΕΙ ΝΑ ΠΗΓΑΙΝΕΙ ΣΕ ΚΑΘΕ ΓΡΑΜΜΗ ΤΟΥ ΠΙΝΑΚΑ
while(i<len(lat)):
    print("arithmos i=",i)
    #ΔΕΙΚΤΗΣ ΠΙΘΑΝΟΥ ΜΟΝΟΠΑΤΙΟΥ ΓΙΑ ΚΑΘΕ ΓΡΑΜΜΗ
    d=0
    while(d<n):
        print("arithmos d=",d)
        #ΠΙΝΑΚΑΣ ΓΡΑΜΜΩΝ ΓΙΑ ΚΑΘΕ ΠΙΘ ΜΟΝΟΠΑΤΙ
        #ΑΡΧΙΚΟ ΣΤΟΙΧΕΙΟΥ ΜΟΝΟΠΑΤΙΟΥ ΓΙΑ ΚΑΘΕ ΓΡΑΜΜΗ
        k=lat[i][0]
        #ΓΙΑ ΚΑΘΕ ΠΙΘΑΝΟ ΜΟΝΟΠΑΤ(!!!!)
        pgr=[]
        gr=i
        pgr.append(gr)
        #ΠΙΝΑΚΑΣ ΠΙΘΑΝΩΝ ΜΟΝΟΠΑΤΙΩΝ
        pnt=[]
        pnt.append(k)
        #ΔΕΝ ΘΥΜΑΜΑΙ
        tra=[]
        tra.append(k)
        j=1
        #ΓΙΑ ΚΑΘΕ ΣΤΗΛΗ
        while(j<len(lat)):
            print("arithmos j=",j)
            #ΔΕΙΚΤΗΣ ΓΡΑΜΜΗΣ
            l=0
            #pinakas=[]
            #ppinakas=[]
            #ΔΙΑΣΧΙΣΗ ΓΡΑΜΜΗ ΓΡΑΜΜΗ
            while l<len(lat):
                print("arithmos l=",l)
                #ΕΑΝ ΤΟ Η ΓΡΑΜΜΗ ΔΕΝ ΕΧΕΙ ΔΕΣΜΕΥΘΕΙ
                if l not in pgr:
                    print("Grammes")
                    pprint.pprint(pgr)
                    #ΕΑΝ ΤΟ ΣΤΟΙΧΕΙΟ ΔΕΝ ΕΧΕΙ ΔΕΣΜΕΥΘΕΙ
                    if lat[l][j] not in pnt:
                        #ΠΡΩΤΟ ΠΙΘΑΝΟ ΜΟΝΟΠΑΤΙ
                        if d==0:
                            print(lat[l][j])
                            print("PINAKAS")
                            pprint.pprint(pnt)
                            print("TRANS")
                            pprint.pprint(trans)
                            #pinakas.append(pnt)
                            #pinakas.append(pgr)
                            #print("pinaks")
                            #pprint.pprint(pinakas)
                            #ppinakas.append(pinakas[-1])
                            print("Vazo to=",lat[l][j])
                            tra.append(lat[l][j])
                            pnt.append(lat[l][j])
                            pgr.append(l)
                            print("Neos Pinakas")
                            pprint.pprint(pnt)
                            print("Neees Grammes")
                            pprint.pprint(pgr)
                            l=1000
                            #print("pinaaaakas")
                            #pprint.pprint(ppinakas)
                        else:
                            #ΓΙΑ d!=0
                            if trans[nt-1][j]!=lat[l][j]:
                                print(lat[l][j])
                                print("PINAKAS")
                                pprint.pprint(pnt)
                                print("TRANS")
                                pprint.pprint(trans)
                                #pinakas.append(pnt)
                                #pinakas.append(pgr)
                                #print("pinaks")
                                #pprint.pprint(pinakas)
                                #ppinakas.append(pinakas[-1])
                                print("Vazo to=",lat[l][j])
                                tra.append(lat[l][j])
                                pnt.append(lat[l][j])
                                pgr.append(l)
                                print("Neos Pinakas")
                                pprint.pprint(pnt)
                                print("Neees Grammes")
                                pprint.pprint(pgr)
                                l=1000
                                #print("pinaaaakas")
                if l==len(lat)-1:
                    tra.append("e")
                print("allazo grammi",l+1)                #pprint.pprint(ppinakas)
                l=l+1
            print("allazo stili",j+1)
            j=j+1
        print("allazo monopati gia ton idio arithmo",nt+1)
        nt=nt+1
        trans.append(tra)
        print("allazo monopati",d+1)
        d=d+1
    print("allazo arxiko arithmo",i+1)
    i=i+1

pprint.pprint(trans)
Trans=[]
for x in trans:
    if 'e' not in x:
        Trans.append(x)
print("telikoo")
pprint.pprint(Trans)
lat=[]
i=0
k=0
for x in Trans:
    while i<len(lat):
        dval=True
        while k<len(lat):
            if Trans[i][k]==x[k]:
                dval=False
            k=k+1
        if dval:
            lat[x].append(Trans[i])
            print("AAAA")
        
    

#
pprint.pprint(lat)
#ss=()
#lati=[]
#for x in lat:
 #   ss=x
 #   ss=set(ss)
  #  lati.append(ss)
#print("jjjj")
#latin=set(lati)
#pprint.pprint(latin)
