#Roblox Man Dating Simulator

define mc = Character("[name]")
define g = Character("[name 2]")
define o = Character("[Josh]")
define d = Character("[Cashier]")
define s = Character("[???]")
define h = Character("[Hatsune Miku]")
define a = Character("[yippee]")
define t = Character("[Staff 1]")
define idk = Character ("[Staff 2]")



label start: 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    $ name = renpy.input("What is your name?")
    $ name = name.strip()
    
call pronounselection
jump intro

label intro:

"You are walking down the streets of Boxburg."
"You have never been in this world before."
mc "yippee"

    return
