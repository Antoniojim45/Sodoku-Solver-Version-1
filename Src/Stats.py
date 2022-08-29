class Stats():
    """
    a class that holds the premade board and an empty duplicate. 
    """
    def __init__ (self):
        self.example_board = [
            [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
            [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
            [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

            [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
            [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
            [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],
 
            [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
            [6, 7, -1,   1, -1, 5,   -1, 4, -1],
            [1, -1, 9,   -1, -1, -1,   2, -1, -1]
        ]

        self.store_value = [ [0 for i in range(9)] for j in range(9)]