from fastapi import APIRouter, HTTPException
from app.models.entities import User, Post

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/{user_uid}")
def create_post(user_uid: str, content: str):
    try:
        user = User.nodes.get(uid=user_uid)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")

    post = Post(content=content).save()
    user.posts.connect(post)
    return {"uid": post.uid, "content": post.content}

@router.post("/{user_uid}/like/{post_uid}")
def like_post(user_uid: str, post_uid: str):
    try:
        user = User.nodes.get(uid=user_uid)
        post = Post.nodes.get(uid=post_uid)
    except (User.DoesNotExist, Post.DoesNotExist):
        raise HTTPException(status_code=404, detail="User or Post not found")

    user.likes.connect(post)  # duplicate likes are ignored by Neomodel
    return {"status": f"{user.username} liked post {post.uid}"}

@router.post("/{user_uid}/unlike/{post_uid}")
def unlike_post(user_uid: str, post_uid: str):
    try:
        user = User.nodes.get(uid=user_uid)
        post = Post.nodes.get(uid=post_uid)
    except (User.DoesNotExist, Post.DoesNotExist):
        raise HTTPException(status_code=404, detail="User or Post not found")

    user.likes.disconnect(post)
    return {"status": f"{user.username} unliked post {post.uid}"}

@router.get("/{post_uid}/likes")
def get_likes(post_uid: str):
    try:
        post = Post.nodes.get(uid=post_uid)
    except Post.DoesNotExist:
        raise HTTPException(status_code=404, detail="Post not found")

    liked_by = post.liked_by.all()  # users who liked the post
    return [{"uid": u.uid, "username": u.username} for u in liked_by]
