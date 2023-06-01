class Leaderboard:
    def __init__(self):
        self.scores = {}

    def add_score(self, player, score):
        if player in self.scores:
            self.scores[player] += score
        else:
            self.scores[player] = score

    def remove_player(self, player):
        if player in self.scores:
            del self.scores[player]

    def get_top_players(self, num_players):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:num_players]


# Example usage:
board = Leaderboard()

# Add scores
board.add_score("Alice", 100)
board.add_score("Bob", 200)
board.add_score("Alice", 50)
board.add_score("Charlie", 300)

# Remove a player
board.remove_player("Bob")

# Get the top 2 players
top_players = board.get_top_players(2)
print("Top Players:")
for player, score in top_players:
    print(f"{player}: {score}")