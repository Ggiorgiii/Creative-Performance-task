import math

def binomial_probability(n, p, k_min):
    """Calculate probability that X >= k_min where X ~ Binomial(n, p)."""
    total = 0
    for k in range(k_min, n + 1):
        c = math.comb(n, k)
        term = c * (p ** k) * ((1 - p) ** (n - k))
        total += term
    return total


def main():
    print("Liar's Bar Probability Calculator \n")

    
    total_players = 4
    dice_per_player = 5
    player_dice = [dice_per_player] * total_players
    total_dice = sum(player_dice)

    print(f"There are {total_players} players and {total_dice} dice total.\n")

    
    your_dice_str = input("Enter your 5 dice values separated by spaces (example: 2 4 6 6 1): ").strip()
    your_dice = [int(x) for x in your_dice_str.split()]
    your_counts = {face: your_dice.count(face) for face in range(1, 7)}

    print("\nWho is playing first?")
    print("1 = You")
    print("2 = Player to your left")
    print("3 = Player opposite you")
    print("4 = Player to your right")
    starter = int(input("Enter number of starting player (1-4): ").strip())
    print(f"Player {starter} starts the round.\n")

    while True:
        print(f"\n Total dice currently in play: {total_dice}")
        print("Enter the current claim (example: '7 4' ).")

        try:
            quantity, face = map(int, input("Claim (quantity face): ").split())
        except ValueError:
            print("Invalid input, try again.")
            continue

        known = your_counts.get(face, 0)
        unknown_dice = total_dice - len(your_dice)
        p = 1 / 6
        needed_from_unknown = max(0, quantity - known)

        prob_true = binomial_probability(unknown_dice, p, needed_from_unknown)
        prob_false = 1 - prob_true

        print("\n--- Probability Results ---")
        print(f"You have {known} of face {face}.")
        print(f"Unknown dice: {unknown_dice}")
        print(f"Need at least {needed_from_unknown} more of that face.")
        print(f"Chance claim is TRUE:  {prob_true*100:.2f}%")
        print(f"Chance claim is FALSE: {prob_false*100:.2f}%")

        print("\nDid someone check the claim?")
        checked = input("Type 'y' for yes (claim checked), 'n' for no (next claim): ").strip().lower()

        if checked == "y":
            print("\nWho lost a die?")
            print("1 = You / 2 = Left / 3 = Opposite / 4 = Right")
            try:
                loser = int(input("Enter number of losing player (1-4): ").strip())
                if 1 <= loser <= 4:
                    if player_dice[loser - 1] > 0:
                        player_dice[loser - 1] -= 1
                        total_dice = sum(player_dice)
                        print(f"Player {loser} now has {player_dice[loser - 1]} dice.")
                    else:
                        print("That player already has 0 dice.")
                else:
                    print("Invalid player number.")
            except ValueError:
                print("Invalid input, no dice removed.")
        else:
            print("No one checked, continuing with same dice count.")
            
        if total_dice <= 1:
            print("\nGame over — only one die remains!")
            break
        
        cont = input("\nDo you want to check another claim? (y/n): ").strip().lower()
        if cont != "y":
            print("\nThanks for using Liar's Bar Probability Calculator. Good luck!")
            break

if __name__ == "__main__":
    main()
