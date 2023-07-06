import chess.pgn
import csv

pgn =""

with open(pgn, 'r') as pgn_file, open('mygames.csv', 'w', newline='') as csv_file:

    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['Start Time', 'Winner', 'Time Increment', 'Termination', 'White Player ID', 'White Player Rating', 'Black Player ID', 'Black Player Rating', 'Moves', 'Number of Moves', 'Opening Eco', 'Opening Name'])

    while True:
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break

        start_time = game.headers['UTCDate'] + ' ' + game.headers['UTCTime']
        winner = game.headers['Result']
        if winner == '1-0':
            winner = 'white'
        elif winner == '1/2-1/2':
            winner = 'draw'
        else:
            winner = 'black'
        time_control = game.headers['TimeControl']
        termination = game.headers['Termination'].split()[-1]
        white_player_id = game.headers['White']
        white_player_rating = int(game.headers['WhiteElo'])
        black_player_id = game.headers['Black']
        black_player_rating = int(game.headers['BlackElo'])
        all_moves = game.mainline_moves()
        num_turns = int(len(list(all_moves)) // 2)
        eco = game.headers['ECO']
        opening_name = game.headers['ECOUrl'][31:].replace('-', ' ')

        csv_writer.writerow([start_time, winner, time_control, termination, white_player_id, white_player_rating, black_player_id, black_player_rating, all_moves, num_turns, eco, opening_name])

with open(pgn, 'r') as pgn_file, open('mygames.csv', 'a', newline='') as csv_file:

    csv_writer = csv.writer(csv_file)

    while True:
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break

        start_time = game.headers['UTCDate'] + ' ' + game.headers['UTCTime']
        winner = game.headers['Result']
        if winner == '1-0':
            winner = 'white'
        elif winner == '1/2-1/2':
            winner = 'draw'
        else:
            winner = 'black'
        time_control = game.headers['TimeControl']
        termination = game.headers['Termination'].split()[-1]
        white_player_id = game.headers['White']
        white_player_rating = int(game.headers['WhiteElo'])
        black_player_id = game.headers['Black']
        black_player_rating = int(game.headers['BlackElo'])
        all_moves = game.mainline_moves()
        num_turns = int(len(list(all_moves)) // 2)
        eco = game.headers['ECO']
        opening_name = game.headers['ECOUrl'][31:].replace('-', ' ')

        csv_writer.writerow([start_time, winner, time_control, termination, white_player_id, white_player_rating, black_player_id, black_player_rating, all_moves, num_turns, eco, opening_name])

