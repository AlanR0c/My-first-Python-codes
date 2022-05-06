#Final Project#

#Labyrinthian - Multiple Choice Game

#Notice that in order for the computer to interpret and display the ASCII art properly, you must place it between 3 single quotes, like so'''  '''. If it was placed between ' ' or " ", it would't display it on the console, but an error would be displayed instead. Basically what these 3 single quotes do is allow you to create multiple lines of a string(multi block string), essentially.  

print('''
    _.-""}
      / "" ;
  .-"` __] ',               ___
  I_ ""__.`-,;             |   |
    I_.,-"ii"{             !___!
    | ||  ||  |        ,    | |
    | ||  ||  |       .;    | |
    | ||  ||  |       | \   | |
    | ||  ||  |       |  |  | |
    | ||  ||  |       |  |  | |   __
    | ||  ||  |       |  |  | |  |  |
    | ||  ||  |   ;|  |  |  | |  |  |
    | ||  ||  |"\_/`,_|  |  | |  |  |  ___.--""`\
    | ||  ||  |       |  |\.| |=,|  |""          `,
    | ||  ||  |       |  |  | |  |  |____________.-+.__
   _:_!|_,'!__!       |  |  | |_,!  !         __,I   `"|
  :     |      `-""`,.!__!-,!_!_ '--'`,_,--"""         |
  |     ;___          `"-.-'    `,_.-'"            _..-'
   `-._ |   """--,,_     |`""-.--'|         __.--""
       `"--..__     ""--.|    |   |_,_  _.-'
               ""--.._   `-,__!_.-' _,""      fsc
                      ""--,____.--'"
''')

print("Welcome to Labyrinthian, one of the most dangerous locations in Skyrim. \n\n Your mission is to acquire the Staff of Magnus from Morokei, an incredibly powerful Dragon Priest inside Labyrinthian.")

print('''
After the chaos caused by Ancano at the College of Winterhold trying(when he tried) to harness energy of the Eye of Magnus, ye were sent to retrieve the only weapon that could destroy this unprecedent threat to Skyrim and its inhabitants. You have endured a long an treacherous journey across the most remote forests and mountains of Skyrim and now you find yerself before the doors leading into the dungeon(s) where you have been told the Staff of Magnus might be found. After catching yer breath for a while, you finally decide to go through the doors and into the mysterious and intriguing ruins. Closing the doors behind, you find yourself inside a stony hall. You notice an iron door on your right-hand side, (and)you also realise that a wide corridor lies ahead.
''')

decision1 = input("Would ye like to check what's beyond the iron door or proceed through the wide corridor? Iron door or wide corridor? \n\n")

lower_case_decision1 = decision1.lower()
#Alternatively, the .lower() function could have been used in the "decision1" variable, thus nullifying the need to create the variable lower_case_decision1.

if lower_case_decision1 == "wide corridor":
  print("After killing some Dragons Priests, looting their bodies and a few burial urns that were lying around, you finally make to a narrow bridge. As you cautiosly walk on the narrow bridge, you look downwards and, to yer surprise, you can't see a thing, it's too dark. The bridge leads you to a dimly-torched-lit place where ye can barely make two ways, one on your left-hand side and the other on yer right-hand side.")
  
  decision2 = input("Which way are ye going to take? Left or right? \n\n")

  lower_case_decision2 = decision2.lower()
  
  if lower_case_decision2 == "left":
    print("After what it seemed like hours, ye finally spot a great rocky portal with some ancient language and symbols carved on it. 'This is it', ye think. 'Morokei's certainly beyond this bloody portal, I got to tread rather carefully from now on'. Squinting in the darkeness and keeping yer ears peeled to any weird noise that could expose Morokei's presence, you move on as stealthily as ye can. When ye look to yer right, however, ye find yer face to face with Morokei, who casts a powerful spell on you, thus draining all yer magicka. 'I must react fast or I'll be dead in a second', you desperately tell yerself. Since the beast is really close two ya, you only got two options: counter attack Morokei with a destruction spell, either the Thunderbolt spell or the Ice Spike spell, which would render him weaker and probably cause some real damage to his magicka, or unsheathe yer holy sword and behead the ancient dragon priest right on the spot.")
    
    decision3 = input("What do ye do? Cast the Thunderbolt? Cast the Ice Spike? Use Holy Sword: \n\n")

    lower_case_decision3 = decision3.lower()

    if lower_case_decision3 == "cast the thunderbolt" or lower_case_decision3 == "cast the ice spike":
      print("As ye find yerself face to face with Morokei, yer instant and instinctive reaction is to try and cast a destruction spell on him, that'd probably not only deal a great deal of physical damage but also a massive magicka damage; 'The ancient Dragon Priest would succumb in no time', ye tell yerself. However, as Morokei had cast a powerful spell on ye, a few seconds earlier, ye bitterly realise it had thoroughly depleted yer magicka, thus rendering yer spell to nothing but a little spec of light. The last thing ye hear is Morokei's evil laughter and yer blinded by flash of light. Ye feel a terribly sharp and painful burning sensation, Morokei had pulverised ye with a Fireball spell. \nGame over.")
    else:
      print("Ye wisely realise that Morokei had fully drained yer magicka with that spell, and therefore, ye decide to unsheathe yer holy sword. With a precise and deadly swing, ye behead Morokei. As ye can still feel yer heart racing, ye watch the ancient dragon priest's head roll in the air, when a sudden and blinding light dazzles ye for a few seconds. Ye hear a metal clatter, and as ye recover yer vision, ye spot the Staff of Magnus and a blueish mask lying on the floor. Relieved and thankful ye had not used magicka on Morokei, ye reach for the Staff of Magnus. 'Now we can put an end to Ancano's evil plans, whatever they might be', ye sigh in relief. As ye pick the blueish mask up, ye realise it vibrating and ye can feel it's a powerful magical mask, and not just an ordinary one. Ye return to Winterhold and, thanks to the power of the Staff of Magnus, ye defeat Ancano. However, short afterwards ye realise that despite that tremendous victory, ye also had a great loss. The Arch Mage Savos Aren lost his life in the battle against Ancano. A great loss, indeed. Winterhold needs a new Arch-Mage, and to yer surprise, Tolfdir says that you're a valiant wizard and due to yer efforts to retrieve the Staff Of Magnus and defeat Ancano, yer the one who should be chosen to be the new Winterhold's leader.")
  else:
    print("Most unfortunately, the way on yer right-hand side led ye to yer untimely demise: without realising, ye step on a fake floor trap and ye fall into an abyss. \nGame over.")

else:
  print("Yer skull gets pierced through by an iron spear, a deadly trap. \nGame over.")
