import re

post = "Loving #Python and #Coding at #LkhibraAcademy!"

hashtags = re.findall(r'#\w+', post)

print(f"Hashtags : {hashtags}")