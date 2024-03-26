import base64

a = "안녕하세요!"

result = a.encode("utf-8")

result = base64.b64encode(result)



print(result)