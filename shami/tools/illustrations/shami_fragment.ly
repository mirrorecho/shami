% 2017-12-30 23:37

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \context Staff = "Line1" \with {
            \consists Horizontal_bracket_engraver
        } {
        }
    >>
}