import pyshark
import os
import time

def readfile(filei):
    r_file=[]
    f=pyshark.FileCapture(filei,display_filter='rtp')
    for i in f:
        try:
            r_file.append(i[3])
        except:
            pass
    f.close()
    return r_file
    
def control_int(s,c,n):
    ok=0
    while(ok==0):
            try:
               int(c)
               ok=1
            except:
               ok=0
               print("\n\033[31;1mInvalid Number \033[0m")
               print(s) 
               print("\nChoose the file number to listen (1-"+str(n)+") or 0 to exit")
               c=input("file: ")
    return c

def listen(s):
    n=len(source)
    m=n
    control=0
    stampa=""
    if(s=='3'):
        m=n+1
        s='2'
        control=1
    if(s=='2'):
        stampa="\n"+stampa+str(m)+" files found"+"\n"
        for l in range(1,n+1):
            stampa=stampa+str(l)+". "+fileo+str(l)+".wav"+"\n"
        if(control==1):
            stampa=stampa+str(m)+". "+fileo+".wav (Complete File)"
        print(stampa)  
        n=m
        print("\nChoose the file number to listen (1-"+str(n)+") or 0 to exit")
        chf=input("file: ")     
        chf=control_int(stampa,chf,n)
        while chf!='0' and (int(chf)<0 or int(chf)>n):
           print("\n\033[31;1mOut of range \033[0m")
           print(stampa)
           print("\nChoose the file number to listen (1-"+str(n)+") or 0 to exit")
           chf=input("file: ")
           chf=control_int(stampa,chf,n)
        while(chf!='0'):
           if(chf==str(n) and control==1):
               os.system('play '+fileo+'.wav')
           else:
               os.system('play '+fileo+str(chf)+'.wav')
           print(stampa)
           print("\nChoose the file number to listen (1-"+str(n)+") or 0 to exit")
           chf=input("file: ")
           chf=control_int(stampa,chf,n)
           while chf!='0' and (int(chf)<0 or int(chf)>n):
               print("\n\033[31;1mOut of range \033[0m")
               print(stampa)
               print("\nChoose the file number to listen (1-"+str(n)+") or 0 to exit")
               chf=input("file: ")
               chf=control_int(stampa,chf,n)
    if(s=='1'):
        os.system('play '+fileo+'.wav')
    
def def_source(r_file):
    source_list = []
    source=[]
    for i in r_file:
        source_list.append(i.ssrc)
    for c in source_list:
        if source_list.count(c)>=2 and source.count(c)==0:
            source.append(c)
    return source

def def_codec(r):
    codec_list=[]
    for indice in r:
            codec_list.append(indice.p_type)
    c=codec_list[1]
    codec_list=[]
    codec = {
        '0':'sox -t ul -r 8000 -c 1 temp.raw ', #PCMU
      #'3':'Codifica Non Disponibile', #GSM
        '8':'sox -t al -r 8000 -c 1 temp.raw ', #PCMA
      #'9':'Codifica Non Disponibile', #G722
      #'18':'Codifica Non Disponibile', #G729
            }
    com=codec.get(c,'Codec not available')
    return com

def decode(s,r,fileo,source,codec):                                               
    print("\t| Decode the voip call with source: "+source+" |")
    rtp_list = []
    raw_audio = open("temp.raw",'wb')
    for i in r:
        if(i.ssrc==source):
            if i.payload:
                rtp_list.append(i.payload.split(":"))
    for rtp_packet in rtp_list:
        packet = " ".join(rtp_packet)
        audio = bytearray.fromhex(packet)
        raw_audio.write(audio)
    codec=codec+fileo
    os.system(codec)
    if(s=='s'):
        print("\t| File wav created                             |")
    print("\t------------------------------------------------")
    os.system("rm temp.raw")

indice=1
outputfile=''
source=[]
mix=''
esiste=0
cancella=0
print("Choose an option: ")
print("1) one file")
print("2) multiple files")
print("3) both")
scelta=input("choice: ")
while scelta!='1' and scelta!='2' and scelta!='3':
    print("\n\033[31;1mInvalid choose \033[0m")
    print("Choose an option: ")
    print("1) one file")
    print("2) multiple files")
    print("3) both")
    scelta=input("choice: ")
