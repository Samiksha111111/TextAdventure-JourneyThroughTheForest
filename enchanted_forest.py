name = input("Type your name: ")
print(f"Welcome to the Enchanted Forest, {name}!")
print("A place where magic thrives and danger lurks in every shadow.")
print("Your goal is simple: survive and uncover the secrets of this mystical place.")
print("But remember, every choice you make could lead you to glory—or disaster.")

# First choice: Left or Right
answer = input("You stand at the edge of a mysterious forest, thick with ancient trees that seem to whisper secrets to one another. The path in front of you forks into two, disappearing into the gloom. One arrow points left, marked with a strange symbol of a crescent moon, and the other points right, towards a glowing orb. Which path will you choose? (left/right) ").lower()

if answer == "left":
    # Left path narrative
    answer = input("You take the Crescent Moon Trail, and soon the trees around you grow denser, their branches intertwining to form a canopy overhead. As the light fades, a cool mist begins to rise, swirling around your feet. Suddenly, you hear a soft melody in the distance, like the song of a siren calling you deeper into the woods. You spot a shimmering lake ahead, its waters dark and still, with a small wooden boat docked on the shore. Will you board the boat or walk around the lake? (boat/walk) ").lower()

    if answer == "boat":
        print("You push the boat into the lake, and the water ripples unnaturally. Halfway across, the siren's song grows louder, but its sweetness turns menacing. Without warning, a massive sea creature rises from the depths, pulling you under the water. You lose!")
    elif answer == "walk":
        print("You decide to stay on solid ground, trekking around the lake’s edge. The mist thickens, but you keep walking. Hours pass, and your legs grow weary, but you eventually find a hidden grove where a magical fountain flows. You drink from it, and your strength returns. You continue your journey.")
    else:
        print("Invalid option. You lose!")

elif answer == "right":
    # Right path narrative
    answer = input("The Glowing Orb Path feels warmer, more inviting, but with every step, the glow dims. The orb hovers ahead, always just out of reach. Soon, you find yourself standing in front of an ancient stone bridge, arching over a deep ravine. The bridge looks old, its stones cracked and weathered. A faint tremor shakes the ground beneath your feet. Will you cross the bridge or turn back? (bridge/back) ").lower()

    if answer == "bridge":
        print("You step cautiously onto the bridge, feeling it wobble under your weight. Halfway across, a gust of wind howls through the ravine, causing the bridge to sway violently. With one final lurch, the stones crumble beneath you, and you fall into the abyss below. You lose!")
    elif answer == "back":
        print("You retrace your steps and notice a hidden path, obscured by vines. You follow it and soon find a mysterious stranger standing by a campfire, their face hidden by a hood. They offer you a deal: answer their riddle, and they will show you the way to the treasure.")
        
        # The Riddle
        riddle_answer = input('The stranger asks: "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?" (Type your answer) ').lower()

        if riddle_answer == "echo":
            print("The stranger smiles and steps aside, revealing a hidden treasure chest overflowing with gold and ancient relics. You win!")
        else:
            print("The stranger frowns, and the campfire flickers out. As darkness envelops you, you feel a chill in the air. Suddenly, the ground beneath you crumbles, and you fall into a hidden pit. You lose!")
    else:
        print("Invalid option. You lose!")
else:
    print("Invalid option. You lose!")

print(f"Thank you for trying your luck in the Enchanted Forest, {name}! Every choice shapes your fate, so choose wisely on your next adventure.")
