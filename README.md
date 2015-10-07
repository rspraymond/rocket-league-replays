# rocket-league-replays

[![Build Status](https://travis-ci.org/danielsamuels/rocket-league-replay-parser.svg?branch=develop)](https://travis-ci.org/danielsamuels/rocket-league-replay-parser)
[![Coverage Status](https://coveralls.io/repos/danielsamuels/rocket-league-replay-parser/badge.svg?branch=develop&service=github)](https://coveralls.io/github/danielsamuels/rocket-league-replay-parser?branch=develop)

Replay database and parser for Rocket League

## Server cronjobs

```
# Pull in player ratings every 5 minutes.
*/5 * * * * /var/www/rocket_league/.venv/bin/python -W ignore /var/www/rocket_league/manage.py get_league_ratings --settings=rocket_league.settings.production

# Post to Twitter and reddit at 10PM every day.
0 22 * * * /var/www/rocket_league/.venv/bin/python -W ignore /var/www/rocket_league/manage.py social_post --settings=rocket_league.settings.production

# Reprocess all matches in the morning (mostly for the excitement factor decay).
0 2 * * * /var/www/rocket_league/.venv/bin/python -W ignore /var/www/rocket_league/manage.py reprocess_matches --settings=rocket_league.settings.production
```
