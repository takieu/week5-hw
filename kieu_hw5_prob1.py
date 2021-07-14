punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

words = input("Put in words and punctuations :")

no_punct = ""
for char in words:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)

