import abjad
import calliope
import shami

o = None

# music = [
# {   "label":"",
#     "I":    ([[0,0],{2:"tsu"},3,4],     [0,0],      o,      o),
#     "II":   (o,     o,      o,      o),
#     "III":  (o,     o,      o,      o),
# },
# {   "label":"",
#     "I":    (o,     o,      o,      o),
#     "II":   (o,     o,      o,      o),
#     "III":  (o,     o,      o,      o),
# },
# ]
# 

class MyGrid(calliope.Bubble):
    class Line1(shami.ShamiFragment):
        music_contents="c'4 b' a'"
        def process_music(self, music, **kwargs):
            super().process_music(music, **kwargs)
            abjad.attach( abjad.LilyPondCommand('txtNoteHead "6"', 'before'), music[0] )

m = MyGrid()

m.illustrate_me(score_type=shami.ShamiScore)
