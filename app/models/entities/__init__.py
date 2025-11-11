from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, UniqueIdProperty
from app.models.relations import FollowsRel, LikesRel

class User(StructuredNode):
    uid = UniqueIdProperty()
    username = StringProperty(unique_index=True)
    follows = RelationshipTo('User', 'FOLLOWS', model=FollowsRel)
    followers = RelationshipFrom('User', 'FOLLOWS')
    posts = RelationshipTo('Post', 'POSTED')
    likes = RelationshipTo('Post', 'LIKES', model=LikesRel)

class Post(StructuredNode):
    uid = UniqueIdProperty()
    content = StringProperty()
    liked_by = RelationshipFrom('User', 'LIKES', model=LikesRel)
