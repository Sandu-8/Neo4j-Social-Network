from neomodel import StructuredRel, StringProperty, UniqueIdProperty

class FollowsRel(StructuredRel):
    since = StringProperty()
    uid = UniqueIdProperty()

class LikesRel(StructuredRel):
    since = StringProperty()
    uid = UniqueIdProperty()
