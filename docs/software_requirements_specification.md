# Overview
This document has a purpose of establishing and defining what our project R6stats is aiming to be. We are going to build our framework through functional and non-functioanl requirements. Our functional requirments should do a good job of explaining our projects basic functions. While the non-functional requirments should do a good job telling why those functions should be doing what they are doing. Overall this document is a key piece in explaining our project as it's developed.


# Functional 

1. Add a match
   * Ask for map and mode (eg. Chalet, Quick Match Secure Area)
   * Add each round and ask for Attack/Defense, operator, site and results (eg. Defense, Lesion, 2F Piano Room, K:2 D:1 A:0 W/L: W)
   * Could possibly dig even deeper and ask for the loadout of the operator, as well as notes for the round
   * Iterate adding each round until one side wins (eg. Until user has won 3 rounds)
   * At the end it confirms if the displayed information is correct, which the user will then confirm
   * When finished, the match will be added to a database and all other stat options will be updated


# Non-Functional

1. Add a match
   * Should be quick and easy to input information
   * Function finishes running when final round is added

# Functional 

1. Check stats
   * Check stats brings up 3 options: Operator Stats, Map Stats and Matches
   * Also displays lifetime stats (More about that below)
   * Each options functions explained below

# Non-Functional

1. Check stats for maps, operator and matches
   * The cursor should have a smooth transition to the next image/option
   * When the info is all loaded and found, then the page will be displayed
   * Don't let the user see lag, if data takes longer to retrieve then keep load screen going

# Functional 

1. Retrieve operator based stats
   * Cursor navigation (Colored square outline to represent selection), displayed in a similar manner to the actual game or mouse input can be used
   * On the side there is a section that displays top3/5 operators on each side and their stats (KDA and win rate)
   * When operator is selected, screen displays overall stats as well as most recent performance with operator
   * Data visualization and trends available

  # Functional 

1. Retrieve map based stats
   * Cursor navigation, displayed in a similar manner to the actual game or mouse input can be used
   * On side there is a section that displays top 5 maps and their stats (KDA and win rate)
   * When map is selected, overall stats are displayed and site data is displayed in a drop down list format
   * Data visualization and trends available


# Functional

1. Retrieve match based stats
   * Sorted by time in a drop down list format
   * Displayed with map picture, and also navigated by either cursor or mouse input
   * Next to map picture is the date and time played as well as a green or red highlight and the words "win" or "loss" to represent match result
   * Clicking on the match displays the stats of each round


# Functional 

1. Retrieve lifetime stats
   * Retrieves stats from the Ubisoft website
   * Also displays overall stats that have been added to the application since the start


# Non-Functional

1. Retrieve lifetime stats
   * Should be maunaully reloaded as the website updates
   * Overall stats will already be in the database so no need to reload


# Functional 

1. Retrieve information based on user input
   * functional requirement
   * functional requirement


# Non-Functional

1. Retrieve information based on user input
   * non-functional requirement
   * non-functional requirement

# Functional 

1. Allow user input
   * functional requirement
   * functional requirement


# Non-Functional

1. Allow user input
   * non-functional requirement
   * non-functional requirement


# Functional 

1. Allow easy movement around website
   * functional requirement
   * functional requirement


# Non-Functional

1. Allow easy movement around website
   * non-functional requirement
   * non-functional requirement 
