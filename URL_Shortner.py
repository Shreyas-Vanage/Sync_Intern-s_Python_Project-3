# Sync_Intern-s_Python_Project-3
import pyshorteners
l_url = input("Enter the URL to shorten: ")
 
#Using here pyshorterners / Tinyurl shortener service
a=pyshorteners.Shortener()
s_url=a.tinyurl.short(l_url)
 
print("The Shortened URL is : " + s_url)