#(set-global-staff-size 22)

txtNoteHead = #(define-music-function
     (parser location txt)
     (string?)
   #{
        \once \override NoteHead.stencil = #ly:text-interface::print
        \once \override NoteHead.text = #(markup txt )
   #})

scoreOverrides = {
    \override Staff.StaffSymbol.line-positions = #'( 6 0 -6 )
    \override Staff.TimeSignat dure.break-visibility = #all-invisible
}