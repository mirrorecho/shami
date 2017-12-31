% 2017-12-31 00:28

\version "2.19.54"
\language "english"

\include "../tools/shami_stylesheet.ily"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Line1" \with {
            \consists Horizontal_bracket_engraver
        } {
            {
                \override Staff.StaffSymbol.line-positions = #'( 3 0 -3 )
                \override Staff.TimeSignature.break-visibility = #all-invisible
                \txtNoteHead "6"
                c'4
                b'4
                a'4
            }
        }
    >>
}