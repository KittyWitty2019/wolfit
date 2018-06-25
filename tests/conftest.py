import pytest
from app import db
from app.models import User, Post
from random import randint

USERNAME = "john"
PASSWORD = "yoko"


@pytest.fixture
def test_user():
    u = User(username=USERNAME, email="john@beatles.com")
    u.set_password(PASSWORD)
    db.session.add(u)
    db.session.commit()
    return u


@pytest.fixture
def single_post():
    user = db.session.query(User).filter_by(username=USERNAME).first()
    if user is None:
        user = test_user()
    p = Post(title="First post", body="Something saucy", user_id=user.id)
    db.session.add(p)
    db.session.commit()
    return p


@pytest.fixture
def random_post():
    username = f"user-{randint(0, 999999)}"
    u = User(username=username, email=f"{username}@python.org")
    u.set_password('rando')
    db.session.add(u)
    db.session.commit()
    p = Post(title=f"Random post #{randint(0, 999999)}",
             body="Something very random",
             user_id=u.id)
    db.session.add(p)
    db.session.commit()
    return p