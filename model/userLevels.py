##########*********** IMPORTANT *****************#############
################## WHY ARE WE DOING THIS? ####################
# -------------> WE ARE DOING THIS BECAUSE THIS WILL ADD INNOVATION TO OUR PROJECT. IF MORT JUST SEES US DOING GAMES AND SLAPPING AN API ONTO IT, HE'S GONNA SAY WE AREN'T INNOVATIVE ENOUGH.
# -------------> BY DOING THIS, IT WILL ADD GREATER INNOVATION FOR US, WE WILL GET A HIGHER SCORE

# PLEASE, for god's sake, DO NOT DISREGARD THIS MESSAGE. WE LITERALLY DO NOT HAVE THAT MUCH TIME LEFT. IF WE KEEP SLACKING OFF LIKE THIS WE WILL FAIL.
# I CANNOT EMPHASIZE THIS ENOUGH.

####################################################################################################
# Plan for user levels:
# 1. This will be executed in all the different game modes
# 2. Accounts for all games
# 3. Each submission of the same username adds the games played by one
# 4. After playing any game a certain amount of times, they achieve a ranking.
# 5. Plan for ranking: 10 games=Bronze, 25 games=Silver, 60 games=Gold, 100 games=Platinum
# How is this possible you may ask? Just abuse the update thing in CRUD, I'm pretty sure that's it. We have to try to find out if it works.
from datetime import date
import datetime
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError