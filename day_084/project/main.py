"""
╔══════════════════════════════════════╗
║        TIC TAC TOE  ✕ ○             ║
║         Python Day 084              ║
╚══════════════════════════════════════╝
  A 2-player command-line game.
"""


# ── Helpers ───────────────────────────────────────────────────────────────────

def clear():
    # ANSI escape: move cursor to top-left and erase the entire screen.
    print("\033[H\033[2J\033[3J", end="", flush=True)


# ── Board ─────────────────────────────────────────────────────────────────────

def make_board():
    """Return a fresh board: 10 spaces, index 0 unused so positions 1-9 match indices."""
    return [" "] * 10


def display_board(board):
    """Print a styled board with position hints on the side."""
    X_STYLED = "\033[1;91m X \033[0m"   # bold red
    O_STYLED = "\033[1;94m O \033[0m"   # bold blue

    def cell(val):
        if val == "X":
            return X_STYLED
        if val == "O":
            return O_STYLED
        return f"\033[2m {val} \033[0m"

    # Substitute numbers as position hints for empty cells
    display = [" "] + [
        board[i] if board[i] != " " else str(i)
        for i in range(1, 10)
    ]

    print()
    print("  ╔═══╦═══╦═══╗       ╔═══╦═══╦═══╗")
    print(f"  ║{cell(display[1])}║{cell(display[2])}║{cell(display[3])}║       ║\033[2m 1 \033[0m║\033[2m 2 \033[0m║\033[2m 3 \033[0m║")
    print("  ╠═══╬═══╬═══╣       ╠═══╬═══╬═══╣")
    print(f"  ║{cell(display[4])}║{cell(display[5])}║{cell(display[6])}║       ║\033[2m 4 \033[0m║\033[2m 5 \033[0m║\033[2m 6 \033[0m║")
    print("  ╠═══╬═══╬═══╣       ╠═══╬═══╬═══╣")
    print(f"  ║{cell(display[7])}║{cell(display[8])}║{cell(display[9])}║       ║\033[2m 7 \033[0m║\033[2m 8 \033[0m║\033[2m 9 \033[0m║")
    print("  ╚═══╩═══╩═══╝       ╚═══╩═══╩═══╝")
    print("      Game Board            Positions")
    print()


# ── Game Logic ────────────────────────────────────────────────────────────────

WIN_COMBOS = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),   # rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),   # columns
    (1, 5, 9), (3, 5, 7),              # diagonals
]


def check_win(board, marker):
    return any(
        board[a] == board[b] == board[c] == marker
        for a, b, c in WIN_COMBOS
    )


def check_draw(board):
    return all(board[i] != " " for i in range(1, 10))


def get_move(board, player_name, marker):
    """Ask the current player for a valid move (1–9)."""
    color = "\033[1;91m" if marker == "X" else "\033[1;94m"
    reset = "\033[0m"

    while True:
        try:
            move = int(input(
                f"  {color}{player_name} ({marker}){reset} → choose a position (1-9): "
            ))
            if move < 1 or move > 9:
                print("  \033[33m⚠  Please enter a number between 1 and 9.\033[0m")
            elif board[move] != " ":
                print("  \033[33m⚠  That spot is already taken! Try another.\033[0m")
            else:
                return move
        except ValueError:
            print("  \033[33m⚠  Invalid input — please enter a number.\033[0m")


# ── Screens ───────────────────────────────────────────────────────────────────

def banner():
    print("\033[1;96m")   # bold cyan
    print("  ╔══════════════════════════════════════╗")
    print("  ║                                      ║")
    print("  ║      T I C   T A C   T O E           ║")
    print("  ║            ✕   ○                     ║")
    print("  ║                                      ║")
    print("  ╚══════════════════════════════════════╝")
    print("\033[0m")


def get_player_names():
    print("  Let's set up the players!\n")
    p1 = input("  Enter name for Player 1 (X): ").strip() or "Player 1"
    p2 = input("  Enter name for Player 2 (O): ").strip() or "Player 2"
    return p1, p2


def show_result(board, winner_name, marker):
    display_board(board)
    if winner_name:
        color = "\033[1;91m" if marker == "X" else "\033[1;94m"
        print(f"  {color}🎉  {winner_name} ({marker}) wins!\033[0m")
    else:
        print("  \033[1;93m🤝  It's a draw! Well played, both!\033[0m")
    print()


def play_again_prompt():
    ans = input("  Play again? (y / n): ").strip().lower()
    return ans == "y"


# ── Main Game Loop ────────────────────────────────────────────────────────────

def play_game(p1_name, p2_name):
    board = make_board()

    players = [(p1_name, "X"), (p2_name, "O")]
    turn = 0

    while True:
        current_name, current_marker = players[turn % 2]

        clear()
        banner()
        display_board(board)
        print(f"  Turn {turn + 1}  |  {current_name}'s go\n")

        move = get_move(board, current_name, current_marker)
        board[move] = current_marker

        if check_win(board, current_marker):
            clear()
            banner()
            show_result(board, current_name, current_marker)
            return current_name   # winner

        if check_draw(board):
            clear()
            banner()
            show_result(board, None, None)
            return None           # draw

        turn += 1


def main():
    clear()
    banner()
    p1_name, p2_name = get_player_names()

    scores = {p1_name: 0, p2_name: 0, "Draws": 0}

    while True:
        winner = play_game(p1_name, p2_name)

        if winner:
            scores[winner] += 1
        else:
            scores["Draws"] += 1

        # Scoreboard
        print("  ── Scoreboard ─────────────────────────")
        print(f"  \033[1;91m{p1_name} (X)\033[0m : {scores[p1_name]}")
        print(f"  \033[1;94m{p2_name} (O)\033[0m : {scores[p2_name]}")
        print(f"  Draws       : {scores['Draws']}")
        print("  ───────────────────────────────────────\n")

        if not play_again_prompt():
            clear()
            banner()
            print("  Thanks for playing! 👋\n")
            print("  Final scores:")
            print(f"    {p1_name}: {scores[p1_name]} win(s)")
            print(f"    {p2_name}: {scores[p2_name]} win(s)")
            print(f"    Draws:    {scores['Draws']}\n")
            break


if __name__ == "__main__":
    main()