import abjad
import calliope
import shami

o = None

music = [
# {   "label":"",
#     "I":    ([[0,0],{2:"tsu"},3,4],     [0,0],      o,      o),
#     "II":   (o,     o,      o,      o),
#     "III":  (o,     o,      o,      o),
# },
{   "label":"",
    "I":    ([1,1],     o,      o,      o),
    "II":   (o,     o,      o,      o),
    "III":  (o,     o,      o,      o),
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

calliope.illustrate_me(score_type=shami.ShamiScore)
