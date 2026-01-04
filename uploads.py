from fastapi import UploadFile, Depends
from auth import get_user

async def upload(file: UploadFile, user=Depends(get_user)):
    if not user["is_admin"]:
        return {"error":"Not allowed"}

    with open(f"media/{file.filename}","wb") as f:
        f.write(await file.read())

    return {"status":"uploaded"}
