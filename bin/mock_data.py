from app.db import config
from app.models.entities import User, Post, FollowsRel, LikesRel
import random
from datetime import datetime

def clear_db():
    """Clear all users and posts."""
    for post in Post.nodes.all():
        post.delete()
    for user in User.nodes.all():
        user.delete()
    print("Database cleared.")

def create_mock_data():
    """Generate 50 users, random posts, follows, likes."""
    users = []
    posts = []

    for i in range(1, 51):
        user = User(username=f"user{i}").save()
        users.append(user)

    for user in users:
        for j in range(random.randint(1, 3)):
            post = Post(content=f"Post {j+1} from {user.username}").save()
            user.posts.connect(post)
            posts.append(post)

    for user in users:
        others = [u for u in users if u != user]
        following = random.sample(others, k=random.randint(5, 15))
        for target in following:
            # Use StructuredRel to store 'since'
            user.follows.connect(target, {'since': datetime.now().isoformat()})

    for user in users:
        liked_posts = random.sample(posts, k=random.randint(1, 5))
        for post in liked_posts:
            user.likes.connect(post, {'since': datetime.now().isoformat()})

    print(f"Mock data created: {len(users)} users, {len(posts)} posts, follows, likes.")

def main():
    clear_db()
    create_mock_data()
