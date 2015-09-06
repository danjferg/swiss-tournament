#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches;")
    DB.commit()
    DB.close()
    return None


def deletePlayers():
    """Remove all the player records from the database."""

    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players;")
    DB.commit()
    DB.close()
    return None


def countPlayers():
    """Returns the number of players currently registered."""

    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(*) FROM players;")
    num_players = c.fetchone()
    DB.close()
    return int(num_players[0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    DB.commit()
    DB.close()
    return None


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    QUERY = '''
        SELECT p.id, p.name,
            count(mw.winner) as wins,
            count(mw.winner) + count(ml.loser) as losses
        FROM players p
        LEFT JOIN matches mw ON p.id = mw.winner
        LEFT JOIN matches ml ON p.id = ml.loser
        GROUP BY p.id, p.name
        ORDER by wins DESC
    '''
    DB = connect()
    c = DB.cursor()
    c.execute(QUERY)
    standings = c.fetchall()
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    QUERY = "INSERT INTO matches (winner, loser) VALUES (%s,%s);"
    DB = connect()
    c = DB.cursor()
    c.execute(QUERY, (winner, loser))
    DB.commit()
    DB.close()
    return None


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = playerStandings()
    pairs = []
    for i in range(0, len(standings)/2):
        pairs.append((standings[2*i][0], standings[2*i][1],
                     standings[2*i+1][0], standings[2*i+1][1]))
    return pairs
