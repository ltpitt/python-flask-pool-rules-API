from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Category, Rule

app = Flask(__name__)

engine = create_engine('sqlite:///pool-rules.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

newCategory = Category(
    name="1. General Rules",
    description="The following General Rules apply to all the games covered by these rules except when contradicted\
by specific game rules. In addition, the Regulations of Pool Billiards cover aspects of the game not directly\
related to the game rules, such as equipment specifications and organization of events.\
The games of Pool Billiards are played on a flat table covered with cloth and bounded by rubber cushions.\
The player uses a stick (pool cue) to strike a cue ball which in turn strikes object balls.\
The goal is to drive object balls into six pockets located at the cushion boundary.\
The games vary according to which balls are legal targets and the requirements to win a match.\
[Editorial comments on the U.S. English version: The masculine gender has been used for simplicity of wording\
 and is not intended to specify the gender of the players or officials.\
 The word \"game\" is used to refer to a discipline such as nine ball rather than a rack or a match.]",
)

session.add(newCategory)
session.commit()

newCategory = Category(
    name="2. Nine Ball",
    description="Nine ball is played with nine object balls numbered one through nine and the cue ball.\
    The balls are played in ascending numerical order. The player legally pocketing the nine ball wins the rack.",
)

session.add(newCategory)
session.commit()

newRule = Rule(
    name="1.1 Player\'s Responsibility",
    explanation="It is the player's responsibility to be aware of all rules, regulations and schedules applying to\
    competition. While tournament officials will make every reasonable effort to have such information readily\
    available to all players as appropriate, the ultimate responsibility rests with the player.",
    category_id=1,
)

session.add(newRule)
session.commit()
