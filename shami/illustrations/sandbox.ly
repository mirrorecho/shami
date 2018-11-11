% 2018-01-18 22:03

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
                {
                    {
                        \time 4/4
                        \txtNoteHead "0"
                        b'2
                        c'2
                    }
                    {
                        \txtNoteHead "0"
                        b'2
                        c'2
                    }
                    {
                        \txtNoteHead "0"
                        b'2
                        c'2
                    }
                    {
                        \txtNoteHead "0"
                        b'2
                        c'2
                    }
                }
            }
        }
    >>
}