from .import blog


@blog.route('/')
def index():
    return 'flask app'
