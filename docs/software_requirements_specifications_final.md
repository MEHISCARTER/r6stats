#Overview
This document aims to explain the functional and non functional requirements for the R6Stats application. The functional requirements are the functions that the user will be working with in the app, and the non functional requirements are to describe how the functional requirements work.

#Software Requirements 

#Category 1 Map

##Functional Requirement 2
###Selection of map
*Choosing a map is picked using a selection of map icons
*Click on a map picture to choose the map

##Non functional Requirement 2
###Selection of map
*Map icons are instantly loaded and in full quality
*Map icons are located in a file downloaded with the app, not downloaded online

#Category 2 Backend

##Functional Requirement 4
###Backend 
*Each round is ID'd by its match ID like this: matchid_roundnum
*3 Tables: Match, Round, UserStats
*Each table needs the other tables to operate

##Non functional Requirement 4
###Backend
*Data is stored locally on the machine, no server
*Data is quickly sorted and processed and displayed from the backend database

#Category 3 Match

##Functional Requirement 1
###Start up of add match
*On first run, asks for map that is being played on
*Date is added as a way to identify on the outside the match, while the backend gives it an integer ID

##Functional Requirement 3
###Each round stats
*KDA and Operator is input with keyboard
*Site, side and result type are chosen with given options

##Non functional Requirement 1
###Start up of add match
*Date is used to sort for the user while the match_id is for the backend to handle

##Non functional Requirement 3
###Each round stats
*Does not allow user more than 5 kills, 1 death or 5 assists
*Does not allow user to use an operator on the incorrect side

#Category 4 Gui

##Functional Requirement 5
###Add match GUI display
*On startup, the choose map screen comes up
*Next, each round displays Kills, Death, Assists next to each other
*Operator, site and result type are below

##Non Functional Requirement 5
###Add match GUI Display
*Easily readable
*No colors, simple black and white display besides map icons
