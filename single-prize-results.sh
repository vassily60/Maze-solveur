#!/usr/bin/env bash

# Define the maze files
declare -a maze_files=("1prize-open.txt" "1prize-medium.txt" "1prize-large.txt")

# Define the algorithms to test
algorithm1="single_dfs"
algorithm2="single_bfs"
algorithm3="single_gbfs"
algorithm4="single_astar"

# Define the output folder
output_folder="algorithm_results"

mkdir -p "$output_folder"

output_dfs="${output_folder}/${algorithm1}_output.txt";
output_bfs="${output_folder}/${algorithm2}_output.txt";
output_gbfs="${output_folder}/${algorithm3}_output.txt";
output_astar="${output_folder}/${algorithm4}_output.txt";

# Clear the files
> "$output_dfs"
> "$output_bfs"
> "$output_gbfs"
> "$output_astar"

for maze_file in "${maze_files[@]}"; do

    echo -e "\nRunning ${algorithm1} on ${maze_file}:" >> "$output_dfs";
    python3 v1.py -f "$maze_file" -a "$algorithm1" >> "$output_dfs";

    echo -e "\nRunning ${algorithm2} on ${maze_file}:" >> "$output_bfs";
    python3 v1.py -f "$maze_file" -a "$algorithm2" >> "$output_bfs";

    echo -e "\nRunning ${algorithm3} on ${maze_file}:" >> "$output_gbfs";
    python3 v1.py -f "$maze_file" -a "$algorithm3" >> "$output_gbfs";

    echo -e "\nRunning ${algorithm4} on ${maze_file}:" >> "$output_astar";
    python3 v1.py -f "$maze_file" -a "$algorithm4" >> "$output_astar";
done