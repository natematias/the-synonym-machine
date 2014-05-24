#!/bin/sh

# Use this instead of diff[1] to get colored[2] word-based diffs.
# Useful for text documents that have reflowed paragraphs.
# Requires that wdiff is installed in your $PATH.
#
# [1] All diff options are ignored. Only replaces simplest usage.
# [2] Colors are always emitted. If piping into less, use "-R" or set LESS=-R

# Iain Murray, February 2009, Tweaked in June 2011

if [ "$#" -lt 2 ] ; then
    echo 'Usage: cwdiff FILE1 FILE2'
    echo '       cwdiff [any options will be discarded] FILE1 FILE2'
    echo
    echo 'cwdiff emits colored, word-based diffs. Requires wdiff(1).'
    echo 'If piping into less use -R option or set LESS=-R'
    echo
    exit
fi

# Discard any options, for example SVN attempts to set a bunch of GNU diff
# options
shift $(($# - 2))

# Color commands adapted from cdiff alias by
# Paul Warren <pdw@ex-parrot.com> 12/01/2001
# http://ex-parrot.com/pdw/cdiff.html
#  colour for added lines (bright blue)
#  (yellow, used in cdiff, alias is less robust to terminal background colour)
diffnew=`tput setf 1``tput bold`
#  colour for removed lines (bright red)
diffold=`tput setf 4``tput bold`
#  reset - original pair, unset all attributes
reset=`tput op``tput sgr0`


# The -3 option to wdiff gives no context, so I'm getting wdiff to spit out the
# whole document and using grep to trim it down. The regex for grep could be
# improved, but for text documents is probably ok, and at worst will include
# some extra output that can be ignored..
wdiff \
    --start-delete "${diffold}[-" \
    --end-delete "-]${reset}" \
    --start-insert "${diffnew}{+" \
    --end-insert "+}${reset}" \
    -n "$1" "$2" \
    | grep -C2 '\['
# CAREFUL: The line above contains an escape character.
# Don't copy the grep command by typing ^[ instead of 

# This grep line hits false positives more often for me:
# | grep -C2 '[{[][-+].*[-+][]}]'
