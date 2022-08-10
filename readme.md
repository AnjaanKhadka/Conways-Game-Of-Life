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

    pip install -r requirements.txt

## Inference

### Greating your own world

First Execue following code then by simply clicking using mouse pointer, set and reset status of individual cells.

    python main.py

Press enter key to start/stop simulation. Simulation stops automatically once you reach stable state.

### Generating random world

To generate random world click 'r' key to randomize status of each cell randomly.

### Using existing world

To use existing world execute following code.

    python main.py <model_name>

Various example models are given in models directory. Executing acorn model can be done as

    python main.py models/acorn

or

    python main.py models/acorn.data

Alternatively to load those model press 'l' key in keyboard. Then in terminal window it asks for model path. Enter the path and load the model.

### Saving your own world

To save your own world first set the cells as per your desire. Then press 's' key in keyboard to initiate save process. In terminal type in your model_name or model_path/modelname to save the file.

## Models

### R-Pentomino

<!-- ![rpentomino](https://github.com/AnjaanKhadka/Conways-Game-Of-Life/blob/master/results/rpentomino.png) -->