# Conway's Game of Life

It is a simple autometon devised by [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway). It is a zero player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

## Rules

Conway's Game of life follows basic rule that defines certain cell will live or die in next generation. It follows following rules:

1. Cells that have fewer than 2 neighbouring cells alive will die in next generation due to under population.

2. Cells that are active and have 2 or 3 neighbouring cells alive will live next generation being suitable to live.

3. Cells that are dead but has exactly 3 neighbouring cells alive will get to live in next generation being suitable to populate.

4. Cells that are alive and have more than 3 neighbouring cells alive in this genaration will die in next generation as a result of overpopulation.

5. All other cells that were dead will remain dead for next generation.

## Installing

All requirements of the file are given in [requirements.txt](https://github.com/AnjaanKhadka/Conways-Game-Of-Life/blob/master/requirements.txt) file. To install all requirements execute following code.