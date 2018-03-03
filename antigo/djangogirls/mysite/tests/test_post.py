from django.contrib.auth.models import User
from blog.models import Post
import pytest


@pytest.fixture
def user(db):
    user = User(username='foo', email='foo@bar.com', first_name='joao', 
    last_name='silva')
    

def test_can_make_post(db, user):
    post = Post(
        user=user,
        title='teset',
        text='dsfsdf sdfs d',
    )
    post.save()    
