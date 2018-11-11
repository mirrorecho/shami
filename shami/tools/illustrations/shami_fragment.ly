% 2018-01-10 00:10

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    {
        \override Staff.StaffSymbol.line-positions = #'( 3 0 -3 )
        \override Staff.TimeSignature.break-visibility = #all-invisible
        {
            {
                \time 4/4
                c'2
                c'2
            }
            {
                c'2
                c'2
            }
            {
                c'2
                c'2
            }
            {
                c'2
                c'2
            }
            {
                c'2
                c'2
            }
        }
    }
}