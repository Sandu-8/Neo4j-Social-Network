from fastapi import APIRouter, HTTPException
from app.models.entities import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(username: str):
    user = User(username=username).save()
    return {"id": user.element_id, "username": user.username}

@router.get("/")
def get_users():
    users = User.nodes.all()
    return [{"id": u.element_id, "username": u.username, "uid": u.uid} for u in users]

@router.get("/{uid}")
def get_user(uid: str):
    try:
        user = User.nodes.get(uid=uid)
        return {
            "id": user.element_id,
            "username": user.username,
            "following": [{"id": u.element_id, "username": u.username} for u in user.follows.all()],
            "followers": [{"id": u.element_id, "username": u.username} for u in user.followers.all()]
        }
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/{uid}/follow/{target_id}")
def follow_user(uid: str, target_id: str):
    user = User.nodes.get(uid=uid)
    target = User.nodes.get(uid=target_id)
    user.follows.connect(target)
    return {"status": f"{user.username} now follows {target.username}"}
