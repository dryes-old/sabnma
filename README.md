sabnma
=====

* sabnma is a SABnzbd+ post-processing script to notify with NMA ([Notify My Android][nma]).

## dependencies:

* [Python2][python]
* [PyNMA][pynma]

## usage:

* Download both sabnma.py and the PyNMA zip from above.
* Unzip PyNMA and place sabnma.py alongside test.py.
* Set API key at the base of the script. ([NMA][nmaapi])
* Place files (pynma directory too) inside SABnzbd+ scripts path and set as post-processing script.

## notes:

* This can be called both directly by SAB, and also from a parent script - pass the 7 args returned by SAB to it.

[python]: http://www.python.org/
[pynma]: https://github.com/uskr/pynma/zipball/master
[nma]: https://www.notifymyandroid.com/
[nmaapi]: https://www.notifymyandroid.com/account.jsp