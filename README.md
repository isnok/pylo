pylo
====

Some coding around with lojban.

I'd like to have a state-of-the-art lojban parser with python bindings,
but unfortunately searching around the internet returned None ;-)

Fortunately, it returned some lojban-parsers, which satisfied me,
but only for a small amount of time, as i would find out.

So it happened that one evening i sat down to play around with the idea
of parsing lojban.

At first, i started by quickly hacking some idea that i had, an attempt
to do it all in plain python, but after just an hour or two, i got to
the first 'hairy' point, as we germans say, and realized quickly, that
the effort would not be worth it.

There are bison/yacc/younameit grammars out there, under free licenses,
that will definitely do a much better job, and that almost for free.
Bad thing about it, i haven't ever before used one of these, and their
complexity is kind of suspect to me. I fear i could get lost there.

So there must be another way. And of course, there is!
I could just hijack a command line tool to do the parsing, and then,
almost instantly, get to work on the next goal: a jbo2en-translator.

Yep, that was the original idea: Why has noone ever before attempted
to write a 'verbose' translator for lojban? It should be a no-brainer.
We already have the vocabulary in a form, where all we need to do, is
substitute xn with the 'verbose' translation of the sumti.

Okay, okay, that was a bit unspecific, this works only for gismu, and
some cmavo, but hey, why worry about something, that can surely be
fixed once we are the point, that it may become an issue.

I mean, most of my sentences are formed almost exclusively of gismu with
a good portion of cmene as well. And this is possibly true for a lot of
new lojban learners. These could, just as me, make very good use of a
verbose translation of their sentences. More information, more precision.

Jupp, so that's where we were, where we are, and where we're going!
So stay tuned for the latest releases of what starts here (on github)
as pylo.

isnok
