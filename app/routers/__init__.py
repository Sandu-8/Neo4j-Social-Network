from .users import router as users_router
from .posts import router as posts_router

all_routers = [
    users_router,
    posts_router
]
