# Rummy Card Game
Rummy is a two-player card game played in a series of rounds. At the beginning of each round, each player is dealt a 10-card hand from a 36-card deck.

Each card in the deck is uniquely composed of the following two attributes:

One of 4 “suits” (Spades ‘S’, Hearts ‘H’, Clubs ‘C’, or Diamonds ‘D’)
One of 9 “ranks” (the numbers 1-9)

The goal of the game is to group cards into groups (melds) of 3 or more cards of matching rank, which can either be:
 - “sets”: 3+ cards of the same rank (ex: 9D, 9S, 9C since they all have rank 9)
 - “runs”: 3+ cards of consecutive values within the same suit. Consecutive values are any values in the sequence of 1,2,3,4,5,6,7,8,9 (ex: 1-2-3-4 is consecutive, 1-2-4-5 is not).

Given an input of a hand of cards with suits and ranks, return all possible sets and runs that could be formed.

**Example 1:**

```
Input: cards = ["1C", "9C", "8C", "7C", "5C", "4C", "9D", "9S", "1D", "1H"]
Output: [["1C", "1D", "1H"], ["9C", "9D", "9S"], ["7C", "8C", "9C"]]
```

**Example 2:**

```
Input: ["4C", "2C", "3C", "1C", "8D", "6C", "9D", "9C", "1D", "1H"]
Output: [["1C", "1D", "1H"], ["1C", "2C", "3C"], ["2C", "3C", "4C"], ["1C", "2C", "3C", "4C"]]
```
