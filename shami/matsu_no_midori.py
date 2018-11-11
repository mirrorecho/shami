import abjad
import calliope
import shami

o = None
s = 1000



(
    I(  [4, o, (4,l*3), o],      o,   ),
    II( o,                     [0, o, o, o]),
    III(o,                     [o, o, o, 0]),
),( "x 3"
    I(  [4, o, (4,3), o],      o,   ),
    II( o,                     [0, s*0, o, o]),
    III(o,                     [0, o,    o, o]),
)

music = [
{   "label":"",
    "I":    ([4, o, (4,3), o],      o,),
    "II":   (o,                     [0, o, o, o]),
    "III":  (o,                     [o, o, o, 0]),
},
{   "label":"x 3",
    "I":    ([4, o, (4,3), o],      o,),
    "II":   (o,                     [0, 3*s, o, o]),
    "III":  (o,                     [0,  o, o, o]),
},
# {   "label":"",
#     "I":    (o,     o,      o,      o),
#     "II":   (o,     o,      o,      o,      1),
#     "III":  (o,     o,      o,      o),
# }, 
]


Line1 = shami.ShamiFragment(*music)
# class Line1(calliope.Fragment):
#     music_contents="b1 c1"

calliope.illustrate_me(
    score_type=shami.ShamiScore
    )