try:
   fh = open("nyc_airlines", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
   print("KISHAN KISHAN KISHAN")
else:
   print ("Written content in the file successfully")
   
