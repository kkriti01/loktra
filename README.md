# Loktra

Install
----------------
pip install -r requirements.txt

Run webapps
-----------------------
python manage.py runserver
 
 enter url in browser http://www.localhost.com:8000/home/
 
---enter your key for query1 i.e getting total count for that key

---enter your key ,page for query2 i.e. getting total result on this specified page


Run Script
-----------------
#1.Scrapper.py
#Query_1 (i.e getting total count for that key)

 python manage.py scrapper.py key
 
#Query_2 (i.e. getting total result on this specified page)

 python manage.py scrapper.py key page
 
#2. uri.py
 
#Getting  details of uri
   
  python manage.py uri.py url

#Manipulating uri
  
  python manage.py url key value
  
#3.hash.py

# for getting reverse of a string
    python manage.py runserver
    
    ---prompt for string
    ---enter the string    
