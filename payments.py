from fastapi import APIRouter

router = APIRouter()

@router.post("/payment/success")
def payment_success(user_id: int):
    # mark user paid in database
    return {"access":"granted"}
