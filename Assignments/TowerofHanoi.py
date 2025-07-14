
# Dictionary to store results of previous computations
memo = {}


def TowerOfHanoi(n, source_rod, auxiliary_rod, destination_rod):
    # Check if result for the current state is already computed
    if (n, source_rod, auxiliary_rod, destination_rod) in memo:
        return memo[(n, source_rod, auxiliary_rod, destination_rod)]

    # Base case: If only one disk, move it directly
    if n == 1:
        move = [(source_rod, destination_rod)]
        memo[(n, source_rod, auxiliary_rod, destination_rod)] = move
        print(f"Move disk 1 from {source_rod} to {destination_rod}")
        return move

    # Recursive case:
    # Step 1: Move n-1 disks from source to auxiliary, using destination as buffer
    moves1 = TowerOfHanoi(n - 1, source_rod, destination_rod, auxiliary_rod)

    # Step 2: Move the nth disk from source to destination
    move2 = [(source_rod, destination_rod)]
    print(f"Move disk {n} from {source_rod} to {destination_rod}")

    # Step 3: Move n-1 disks from auxiliary to destination, using source as buffer
    moves3 = TowerOfHanoi(n - 1, auxiliary_rod, source_rod, destination_rod)

    # Combine all moves
    all_moves = moves1 + move2 + moves3

    # Store the result in memo
    memo[(n, source_rod, auxiliary_rod, destination_rod)] = all_moves

    return all_moves


# Example usage:
n = 30
TowerOfHanoi(n, "A", "B", "C")
