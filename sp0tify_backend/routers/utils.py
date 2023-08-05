from fastapi import HTTPException

async def verify_query(q: str):
    if q == "" or q == None:
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    print(f"q: {q}")

async def verify_id(id: int):
    if id == None:
        raise HTTPException(status_code=400, detail="ID cannot be empty")
    elif id < 0:
        raise HTTPException(status_code=400, detail="ID cannot be negative")
    elif id == 0:
        raise HTTPException(status_code=400, detail="ID cannot be 0")
    elif type(id) != int:
        raise HTTPException(status_code=400, detail="ID must be an integer")
    print(f"id: {id}")
