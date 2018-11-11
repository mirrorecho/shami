import abjad
import calliope

STRING_WRITTEN_PITCHES = {
    "I": 14,
    "II": 9,
    "III":4,
}

class ShamiMeasure(calliope.Bubble):
    container_type = abjad.Measure
    is_simultaneous = None # TO DO: WTF
    position = 0
    
    def number_note(self, number=0, duration=(1,4), string="I"):
        note = abjad.Note()
        note.written_duration = duration
        note.written_pitch = STRING_WRITTEN_PITCHES[string]
        number_head_command = 'txtNoteHead "%s"' % number
        abjad.attach(abjad.indicatortools.LilyPondCommand(number_head_command, "before"), note)
        return note

    def music(self, **kwargs):
        if "I" in self.parent.tab_dict:
            if len(self.parent.tab_dict["I"]) > self.position:
                self.parent.tab_dict["I"][self.position]
        my_measure = self.music_container((4,4) )
        my_measure.append( self.number_note() )
        return(my_measure)

class ShamiTab(calliope.Bubble):
    # TO DO... measures should be children
    # measures = ()
    child_types = (ShamiMeasure,)
    tab_dict = None
    is_simultaneous = False

    def __init__(self, tab_dict):
        super().__init__()
        self.tab_dict = tab_dict
        measure_length = max( [len(v) for n,v in tab_dict.items() if n in ("I","II","III")] )
        self.extend([ShamiMeasure(position=i) for i in range(measure_length)])

class ShamiFragment(calliope.Bubble):
    # TO DO... tabs should be children
    # stylesheets=("../../stylesheets/score.ily",)
    child_types = (ShamiTab,)
    is_simultaneous = False
    bar_line = None
    tempo_command = None
    rehearsal_mark_number = None
    # time_signature = None # TO DO... use?

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.extend([ShamiTab(a) for a in args])


    def process_music(self, music, **kwargs):
        super().process_music(music, **kwargs)

        if len(music) > 0:
            music_start = music[0]
            staff_lines_command = "override Staff.StaffSymbol.line-positions = #'( 3 0 -3 )"
            hide_time_command = "override Staff.TimeSignature.break-visibility = #all-invisible"
            abjad.attach(abjad.indicatortools.LilyPondCommand(staff_lines_command, "before"), music_start)
            abjad.attach(abjad.indicatortools.LilyPondCommand(hide_time_command, "before"), music_start)
            # abjad.attach(abjad.indicatortools.LilyPondCommand("stopStaff", "before"), music)
            # # TO DO... test out using abjad.override instead
            # abjad.attach(abjad.indicatortools.LilyPondCommand("override Staff.StaffSymbol.line-positions = #'( -4 0 4 )", "before"), music)
            # abjad.attach(abjad.indicatortools.LilyPondCommand("startStaff", "before"), music)

            # # NECESSARY??
            # rests_command =  abjad.indicatortools.LilyPondCommand("expandFullBarRests", "before")
            # abjad.attach(rests_command, music_start)

            # # TO DO: remove clef
            # clef_obj = abjad.Clef(self.clef)
            # abjad.attach(clef_obj, music_start)

            if self.rehearsal_mark_number:
                mark = abjad.indicatortools.RehearsalMark(number=self.rehearsal_mark_number)
                abjad.attach(mark, music_start)

            # # TO DO .. use?
            # if self.time_signature:
            #     # TO DO... is the numeric comm*ad necessary... maybe just include it at the score level?
            #     time_command_numeric =  abjad.indicatortools.LilyPondCommand("numericTimeSignature", "before")
            #     abjad.attach(time_command_numeric, music_start)

            #     time_command =  abjad.indicatortools.LilyPondCommand("time " + str(self.time_signature[0]) + "/" + str(self.time_signature[1]), "before")
            #     # TO DO MAYBE: below is cleaner... but abjad only attaches time signature properly to staff (not notes in a container)... workaround?
            #     # time_command = abjad.TimeSignature( self.time_signature )
            #     abjad.attach(time_command, music)
            #     # TO DO... HIDE TIME SIGNATURE...

            if self.bar_line:
                bar_command =  abjad.indicatortools.LilyPondCommand('bar "' + self.bar_line + '"', 'before')
                abjad.attach(bar_command, music_start)

            if self.tempo_command:
                tempo_command =  abjad.indicatortools.LilyPondCommand("tempo \markup \\fontsize #3 { %s }" % self.tempo_command, "before")
                # print(tempo_command)
                abjad.attach(tempo_command, music_start)
