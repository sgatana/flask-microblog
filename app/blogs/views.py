from . import blog
from app.models import User, Post


@blog.route('/')
def index():
    # user = User.query.all()
    # name = user.username
    return 'flask app'