filei=input("Input file (*.pcap only): ")
while esiste==0:
    while '.pcap' not in filei:
        print("\n\033[31;1mNo extension *.pcap \033[0m")
        filei=input("Input file (*.pcap only): ")
    try:
        f=open(filei)
        esiste=1
    except FileNotFoundError:
        print("\n\033[31;1mFile Not Found \033[0m")
        print("The acceptable files in the current directory are:\n")
        os.system("ls *pcap")
        esiste=0
        filei=input("\nInput file (*.pcap only): ")
print("\n\033[33;1mThe file name chosen below will be followed by default by .wav \033[0m")
fileo=input("Output file (without .wav): ")
while '(' in fileo or ')' in fileo:
    if('(' in fileo and ')' in fileo):
        print("\n\033[31;1mCharacters '(' and ')' are not allowed \033[0m")
   
    elif(')' in fileo):
        print("\n\033[31;1mThe character ')' is not allowed \033[0m")
    else:
        print("\n\033[31;1mThe character '(' is not allowed \033[0m")
    fileo=input("Output file (without .wav): ")
while '.wav' in fileo:
    print("\n\033[33;1m.wav not necessary \033[0m")
    continua=input("You still want to continue, your file will be called:" + fileo + ".wav (s/n)")
    while (continua!='s' and continua!='n' and continua!='S' and continua!='N'):
        print("\n\033[31;1mInvalid choose \033[0m")
        continua=input("You still want to continue, your file will be called:" + fileo + ".wav (s/n)")
    if(continua!='s'):
        fileo=input("\nOutput file (without .wav): ")
    else:
        break
print('\n')
if(scelta=='3'):
    sec=time.time()
    cancella=1
    scelta='1'
if(scelta=='1'):
    if(cancella==1):
        s='s'
    else:
        s='n'
    sec=time.time()
    print("1. Reading from the file "+filei)
    r=readfile(filei)
    print("2. Define the sources of voip call")
    source=def_source(r)
    print("3. Define the codec")
    codec=def_codec(r)
    print("4. ")
    print("\n\t--------------------DECODING--------------------")
    for so in source:
        outputfile=fileo+str(indice)+'.wav'
        indice=indice+1
        decode(s,r,outputfile,so,codec)
        mix=mix+outputfile+' '
    mix='sox -m '+mix+fileo+'.wav '
    print("\n")
    print("\t------------------------------------------------")
    spazi=45-(17+len(fileo))
    stringa="\t| File "+fileo+".wav created"
    for i in range(0,spazi):
        stringa=stringa+' '
    print(stringa+"|")
    print("\t------------------------------------------------")
    os.system(mix)
    if(cancella==0):
        indice=0
        for so in source:
            indice=indice+1
            outputfile=fileo+str(indice)+'.wav'
            os.system('rm '+outputfile)
    print("\n5. All operations completed\n\n")
    secd=time.time()
    ch=input("You want listen the created file? (S/N) ")
    while ch!="S" and ch!="s" and ch!="N" and ch!="n":
        print("\n\033[31;1mInvalid choice \033[0m")
        ch=input("You want listen the created file? (S/N) ")
    if(ch=="S" or ch=="s"):
        if(cancella==1):
            scelta='3'       
        listen(scelta)
if(scelta=='2'):
    sec=time.time()
    print("1. Reading from the file "+filei)
    r=readfile(filei)
    print("2. Define the sources of voip call")
    source=def_source(r)
    print("3. Define the codec")
    codec=def_codec(r)
    print("4. ")
    print("\n\t--------------------DECODING--------------------")
    for so in source:
        outputfile=fileo+str(indice)+'.wav'
        indice=indice+1
        decode('s',r,outputfile,so,codec)
    print("\n5. All operations completed\n\n")
    secd=time.time()
    ch=input("You want listen the created file? (S/N) ")
    while ch!="S" and ch!="s" and ch!="N" and ch!="n":
        print("\n\033[31;1mInvalid choice \033[0m")
        ch=input("You want listen the created file? (S/N) ")
    if(ch=="S" or ch=="s"):
        listen(scelta)  
print("\n\t\033[33;1mDecoding in "+str(round(secd-sec,2))+" seconds.\033[0m\n")  




