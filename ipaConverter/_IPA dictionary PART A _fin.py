import os
import os.path
import re

#WIP search up dictionary foler, count files, open files one by one.



def rawARPAbet():
    directory = "dictionariesIPA/"
    
    all_dic = os.listdir(directory)

    print(all_dic)

    nah = 0
    for f in all_dic:
        nah += 1

    blankTXT = ''
    kek = 0

    thisusedToWork=""
    for f in all_dic:
        dic_list = open(str(directory + all_dic[kek]), 'r', encoding='utf-8') #utf-16-le #utf-8
  #      blankTXT += dic_list.read()
   ##     convertToUpper = dic_list.read()
        ###############print('HEYO')

        for line in dic_list:
            if not line.strip(): continue

            #z = re.sub(r'(\/)', r'~', line)
            #y = re.sub(r'(^.*?)(\s)(.*?)', r'\g<1>, \g<3>', z)
            y  = re.sub(r'(?!\/),.*', r'', line) #removes secondary pronacation from orginal dictionary file
            y = re.sub(r'(.*?)(\s)((\/).*?(\/))', r'\g<1>,  \g<3>', y)            
            
            
            x = y.split(',')
            a=x[0]
            
            b=x[1]
            a=a.upper()
            
            b = re.sub('\u200d', '', b) #removes that annoying symbol
            
            c=a+b
           ################## print(c)
           # c=re.sub(',', '   ')
            blankTXT += c
        blankTXT += "\n"        
        
        kek += 1
     #   print(c)

    print(dic_list)
    #print(blankTXT)
        
      #  if kek == nah:
          #print()
    ff = open('raw_IPA.txt', 'w', encoding='utf-8') #latin-1 #utf-8
    
    #convert small words to big words

    
    ff.write(blankTXT)
    ff.close()
    dic_list.close()
    print('raw_IPA.txt was successfuly created')
    
try:
    print('Do you wish to create new "raw_IPA.txt"? \nY or N')
    ######rawARPAbet()
    con1 = input()
    if (con1 == 'Y') or (con1 == 'y'):
        print('creating raw_IPA.txt, please wait ~30 seconds for code to complete')
        rawARPAbet()
        
    print("ART A complete, use PART B")

except:
    print("""raw_ARPAbet.txt do not exist or cannot be created,
          check if the folder 'dictionariesIPA' exist in same directory as
          PY file and if it contains text files (encode UTF-8)""")


