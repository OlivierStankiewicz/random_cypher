# random_cypher

A project showcasing the substitution cypher, including the funciton of cyphering a txt file and a minigame where you have the chance to decypher it yourself.

The file named "substitution_cypher.py" when run takes a txt file named "original_file.txt" and cyphers it using a random substitution cypher (for easier decyphering it makes all letters capital and shuffles them only among each other, excluding numbers, letters other than latin and other special characters). The cyphered version is put in a file named "cyphered_file.txt".

The file named "decypher.py" contains a minigame, in which in the console the current version of the text is displayed, together with some useful options and information. This includes the option to swap two letters (the main point of the game), option to mark letters as confirmed (they will be displayed as green in the text, making remembering which letters the player is sure of easier) and a statistic of the percentage of each character in the text, which aims to provide some help in guessing the first few swaps (each language has a quite well defined distribution of letters when the text is long enough), there if also an option to randomly shuffle the letters (can be understood as many random swaps performed), the idea is that at the beginning of the game it may be beneficial to shuffle the letters, possibly notice some patterns and by decyphering them start then decyphering the rest much easier (the first few swaps are much harder than later ones).

When the game is finished, by inputing 'q' or 'Q' instead of the two letters to be swapped, the hopefully decyphered again text, is saved in the decyphered_file.txt.

IMPORTANT
This project only cypheres latin letters and even capitalizes them. All other characters are left untouched (provided that python supports them). This was done to make the minigame easier, which is the whole point of the project.
