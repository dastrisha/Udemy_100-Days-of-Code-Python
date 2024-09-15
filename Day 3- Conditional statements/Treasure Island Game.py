
"""Exercise 3: Treasure Island Project: Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.Use the flow chart linked here to create the game logic.

Once you've completed the project, you can always extend the game and make it more interesting!"""

Player_name = input("What is your name?: ").lower()
print(f"Welcome to the  Treasure Island, {Player_name}!\n Please follow the direction to seek the treasure you are looking for.This journey is difficult, but if you are brave my friend, you will get what you deserve or this Game will be Over.\n")
print()
press_enter = input("Type enter to begin! ").lower()
print()
if press_enter=="enter":
    print("Walk straight, you will see sign board to take left or right.\nWalk a little...\nJump a litle.\n.Few more miles...\nVoila! Signboard!")
    print()
    signboard= input("Do you chose RIGHT Or LEFT? ").lower()
    if signboard == "right":
        print("You entered a forest. Beware of the wild animals. They are cute but they may get angry if you annoy them too much!\nYou got luck and did'nt get chased by wild animals.Time to make the next best choice!")
        print()
        signboard_right = input("Castle or Hut? ").lower()
        if signboard_right == "castle":
            print("This castle is haunted. Run for your life and go home. GAME OVER!")
            print()
        elif signboard_right =="hut":
            print ("You are hunble since you chose a hut.  A true seeker of the treasure indeed! Now Break the floor to find the right door.")
            print()
            door = input("Which color door you wish to enter? Red, Green or Blue? ").lower()
            print()
            if door == "red":
                print("Sorry, no treasure but you get a duck to take home. GAME OVER!")
                print()
                print(r''' ,;;,.
                      ;;;;;;
                      ;; ;; ;
                     _;; o;o;
                    / __`` ` \
                    `.\ \    `-...--.
                      .\,\      ./---'
                       .\)'.___.'
                        .\_.-
                         ---'  BP''')
                print()
            elif door == "blue":
                print("Life is all about trying again from the beginning. GAME OVER!")
                print()
            elif door == "green":
                print(f"With map in hand and hearts held high,\nWe hunt beneth the endless sky./nThe treasure waits, both bold and true,\nVictory shines in gold for you!\n\nCongratulations,{Player_name}!\n")
                print(r'''.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-''')
            else :
                print("Invalid input. Try again or accept you lose!")
                print()

    elif signboard =="left":
        print("You found a Sloth! That is all you get to take home. GAME OVER!")
        print()
        print(r'''
              =====(((=))=====(=)))===========
      " `,      |' /
      /"/        |""
     """|        \"|
     |"||        " "
     "" "        |"|\
    /""~\\.      /" ""~,
   ""~""""`"",~`~"!!"!" \
   /"""""/""! "~""" "" "~",
  //\""!!""~"!"!"\"""/~!~, C~"~P
 // !!"""""! "~ " !!"!! "," O o"~
 ||   !!"!!~!!~||"  !     "" Y ""
 \\     !  !  !            `"U"'
  \\
   \\  0))
    \`-~/~
     `~
              ''')
        print()
    else:
        print("Invalid input. Try again or accept you lose!")
        print()
else:
    print("Invalid input. Try again or accept you lose!")
    print()
