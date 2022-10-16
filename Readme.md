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

              >>sudo cp clipit.sh /bin/clipit.sh



  4.2 step 2: change clipit.sh permission to exexutable usig cmd 


             >> sudo chmod +x /bin/clipit.sh
             
             
  4.3 step 3: create a file path as follows
  
  
              >>"/home/clipboard/clipit.json"
          
          
          
  4.4 step 4: update the <path> in the clipit.sh file with the path where this repo is cloned 
  
              >> python3 <path>clipit.py $1
             
          

## 5.How to use

   5.1  To copy currently copied clipboard text to clipit use cmd 

      
      >>clipit.sh -key
    
    note: if you want you can change the file name clipit.sh in bin folder to your  desired name such as clipit or what fits you ,use that name to access     the extension

   5.2  key are 

    for saving "s"
    for copying from list "lo"
    for listing the keywords "ls"
    

### @By Amal krishna M U 
