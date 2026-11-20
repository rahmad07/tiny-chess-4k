# Tiny Chess 4K

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rahmad07/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rahmad07/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A chess engine in at most 4,096 bytes of Python, built for the [tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01) on make.fun. It plays 8 games against a fixed gauntlet of house engines through the trial env and is rated by Elo.

## Play

`main.py` is the whole engine: Python 3.13 standard library only, no other files. It talks to the trial env (`MAKEFUN_ENV_URL`) with POST `/game`, `/move` and `/resign`, and picks its moves with a fixed node-budget search — never a clock, so every replay matches.
