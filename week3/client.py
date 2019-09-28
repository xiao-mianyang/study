#!/usr/bin/env python3

import requests

user_info={'name':'shixiaolou','password':'abc123','hobbies':['code','swin']}

r = requests.post('http://localhost:5000/register',data=user_info)

print(r.text)


