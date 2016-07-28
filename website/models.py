from website import db


def save_object(obj):
    db.session.add(obj)
    try:
        db.session.commit()
        return obj
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()


def delete_object(obj):
    db.session.delete(obj)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    last_update = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        return save_object(self)

    def update(self):
        return save_object(self)

    def delete(self):
        return delete_object(self)


class User(BaseModel):
    __tablename__ = 'user'

    guid = db.Column(db.String(37), nullable=False, unique=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=True)
    full_name = db.Column(db.String(254), nullable=True)
    address = db.Column(db.String(254), nullable=True)
    password = db.Column(db.String(254), nullable=True)
    photo = db.Column(db.String(254), nullable=True)

    # relation field
    twitter = db.relationship('Twitter', uselist=False, backref='user')
    facebook = db.relationship('Facebook', uselist=False, backref='user')


class SocialMedia(BaseModel):
    __abstract__ = True

    token = db.Column(db.String(254), nullable=False)
    token_secret = db.Column(db.String(254), nullable=False)


class Twitter(SocialMedia):
    __tablename__ = 'user_twitter'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    twitter_id = db.Column(db.String(254), nullable=False, unique=True)

    def __repr__(self):
        return '<twitter: {0}>'.format(self.user.username)


class Facebook(SocialMedia):
    __tablename__ = 'user_facebook'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    facebook_id = db.Column(db.String(254), nullable=False, unique=True)

    def __repr__(self):
        return '<facebook: {0}>'.format(self.user.username)
