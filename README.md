The Synonym Machine
===================

*"He loved to dust his quondam grammars; it somehow mildly reminded him of his mortality." *

-- Moby Dick, by Herman Melville and the Synonym machine

**The Synonym Machine** downloads famous works of literature and replaces specified parts of speech with random synonyms. The script is currently configured to do this with Moby Dick, in reaction to [Robin Sloan's fascinating question](https://medium.com/message/14d61617f1d5): *if you replaced every adjective with a close synonym, would it be fair to call this new text by the same title?*

Here is an example of what the Synonym Machine changed in one section of Moby Dick

> ![Replaced adjectives in Moby Dick](http://i.imgur.com/JnJh8Zm.png =550x)

# Running the Synonym Machine
Part of speech tagging can take a while, so don't expect output immediately. On my laptop it takes a few minutes.

    synonym_machine.py moby_dick_synonym_edition.txt

# Setup and Installation

You're going to need nltk to run this and several console tools to generate the diff report. Here's what to do if you're on OSX like me:

    brew install wdiff aha
    pip install nltk urllib urllib2 urlopen simplenlp

From within Python, you're going to need to do the following

    python
    > import nltk
    > nltk.download()

When the selection menu is shown, just select "all" from the list and download the packages. Congratulations! You're ready to run the synonym machine! 

If you want to try other parts of speech, you can get hints in [this gist file](gist.github.com/natematias/75aab9f81086d8ccc82a).
