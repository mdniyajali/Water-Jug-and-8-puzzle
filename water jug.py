from collections import deque

class WaterJug:
    def __init__(self, initial_state=(0, 0), goal_state=(2, 0)):
        # Define the initial and goal states
        self.initial_state = initial_state  # Initial state: (0, 0)
        self.goal_state = goal_state  # Goal state: (2, 0)

    def successors(self, state):
        X, Y = state
        succ = []

        # Action 1: Fill Jug X
        if X < 4:
            succ.append((4, Y))

        # Action 2: Fill Jug Y
        if Y < 3:
            succ.append((X, 3))

        # Action 3: Empty Jug X
        if X > 0:
            succ.append((0, Y))

        # Action 4: Empty Jug Y
        if Y > 0:
            succ.append((X, 0))

        # Action 5: Pour from X to Y
        if X > 0 and Y < 3:
            transfer = min(X, 3 - Y)
            succ.append((X - transfer, Y + transfer))

        # Action 6: Pour from Y to X
        if Y > 0 and X < 4:
            transfer = min(Y, 4 - X)
            succ.append((X + transfer, Y - transfer))

        return succ

    def xbfs(self, initial_state, goal_state):
        open_queue = deque([initial_state])  # Queue of states to explore
        closed_set = set()  # Set of explored states
        predecessor_map = {initial_state: None}  # Map to track predecessors

        while open_queue:
            # Step 1: Pop from OPEN and add it to CLOSED
            current_state = open_queue.popleft()
            closed_set.add(current_state)

            # Step 2: Goal test
            if current_state == goal_state:
                # Goal found, reconstruct path
                return self.reconstruct_path(predecessor_map, current_state)

            # Step 3: Generate successors and add to OPEN if not in OPEN or CLOSED
            for succ in self.successors(current_state):
                if succ not in closed_set and succ not in open_queue:
                    open_queue.append(succ)
                    predecessor_map[succ] = current_state  # Record the predecessor

        return None

    def xdfs(self, initial_state, goal_state):
        open_stack = [initial_state]  # Stack of states to explore
        closed_set = set()  # Set of explored states
        predecessor_map = {initial_state: None}  # Map to track predecessors

        while open_stack:
            # Step 1: Pop from OPEN
            current_state = open_stack.pop()

            # Step 2: Goal test
            if current_state == goal_state:
                # Goal found, reconstruct path
                return self.reconstruct_path(predecessor_map, current_state)

            # Step 3: Add to CLOSED if not already explored
            if current_state not in closed_set:
                closed_set.add(current_state)

                # Generate successors and add to OPEN if not in OPEN or CLOSED
                for succ in self.successors(current_state):
                    if succ not in closed_set and succ not in open_stack:
                        open_stack.append(succ)
                        predecessor_map[succ] = current_state  # Record the predecessor

        return None

    def reconstruct_path(self, predecessor_map, goal_state):
        path = []
        current_state = goal_state
        while current_state is not None:
            path.append(current_state)
            current_state = predecessor_map[current_state]
        path.reverse()  # Reverse to get the path from start to goal
        return path

    def run(self):
        # Prompt user for method choice
        choice = input("Choose method to find goal state (1 for BFS, 2 for DFS): ").strip()
        if choice == "1":
            path = self.xbfs(self.initial_state, self.goal_state)
            method = "BFS"
        elif choice == "2":
            path = self.xdfs(self.initial_state, self.goal_state)
            method = "DFS"
        else:
            print("Invalid choice. Please choose 1 or 2.")
            return

        if path is None:
            print(f"Goal not found using {method}.")
        else:
            print(f"Goal found using {method}, path: {path}")

# Create an instance of the WaterJug class and run it
sol = WaterJug()
sol.run()