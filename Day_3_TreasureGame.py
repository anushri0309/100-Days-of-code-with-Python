print('''                   _.--.
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
                    '-.||_/.-'
  ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a=input("Your at the cross road where do you want to go Left or right")
if(a=="right" or "Right"):
    print("You came to the island")
    
    b=input("Type wait to wait for the boat type swim to swim")
    
    if(b=="wait" or "Wait"):
        
        c = input("Which door you want:RED YELLOW GREEN")
        if c == "RED" or "red" or"green":
            print("You are eaten by a bare>Game Over")
        else:
            print("CONGRATULATIOS! YOU GOT THE TREASURE ")

    else:
        print("you drounded in the see.Game Over")
else :
    print("You jumped.Game Over")
