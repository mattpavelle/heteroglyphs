# heteroglyphs

A list of (and some sample code for) non-confusable/non-homoglyphs - i.e. characters appropriate for use when humans need to manually enter ASCII codes and you don't want them using confusing similar looking letters.

In an effort to maximize the number of characters one can use and minimize human errors, here are the ASCII non-confusables, henceforth known as heteroglyphs (similarity will change based on the typeface).

## Single character ASCII confusables/homographs:

* b ⇔ 6
* B ⇔ 8
* G ⇔ 6
* g ⇔ 9
* g ⇔ q
* L, l ⇔ I, 1
* O, o ⇔ 0
* S, s ⇔ 5
* V, v ⇔ U, u
* Z, z ⇔ 2

## Multi-character ASCII confusables/homographs:

* a ⇔ ci
* A ⇔ fi
* B ⇔ l3
* d ⇔ cl
* g ⇔ cj
* m ⇔ rn
* W ⇔ VV

I we want to prevent most of the multi-character homographs from being possible, we can limit ourselves to upper case letters and numbers and end up with a list of 19 possible characters in upper case (0125689BGILOSUVWZ are banned):

`347ACDEFHJKMNPQRTXY`

Realistically we should also exclude vowels to prevent us from accidentally generating offensive words, so let's trim this down to the following 17 characters:

`347CDFHJKMNPQRTXY`

Alternately we can follow the Microsoft permitted character licensing scheme, then we have a list of 24 characters (015AEILNOSUZ are banned):

`2346789BCDFGHJKMPQRTVWXY` (note, some obvious confusables exist here such as B/8 and G/6)

### Footnote

This whole codebase requires about 3 minutes of coding. But it also requires a few hours of research and as I've done this three times over the years so far, I decided to just save it to a repo.

-----

Thanks to the Unicode Consortium:

* [Technical Standard #39](http://www.unicode.org/reports/tr39/)
* [Confusable Utility](http://unicode.org/cldr/utility/confusables.jsp)
* [confusables.txt](http://www.unicode.org/Public/security/latest/confusables.txt)
