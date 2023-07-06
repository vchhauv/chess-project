# chess-project

### General guideline :
1. Get the current top 10 rated chess players in classical chess.
2. Download the players' games in pgn files.
3. Unzip them into the same folder.
4. Convert all the pgn files to csv files and concatenate them into the same csv file.
6. To be continued...

### How to do so:
1. We will scrap "https://www.chess.com/ratings" to get the top ten.
2. Then, we download automaticaly the pgn from "https://www.pgnmentor.com/files.html" depending on who is in the top 10.
3. We will need to manually unzip the files into the same folder.
4. We will convert the pgn files to csv files using pgn_extract.py.
