Welcome to scoring module:

V0:
Create a scoring module with player and game entities so that we can Use to play the game and get results based on certain hyper parameters and randmoness.


To run the code:
1. Make sure you clone the directory and are present in scoring_module repo
2. Run  :
    `python3 main.py `
3. When you do that you see 3 files being created:
   1. player_events.txt: This file contains all the events of the fantasy game that are recieved by a player.
   2. player_score.txt: This file contain all the players and their scores.
   3. torurnamet_events.txt: This file contains infomration about the rounds and the matches and winner and loser status of the match.

4. Players information is represented by Player class, to define a new player:
 `
```
p1 = Player(
        name='nadal',
        total_score = 0,
        score_array = [],
        atp_ranking = -1,
        credits_needed = -1
    )
```
Add a object like this to add a player in `main.py.`
5. As of now the reward system being followed is:
```
{
    'POINT_WIN': 1,
    'GAME_WIN': 1,
    'ACE_SERVE': 1,
    'SET_WIN': 1,
    'MATCH_WIN': 1
}
```
This map is presnet in `sample_tennis_game_runner.py`