-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop database to start f	resh
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Create a table to hold players
CREATE TABLE players(
	id serial PRIMARY KEY,
	name text
);

-- Create a table to hold match results
CREATE TABLE matches(
	winner int references players(id),
	loser int references players(id)
);

