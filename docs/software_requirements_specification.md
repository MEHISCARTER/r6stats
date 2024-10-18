# Overview
This document has a purpose of establishing and defining what our project R6stats is aiming to be. We are going to build our framework through functional and non-functioanl requirements. Our functional requirments should do a good job of explaining our projects basic functions. While the non-functional requirments should do a good job telling why those functions should be doing what they are doing. Overall this document is a key piece in explaining our project as it's developed.


# Functional 

1. Add a match
   * The website shall Ask for map and mode (eg. Chalet, Quick Match Secure Area)
   * The website shall Add each round and ask for Attack/Defense, operator, site and results (eg. Defense, Lesion, 2F Piano Room, K:2 D:1 A:0 W/L: W)
   * The website shall Could possibly dig even deeper and ask for the loadout of the operator, as well as notes for the round
   * The website shall Iterate adding each round until one side wins (eg. Until user has won 3 rounds)
   * The website shall At the end it confirms if the displayed information is correct, which the user will then confirm
   * The website shall When finished, the match will be added to a database and all other stat options will be updated


# Non-Functional

1. Add a match
   * The website shall Should be quick and easy to input information
   * The website shall Function finishes running when final round is added

# Functional 

1. Check stats
   * The website shall Check stats brings up 3 options: Operator Stats, Map Stats and Matches
   * The website shall Also displays lifetime stats (More about that below)
   * The website shall Each options functions explained below

# Non-Functional

1. Check stats for maps, operator and matches
   * The website shall The cursor should have a smooth transition to the next image/option
   * The website shall When the info is all loaded and found, then the page will be displayed
   * The website shall Don't let the user see lag, if data takes longer to retrieve then keep load screen going

# Functional 

1. Retrieve operator based stats
   * The website shall Cursor navigation (Colored square outline to represent selection), displayed in a similar manner to the actual game or mouse input can be used
   * The website shall On the side there is a section that displays top3/5 operators on each side and their stats (KDA and win rate)
   * The website shall When operator is selected, screen displays overall stats as well as most recent performance with operator
   * The website shall Data visualization and trends available

  # Functional 

1. Retrieve map based stats
   * The website shall Cursor navigation, displayed in a similar manner to the actual game or mouse input can be used
   * The website shall On side there is a section that displays top 5 maps and their stats (KDA and win rate)
   * The website shall When map is selected, overall stats are displayed and site data is displayed in a drop down list format
   * The website shall Data visualization and trends available


# Functional

1. Retrieve match based stats
   * The website shall Sorted by time in a drop down list format
   * The website shall Displayed with map picture, and also navigated by either cursor or mouse input
   * The website shall Next to map picture is the date and time played as well as a green or red highlight and the words "win" or "loss" to represent match result
   * The website shall Clicking on the match displays the stats of each round


# Functional 

1. Retrieve lifetime stats
   * The website shall Retrieves stats from the Ubisoft website
   * The website shall Also displays overall stats that have been added to the application since the start


# Non-Functional

1. Retrieve lifetime stats
   * The website shall Should be maunaully reloaded as the website updates
   * The website shall Overall stats will already be in the database so no need to reload


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
