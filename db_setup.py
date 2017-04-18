from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(
        Integer, primary_key=True
    )
    name = Column(
        String(250), nullable=False
    )
    email = Column(
        String(250), nullable=False
    )
    image = Column(
        String(250)
    )


    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'image': self.image,
        }


class Category(Base):
    __tablename__ = 'category'
    id = Column(
        Integer, primary_key=True
    )

    name = Column(
        String(250), nullable=False
    )

    description = Column(
        String(250), nullable=False
    )

    user_id = Column(
        Integer, ForeignKey('user.id')
    )
    user = relationship(User)

    rule = relationship("Rule",
                        cascade="all, delete-orphan",
                        passive_deletes=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
        }


class Rule(Base):
    __tablename__ = 'rule'
    id = Column(
        Integer, primary_key=True
    )
    name = Column(
        String(250), nullable=False
    )
    explanation = Column(
        String(250), nullable=False
    )
    image = Column(
        String(250)
    )


    category_id = Column(
        Integer, ForeignKey('category.id', ondelete='CASCADE'), nullable=False
    )
    category = relationship("Category")

    user_id = Column(
        Integer, ForeignKey('user.id')
    )
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'explanation': self.explanation,
            'image': self.image,
            'game_id': self.game_id,
            'user_id': self.user_id,
        }


# SQLite engine
engine = create_engine('sqlite:///pool-rules.db')

Base.metadata.create_all(engine)
