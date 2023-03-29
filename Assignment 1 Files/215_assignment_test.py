#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Read the maze from input.txt file
with open("input.txt", "r") as f:
    maze = [list(line.strip()) for line in f]

# Print the maze to check that it was read correctly
for row in maze:
    print(row)


# In[2]:


for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            start_row, start_col = i, j
        elif maze[i][j] == "E":
            end_row, end_col = i, j


# In[4]:


# Define the DFS function to search for a path
def dfs(maze, visited, row, col, end_row, end_col):
    # Check if we have reached the end point
    if row == end_row and col == end_col:
        return True
    
    # Mark the current cell as visited
    visited[row][col] = True
    
    # Check the neighbors of the current cell
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r, c = row + dr, col + dc
        if r >= 0 and r < len(maze) and c >= 0 and c < len(maze[0]):
            if maze[r][c] != "#" and not visited[r][c]:
                # Recursively search for a path from the neighbor cell
                if dfs(maze, visited, r, c, end_row, end_col):
                    # Mark the path and return True
                    maze[r][c] = "*"
                    return True
    
    # If no path is found, return False
    return False


# In[5]:


# Create a visited list to mark the visited cells
visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

# Call the DFS function to search for a path
dfs(maze, visited, start_row, start_col, end_row, end_col)


# In[7]:


for row in maze:
    for char in row:
        if char == "*":
            print("\033[91m{}\033[0m".format(char), end="")
        else:
            print(char, end="")
    print()


# In[ ]:




