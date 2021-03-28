import uuid
uid = str(uuid.uuid4())
suid = ''.join(uid.split('-'))
print(uid,suid)