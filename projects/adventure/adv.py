from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

my_map = {}
cur_room = player.current_room.id
prev_room = None

first_pass = True
# DFT
# Explore the graph in some direction
# As we go, log our directions in our traversal path
# BFS
# When we hit a dead end, find the nearest unvisited room: nearest question mark
# As we go to the nearest unexplored exit, log our path again
while len(traversal_path) > 960 or first_pass == True:
    first_pass = False
    traversal_path = []
    my_map = {}

    while len(my_map) < len(room_graph):

        if cur_room not in my_map:
            my_map[cur_room] = {}
            exits = player.current_room.get_exits()
            for exit in exits:
                my_map[cur_room][exit] = '?'
        else:
            exits = player.current_room.get_exits()

        if traversal_path:
            last_step = traversal_path[-1]
            if last_step == 'n':
                my_map[cur_room]['s'] = prev_room
            elif last_step == 'e':
                my_map[cur_room]['w'] = prev_room
            elif last_step == 's':
                my_map[cur_room]['n'] = prev_room
            elif last_step == 'w':
                my_map[cur_room]['e'] = prev_room


        if '?' in my_map[cur_room].values():

            good_direction = False
            while good_direction is False:
                direction = random.choice(exits)
                if my_map[cur_room][direction] == '?':
                    good_direction = True

            prev_room = cur_room

            player.travel(direction)
            traversal_path.append(direction)

            cur_room = player.current_room.id

            my_map[prev_room][direction] = cur_room

        else:        

            queue = Queue()
            visited = set()

            path = [(None, cur_room)]

            queue.enqueue(path)

            while queue.size() > 0:
                current_path = queue.dequeue()
                temp_room = current_path[-1][1]

                if '?' in my_map[temp_room].values():
                    break

                if temp_room not in visited:
                    visited.add(temp_room)
                    neighbors = my_map[temp_room].items()

                    for room in neighbors:
                        path_copy = current_path[:]
                        path_copy.append(room)
                        queue.enqueue(path_copy)
            
            for i in range(1, len(current_path)):
                player.travel(current_path[i][0])
                traversal_path.append(current_path[i][0])

            prev_room = current_path[-2][1]
            cur_room = player.current_room.id
        

            

        # path_copy = traversal_path[:]
        # path_copy.reverse()

        # for step in path_copy:
        #     if step == 'n':
        #         back_step = 's'
        #         player.travel(back_step)
        #         traversal_path.append(back_step)
        #     elif step == 'e':
        #         back_step = 'w'
        #         player.travel(back_step)
        #         traversal_path.append(back_step)
        #     elif step == 's':
        #         back_step = 'n'
        #         player.travel(back_step)
        #         traversal_path.append(back_step)
        #     elif step == 'w':
        #         back_step = 'e'
        #         player.travel(back_step)
        #         traversal_path.append(back_step)

        #     cur_room = player.current_room.id

        #     exits = my_map[cur_room]

        #     if '?' in exits.values():
        #         backtracked = True
        #         break
    



# Repeat until all rooms are visited

# When you move into a room, update the previous room
# Exiting DFT and running BFS
# Stop BFS and run DFT
# Convert BFS path into directions for your traversal_path

# the maze is known (we could run traversal/search on it)
# the step-by-step path is unknown (we must build on top of our traversal/search)

# Is it a valid exit?
# Make sure it's not where you just came from


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
