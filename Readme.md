#  Multi-clipboard clipit 

using this python script you can save multiple data in clipboard in different tags and can access those data using tags when ever you wish .Now you can search through your clipboard with ease 


## 1.scripting languages used 

  1.1. Python   
  1.2. bash




## 2.for storing data

  2.1.json



## 3.pre-prerequisite

  3.1. python3  
  3.2. install clipboard python module (use cmd "pip install clipboard")    
  3.3. bash shell  





## 4.To run it in terminal directly (for linux distro)  

  4.1 step 1: move clipit.sh to /bin using cmd 

              >>sudo cp clipit.sh /bin/clipit



  4.2 step 2: change clipit.sh permission to exexutable usig cmd 


             >> sudo chmod 777 /bin/clipit
             
             
  4.3 step 3: create a file path as follows
  
  
              >>"/home/clipboard/clipit.json"
          
          
          
  4.4 step 4: update the <path> in the clipit.sh file with the path where this repo is cloned 
  
              >> python3 <path>clipit.py $1
             
          

## 5.How to use

   5.1  To copy currently copied clipboard text to clipit use cmd 

      
      >>clipit -key
    
  

   5.2  key are 

    for saving "s"
    for copying from list "lo"
    for listing the keywords "ls"
    for help "-h"
    

### @By Amal krishna M U 
  
  24-5-2023
