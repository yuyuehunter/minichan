#!/bin/python3

from app import db, models

# Japan

am = models.Category(name="Anime & Manga", url_name="a")
db.session.add(am)

poke = models.Category(name="Pokémon", url_name="poke")
db.session.add(poke)

dbz = models.Category(name="Dragon Ball (Z/GT/Super)", url_name="db")
db.session.add(dbz)

# Interests

v = models.Category(name="Video Games", url_name="v")
db.session.add(v)

tech = models.Category(name="Technology", url_name="g")
db.session.add(tech)

nix = models.Category(name="*nix", url_name="nix")
db.session.add(nix)

tv = models.Category(name="TV", url_name="tv")
db.session.add(dbz)

weapons = models.Category(name="Weapons", url_name="k")
db.session.add(weapons)

auto = models.Category(name="Auto", url_name="o")
db.session.add(auto)

bike = models.Category(name="Bicycles", url_name="bk")
db.session.add(bike)

animals = models.Category(name="Animals & Nature", url_name="an")
db.session.add(animals)

sports = models.Category(name="Sports", url_name="sp")
db.session.add(sports)

science = models.Category(name="Science", url_name="sci")
db.session.add(science)

international = models.Category(name="International", url_name="int")
db.session.add(international)

toys = models.Category(name="Toys", url_name="biz")
db.session.add(toys)

# Creative

photo = models.Category(name="Photography", url_name="p")
db.session.add(international)

food = models.Category(name="Food & Coocking", url_name="ck")
db.session.add(food)

artwork = models.Category(name="Artwork", url_name="aw")
db.session.add(artwork)

music = models.Category(name="Music", url_name="mu")
db.session.add(music)

design = models.Category(name="Graphic Design", url_name="gd")
db.session.add(design)

diy = models.Category(name="DIY", url_name="diy")
db.session.add(international)

# Others

travel = models.Category(name="Travel", url_name="trv")
db.session.add(travel)

paranormal = models.Category(name="Paranormal", url_name="x")
db.session.add(paranormal)

literature = models.Category(name="Literature", url_name="lit")
db.session.add(literature)

advice = models.Category(name="Advice", url_name="adv")
db.session.add(advice)

lgbt = models.Category(name="LGBT", url_name="lgbt")
db.session.add(lgbt)

# NSFW

random = models.Category(name="Random", url_name="b")
db.session.add(random)

request = models.Category(name="Request", url_name="r")
db.session.add(request)

women = models.Category(name="Sexy Beautiful Women", url_name="s")
db.session.add(women)

men = models.Category(name="Handsome Men", url_name="hm")
db.session.add(men)

pron = models.Category(name="pr0n", url_name="pr0n")
db.session.add(pron)

db.session.commit()

print ("All Done")
