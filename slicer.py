#!usr/bin/env python3

# pip install regex
import re

email=input(" Enter the Email:")
# spliting the email 

mail=re.split('@', email);print( "\n User name is  :" ,mail[0],"\n Domain name is :",mail[1])
