import abjad
import calliope


class ShamiFragment(calliope.Fragment):
    # stylesheets=("../../stylesheets/score.ily",)
    
    # pass
    def process_music(self, music, **kwargs):
        super().process_music(music, **kwargs)

        if len(music) > 0:
            music_start = music[0]
            staff_lines_command = "override Staff.StaffSymbol.line-positions = #'( 3 0 -3 )"
            hide_time_command = "override Staff.TimeSignature.break-visibility = #all-invisible"
            abjad.attach(abjad.indicatortools.LilyPondCommand(staff_lines_command, "before"), music_start)
            abjad.attach(abjad.indicatortools.LilyPondCommand(hide_time_command, "before"), music_start)
    #     abjad.attach(abjad.indicatortools.LilyPondCommand("stopStaff", "before"), music)
    #     # TO DO... test out using abjad.override instead
    #     abjad.attach(abjad.indicatortools.LilyPondCommand("override Staff.StaffSymbol.line-positions = #'( -4 0 4 )", "before"), music)
    #     abjad.attach(abjad.indicatortools.LilyPondCommand("startStaff", "before"), music)



