## Puzzle Tools by Tam
#### Video Demo:  https://youtu.be/Jw52Kyht7ws
#### Description:  A web-based utility app for puzzle hunt enthusiasts.  Python program with Flask.  Utilizes HTML, CSS,Javascript, JQuery, SQL, Jinja templates.  Use to calculate word values, compare strings that may be anagrams, see Caesar rotations of words, check basic characteristics of numbers, and access various reference material relating to words and numbers.
#### Overall structure.  There are three main sections: Words, Numbers, and Extras.  All can be accessed via dropdown menus from the top of the webpage or via a full left-sided collapsing menu.  All navigation tools utilize Bootstrap frameworks.  The side bar menu operates with Javascript functions on button click.  The main python program is supported by two helper files that contain the multiple functions for the Word and Numbers utilities.  There is a SQLite database file containing fixed data in a letters table and a numbers table that is accessed by Select query per user input.
#### WORDS.  In all cases, user input is stripped of non-alphabetic characters and converted to upper case.  If no alphabetic characters are entered, the user is prompted to try again.
##### Word Value.  User enters a word/text string and the function returns/displays the total word value based on user-selected scale (A=1 to Z=26, A=26 to Z=1, standard Scrabble values, or all 3 of these).  Radio button label of the selected item changes to bold (via JQuery function).
##### Anagram Comparison.  User enters 2 strings and the function returns whether the strings contain the same or different characters overall.  If the same, results include the list of letters in alphabetical order.  If different, results include the list of letters in common and the lists of letters unique to each of the two words.
##### Caesar Rotations.  User enters a text string and the function returns all 26 Caesar rotations.  Results also include possible English words among the rotation list via a call to a text dictionary (read from file at the time of the function call).  (Future enhancement: format the results table to highlight the possible English word matches compared to current version where those words are reported separately in tabular form above the rotation results).
##### Word Representations.  This function calls to a Letters table in a SQLite database built for this program.  Available data includes numeric representation of letters (binary, ternary, octal, hex), morse representation of letters, phonetic words representing letters, ascii codes for capital and lower case letters.  User can select any or all categories for tabular display.  Checkbox labels of selected items change to bold (via CSS).
#### NUMBERS.  Numeric input is checked and user is instructed to try again if any characters other than digits are entered.  Only positive integers are permitted (0 is disallowed).
##### Fun with Numbers.  This function checks a user-entered number and returns whether it is prime, a perfect square, a perfect cube, a triangular number and/or a Fibonacci number.  For non-prime numbers, all factors of the number are returned.  If the entered number exceeds 7 digits, the user is instructed to try again (design decision given that the python algorithms used are insufficiently speedy with large numbers).
##### Number Representations.  This function calls to a Numbers table in a SQLite database built for this program.  Available data includes alternate numeric representation (binary, ternary, octal, hex), morse representation of letters, roman numerals.  User can select any or all categories for tabular display.  Checkbox labels of selected items change to bold (via CSS).
#### EXTRAS.
##### Reference.  This page gathers some frequently used alphabets and other reference information (including an ASCII table, Braille, nautical flags, morse code, pig pen, semaphore, sign language, dancing man, and the periodic table).  The page utilizes Detail and Summary tags for easy dropdown display.  Summary text is restyled on click and provides a heading for each table as it is shown.
##### Links.  This is a simple list of 20 external websites of possible interest to puzzle hunt enthusiasts.  Each opens in a new tab when clicked.
##### Other.  Configured to run on my system with Flask in a virtual environment.  Call to the program via an executable command in terminal.  Liberal use of conditional jinja templates to control display output in html.
##### Files structure.  Project folder contains practice file, virtual file, and Readme.md.  Virtual file contains a virtual environment for python.  Flask installation was done in this virtual environment.  Practice file contains 3 python files (the main puztools.py and the two helpers: numbersnips.py and wordsnips.py), the database file with tables Letters and Numbers (numletter.db), the text-based dictionary (words_alpha.txt), the static folder, and the templates folder.  The static folder contains a folder for CSS (containing only main.css but with the option for an additional custom style sheet), a folder for images (containing the images for the reference page), and several favicon files for production of the tab icon (image also used in the main navigation bar).  The templates folder contains the main html page layout.html, a home.html landing page, the three top level html pages (words.html, numbers.html, and extras.html), and folders for words, numbers, and extras containing the subpages for each (as indicated by each heading above).







