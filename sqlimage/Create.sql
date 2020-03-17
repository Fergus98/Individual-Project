CREATE DATABASE baseball;
CREATE TABLE baseball.game(
	game_no INTEGER NOT NULL PRIMARY KEY,
	losing_team STRING(30) NOT NULL,
	winning_team STRING(30) NOT NULL,
	score INTEGER NOT NULL
);

CREATE table baseball.team(
	team_id INTEGER NOT NULL PRIMARY KEY,
	wins INTEGER NOT NULL,
	losses INTEGER NOT NULL
);

CREATE table baseball.players(
	player_id INTEGER NOT NULL PRIMARY KEY,
	team1 = STRING(30) NOT NULL,
	player_name STRING(30) NOT NULL
);
