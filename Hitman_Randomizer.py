import random

print("___    ___     ___    ___________    ___        __                     ___    __")
print("\ /    \ /     \ /    |/  | |  \|    \  \      / /         /\         \  \   \/")
print("| |    | |     | |        | |        |\  \    // |        /. \        ||\ \  ||")
print("| |____| |     | |        | |        ||\  \  //| |       // \ \       || \ \ ||")
print("| |    | |     | |        | |        || \  \// | |      //___\ \      ||  \ \||")
print("| |    | |     | |        | |        ||  \  /  | |     //     \ \     ||   \  |")
print("/_\    /_\     /_\        /_\       /_\   \/   /_\    /_\     /__\   /__\   \_|")
print("")
print("                                    /|")
print("                                    \\  \`.")
print("                               ,'/  ||   ) `.                          ")
print("                             ,' (   //,-'_,-'    ,                         ")
print("                       .    `-._`-.  |  (_____,-'/                        ")
print("                       \`-._____)  | | ,-'-.    /")
print("                        \    ,-'-. | |/     ) ,'")
print("                         `. (     \|     _,','")
print("                           `.`._")

maps = ['Paris', 'Sapienza', 'Marrakesh', 'Bangkok', 'Colorado', 'Hokkaido',
        "Hawke's Bay", 'Miami', 'Santa Fortuna', 'Mumbai', 'Whittleton Creek', 'Isle of Sgail', 'New York', 'Haven Island',
        'Dubai', 'Dartmoor', 'Berlin', 'Chongqing', 'Mendoza', 'Ambrose Island']

concealed_weapons = ['"El Matador"', '"Rude Ruby"', 'Concept 5', 'Custom 5MM', 'Custom 5MM DTI',
                     'HWK21', 'HWK21 Covert', 'HWK21 MK II', 'HWK21 Pale Homemade Silencer', 'ICA DTI Stealth',
                     'ICA19', 'ICA19 Black Lily', 'ICA19 Chrome', 'ICA19 Classicballer', 'ICA19 F/A',
                     'ICA19 F/A Stealth', 'ICA19 F/A Stealth "Ducky" Edition', 'ICA19 Goldballer', 'ICA19 Iceballer', 'ICA19 Shortballer', 'ICA19 Silverballer',
                     'ICA19 Silverballer MK II', 'Kalmer 1 - Tranquilizer', 'Kalmer 2 - Tranquilizer', 'Krugermeier 2-2', 'Krugermeier 2-2 Dark',
                     'Krugermeier 2-2 Silver', 'Sieker 1', 'Striker', 'Striker V3', 'The Ducky Gun',
                     'The Floral Baller', "The Serpent's Tongue", 'The Taunton Dart Gun', 'DAX X2 Covert', 'Slapdash SMG']

categories = ['Containers', 'Pistols', 'SMGs', 'Shotguns', 'Assault Rifles', 'Sniper Rifles', 'Melee', 'Tools', 'Distractions', 'Poisons', 'Explosives']

cat_minus_containers = ['Pistols', 'SMGs', 'Shotguns', 'Assault Rifles', 'Sniper Rifles', 'Melee', 'Tools', 'Distractions', 'Poisons', 'Explosives']

cat_minus_guns = ['Containers', 'Melee', 'Tools', 'Distractions', 'Poisons', 'Explosives']

cat_minus_containers_and_guns = ['Melee', 'Tools', 'Distractions', 'Poisons', 'Explosives']

containers = ['Arctic Toolbox', 'Black Leather Briefcase', 'Chinese Briefcase', 'Golden Briefcase', "Hunter's Briefcase",
              'ICA Briefcase', 'ICA Briefcase MK III', 'ICA Executive Briefcase', 'ICA Executive Briefcase Mk II', 'Sieger 300 Sniper Case',
              'Toolbox']

pistols = ['"El Matador"', '"Rude Ruby"', 'Concept 5', 'Custom 5MM', 'Custom 5MM DTI',
            'HWK21', 'HWK21 Covert', 'HWK21 MK II', 'HWK21 Pale Homemade Silencer', 'ICA DTI Stealth',
            'ICA19', 'ICA19 Black Lily', 'ICA19 Chrome', 'ICA19 Classicballer', 'ICA19 F/A',
            'ICA19 F/A Stealth', 'ICA19 F/A Stealth "Ducky" Edition', 'ICA19 Iceballer', 'ICA19 Goldballer', 'ICA19 Shortballer', 'ICA19 Silverballer',
            'ICA19 Silverballer MK II', 'Kalmer 1 - Tranquilizer', 'Kalmer 2 - Tranquilizer', 'Krugermeier 2-2', 'Krugermeier 2-2 Dark',
            'Krugermeier 2-2 Silver', 'Sieker 1', 'Striker', 'Striker V3', 'The Ducky Gun',
            'The Floral Baller', "The Serpent's Tongue", 'The Taunton Dart Gun']

smgs = ['Brine-Damaged SMG', 'DAK Black Covert', 'DAK Gold Covert', 'DAK X2 Covert', 'ICA SMG Raptor Covert',
       'Militia-Issued HX-10 SMG', 'SMG Raptor Rude Ruby Covert', 'Slapdash SMG', 'TAC-SMG', 'TAC-SMG Covert',
       'TAC-SMG MK II', 'TAC-SMG S']

shotguns = ['Bartoli 12G Short H', 'Bartoli Hunting Shotgun Deluxe', 'Enram HV', 'Enram HV CM', 'Enram HV Covert',
            'ICA Tactical Shotgun', 'ICA Tactical Shotgun Covert (Black)', 'ICA Tactical Shotgun Covert (White)', 'Sawed-Off Bartoli 12G', 'The Maximalist Shotgun']

assault_rifles = ['RS-15', 'Shashka A33 Gold', 'Shashka A33 H', 'Sieger AR552 Tactical', 'TAC-4 AR Auto', 'TAC-4 AR Desert',
                  'TAC-4 AR MK II', 'TAC-4 AR Stealth', 'TAC-4 S/A', 'TAC-4 S/A Jungle', 'The Shashka Beast']

sniper_rifles = ['Bartoli Woodsman Hunting Rifle', 'Druzhina 34', 'Druzhina 34 DTI', 'Druzhina 34 ICA Arctic', 'Hackl Leviathan Sniper Rifle Covert',
                 'Hackl Sniper Rifle Covert "Ducky" Edition', 'ICA Bartoli Woodsman Rifle Covert', 'Jaeger 7', 'Jaeger 7 Covert', 'Jaeger 7 Green Eye',
                 'Jaeger 7 Lancer', 'Jaeger 7 MK II', 'Jaeger 7 Tiger', 'Jaeger 7 Tuatara', 'Sieger 300',
                 'Sieger 300 Advanced', 'Sieger 300 Arctic', 'Sieger 300 Ghost', 'Sieger 300 Tactical', 'Sieger 300 Viper',
                 'The Golden Dragon', 'The Majestic', 'The White Ruby Rude 300 Sniper Rifle']

non_briefcase_melees = ['Antique Curved Knife', 'Banana', 'Bat Shuriken', 'Blueberry Muffin',
         'Burj Al-Ghazali Snowglobe', 'Claw Hammer', 'Combat Knife', 'Concealable Baton',
         'Concealable Knife', 'Crystal Ball', 'Earphones', 'Feather Duster', 'Fiber Wire',
         'Fiber Wire Classic', 'Fish', 'Fishing Line', 'Hobby Knife',
         'Hook', 'IO Elite S2VP Earphones', 'Ice Pick',
         'Janbiya', 'Kukri Knife', 'Measuring Tape', 'Meaty Bone', 'Okinawan Tonfa',
         'Piton', 'Quickdraw', 'Sacrificial Knife', 'Shuriken',
         'Small Goldbar', 'Snowball', 'Tanto', "The Black Almond's Dagger", "The Cat's Claw",
         'The Straitjacket Belt', 'Violin']

melees = ['A New Bat', 'Antique Curved Knife', 'Banana', 'Bat Shuriken', 'Blueberry Muffin',
         'Broadsword', 'Burj Al-Ghazali Snowglobe', 'Claw Hammer', 'Combat Knife', 'Concealable Baton',
         'Concealable Knife', 'Crystal Ball', 'Earphones', 'Feather Duster', 'Fiber Wire',
         'Fiber Wire Classic', 'Fish', 'Fishing Line', 'HF Championship Bat', 'Hobby Knife',
         'Hook', 'ICA Combat Axe', 'IO Elite S2VP Earphones', 'Ice Axe', 'Ice Pick',
         'Janbiya', "Jarl's Pirate Saber", 'Kukri Knife', 'Kukri Machete', 'Mace',
         'Masamune', 'Measuring Tape', 'Meaty Bone', "Nne Obara's Machete", 'Okinawan Tonfa',
         'Ornate Scimitar', 'Piton', 'Quickdraw', 'Sacrificial Knife', 'Shuriken',
         'Small Goldbar', 'Snowball', 'Tanto', "The Black Almond's Dagger", "The Cat's Claw",
         'The Iridescent Katana', 'The Proud Swashbuckler', 'The Straitjacket Belt', 'Violin',
         'Walking Cane', 'White Katana']

tools = ['Bone Lockpick', 'Classic Lockpick', 'Disposable Scrambler', 'Electronic Key Hacker', 'Electronic Key Hacker MK III',
         'Emetic Gas Grenade', 'Emetic Grenade', "Guru's Emetic Grenade", 'Handyman Wrench', 'ICA Flash Phone',
         'ICA Proximity Taser', 'ICA Remote Micro Taser', 'ICA Remote Taser', 'ICA Titanium Crowbar', 'Lockpick',
         'Lockpick MK II', 'Lockpick MK III', 'Professional Screwdriver', 'Remote EMP Charge', 'Remote Emetic Gas Device']

distractions = ['"Mixtape 47"', 'Classic Coin', 'Coin', 'Gold Coin', 'Greedy Little Coin',
                'ICA Remote Audio Distraction', 'ICA Remote Audio Distraction MK II', 'ICA Remote Audio Distraction MK III', 'ICA Remote Micro Audio Distraction', 'Red-Tie Kiwi',
                'The Big One']

poisons = ['"Bubble Queen" Gum Pack', 'Antique Emetic Syringe', 'Antique Lethal Syringe', 'Emetic Pills', 'Emetic Poison Vial',
           'Emetic Poison Vial MK II', 'Emetic Syringe MK II', "Guru's Pen Syringe Emetic", 'ICA Pen Syringe Emetic', 'Lethal Pills',
           'Lethal Pills MK II', 'Lethal Poison Vial', 'Lethal Poison Vial MK II', 'Lethal Syringe MK II', 'Lethal Syringe MK III',
           'Modern Emetic Syringe', 'Modern Lethal Syringe', 'Modern Sedative Syringe', 'Sedative Pills', 'Sedative Poison Vial',
           'Sedative Poison Vial MK II']

explosives = ['Breaching Charge MK III', 'Concussion Grenade', 'Explosive Baseball', 'Explosive Compound', 'Explosive Golf Ball', 'Explosive XMas Gift'
              'Flash Grenade', 'Flash Grenade MK III', 'Fragmentation Grenade', 'Goldbrick Proximity Mine', 'ICA Explosive Phone',
              'ICA Micro Remote Explosive', 'ICA Proximity Concussion Device', 'ICA Proximity Concussion Device MK III', 'ICA Proximity Explosive', 'ICA Proximity Explosive MK II',
              'ICA Proximity Explosive MK III', 'ICA Proximity Micro Explosive', 'ICA Remote Concussion Devivce', 'ICA Remote Explosive', 'ICA Remote Explosive MK II',
              'ICA Remote Explosive MK III', 'ICA Remote Flash Device', 'ICA Tripwire Mine', "Lil' Flashy", 'Magnesium Pouch', 'Molotov Cocktail',
              'Napoleon Blownaparte', 'Nitroglycerin', 'Proximity CX Demo Block', 'Proximity CX Demo Block MK II', 'Proximity Explosive Duck MK III', 'Proximity Explosive Duck',
              'Proximity Explosive Rubber Duck MK II', 'Proximity Semtex Demo Block MK III', 'RFID Triggered Explosive', 'Remote Breaching Charge', 'Remote CX Demo Block',
              'Remote CX Demo Block MK II', 'Remote Concussion Collectors Duck', 'Remote Concussion Rubber Duck', 'Remote Explosive Classic Rubber Duck', 'Remote Explosive Devil Rubber Duck',
              'Remote Explosive Duck', 'Remote Explosive Rubber Duck MK II', 'Remote Semtex Demo Block MK III', 'Shaman Powder', 'The Ancestral Fountain Pen', 
              'The Iconator', 'The Pale Duck', 'The Roar Flash Grenade', "The Serpent's Bite"]

suits = ['Default Suit', "47's Signature Suit", "47's Signature Suit with Gloves", 'Absolution Suit', 'Blood Money Suit',
         'Phantom Suit', 'Ashen Suit with Gloves', 'The Undying Look', 'Suburban Suit with Driving Gloves', 'Requiem Suit',
         "Agent 17's Signature Suit", 'Platform Specific Suit', 'Terminus', 'Black & White Tuxedo Set with Gloves', 'Tuxedo with Gloves',
         'Classic All-Black Suit', 'Tuxedo, Mask and Gloves', 'The Cashmerian', 'Imperial Classic with Gloves', 'Classic Cut Long Coat Suit with Gloves',
         'Number Six with Gloves', 'Neon City Suit with Gloves', 'The New Yorker with Gloves', 'Winter Suit', 'Snow Festival Suit',
         'Casual Suit with Gloves', 'Italian Suit with Gloves', 'Florida Fit with Gloves', 'Casual Tourist with Gloves', 'Summer Suave Suit', 'Summer Sightseeing Suit with Gloves',
         'Casual Undercover', 'Midnight Black Suit', 'Summer Suit with Gloves', 'The Tropical Suit', 'Smart Casual Suit',
         'The Raver', 'The Lucky Ducky Suit', 'Tactical Wetsuit', 'Guerilla Wetsuit', 'Tactical Turtleneck',
         'Raven Suit', "Tactical Gear with Hunter's Hat", 'Freedom Phantom Suit', 'Polar Survival Suit', 'White Yukata',
         'Winter Sports Suit', 'Cowboy Suit', 'Lynch Suit', 'Futo Suit', 'The Neon Ninja Suit',
         'Rave On Suit', 'The Yellow Rabbit Suit', 'The Ruby Rude Track Suit', 'The Big, Bad Wolf Suit', 'The Arkian Tuxedo', 'Blue Flamingo Suit',
         'Clown Suit', 'The Buccaneer', 'The Sandman Suit', 'Santa 47', "The Devil's Own", 'Formal Hunting Attire',
         'The Black Dragon', 'Guru Suit', 'The White Shadow', 'The Straitjacket', 'The Rapacious Suit',
         'The Narcissus Suit', 'The Lotophage Suit', 'The Scarlet Suit', 'The Profligacy Suit', 'The Odium Suit',
         'The Temper Suit']

print("Welcome to the Hitman Randomizer. Before we start, here's some options to customize your experience.")
answer = str(input("Include items from the Trinity Pack? Y/N: "))
if answer == 'Y' or answer == 'y':
    concealed_weapons += ['ICA19 Whtie Trinity', 'ICA19 Red Trinity', 'ICA19 Black Trinity']
    pistols += ['ICA19 Whtie Trinity', 'ICA19 Red Trinity', 'ICA19 Black Trinity']
    containers += ['Premier White Briefcase', 'Crimson Red Briefcase', 'Ultimate Black Briefcase']
    suits += ['Premier White Suit', 'Crimson Red Suit', 'Ultimate Black Suit']

answer = str(input("Include items only available from Progress Transfer (ICA Performance Coins, Explosive Pen, etc.)? Y/N: "))
if answer == 'Y' or answer == 'y':
    distractions += ['ICA Performance Coin']
    containers += ['Aluminum Travel Briefcase']
    explosives += ['Explosive Pen', 'Lil Flashy']
    suits += ['Black Winter Suit']
def random_loadout():
    level = random.choices(maps)

    suit = random.choices(suits)

    weapon = random.choices(concealed_weapons)

    smuggled_item_cat = random.choices(cat_minus_containers)

    if smuggled_item_cat == ['Pistols']:
        smuggled_item = random.choices(pistols)

    elif smuggled_item_cat == ['SMGs']:
        smuggled_item = random.choices(smgs)

    elif smuggled_item_cat == ['Shotguns']:
        smuggled_item = random.choices(shotguns)

    elif smuggled_item_cat == ['Assault Rifles']:
        smuggled_item = random.choices(assault_rifles)

    elif smuggled_item_cat == ['Sniper Rifles']:
        smuggled_item = random.choices(sniper_rifles)

    elif smuggled_item_cat == ['Melee']:
        smuggled_item = random.choices(melees)

    elif smuggled_item_cat == ['Tools']:
        smuggled_item = random.choices(tools)

    elif smuggled_item_cat == ['Distractions']:
        smuggled_item = random.choices(distractions)

    elif smuggled_item_cat == ['Poisons']:
        smuggled_item = random.choices(poisons)

    elif smuggled_item_cat == ['Explosives']:
        smuggled_item = random.choices(explosives)
    else:
        print("How did you manage this")
        smuggled_item = "Null"

    item_one_cat = random.choices(cat_minus_guns)

    if item_one_cat == ['Containers']:
        item_one = random.choices(containers)
        briefcase_item_cat = random.choices(cat_minus_containers)
        if briefcase_item_cat == ['Pistols']:
            briefcase_item = random.choices(pistols)
        elif briefcase_item_cat == ['SMGs']:
            briefcase_item = random.choices(smgs)
        elif briefcase_item_cat == ['Shotguns']:
            briefcase_item = random.choices(shotguns)
        elif briefcase_item_cat == ['Assault Rifles']:
            briefcase_item = random.choices(assault_rifles)
        elif briefcase_item_cat == ['Sniper Rifles']:
            briefcase_item = random.choices(sniper_rifles)
        elif briefcase_item_cat == ['Melee']:
            briefcase_item = random.choices(melees)
        elif briefcase_item_cat == ['Tools']:
            briefcase_item = random.choices(tools)
        elif briefcase_item_cat == ['Distractions']:
            briefcase_item = random.choices(distractions)
        elif briefcase_item_cat == ['Poisons']:
            briefcase_item = random.choices(poisons)
        elif briefcase_item_cat == ['Explosives']:
            briefcase_item = random.choices(explosives)
        else:
            print("How did you manage this?")
            briefcase_item = "Null"

        item_one = item_one[0] + ", smuggling in " + briefcase_item[0]
        item_one = [item_one]

    elif item_one_cat == ['Melee']:
        item_one = random.choices(non_briefcase_melees)

    elif item_one_cat == ['Tools']:
        item_one = random.choices(tools)

    elif item_one_cat == ['Distractions']:
        item_one = random.choices(distractions)

    elif item_one_cat == ['Poisons']:
        item_one = random.choices(poisons)

    elif item_one_cat == ['Explosives']:
        item_one = random.choices(explosives)

    else:
        print("How did you manage this")
        item_one = "Null"

    if item_one_cat == ['Containers']:
        item_two_cat = random.choices(cat_minus_containers_and_guns)
    else:
        item_two_cat = random.choices(cat_minus_guns)

    if item_two_cat == ['Containers']:
        item_two = random.choices(containers)
        briefcase_item_cat = random.choices(cat_minus_containers)
        if briefcase_item_cat == ['Pistols']:
            briefcase_item = random.choices(pistols)
        elif briefcase_item_cat == ['SMGs']:
            briefcase_item = random.choices(smgs)
        elif briefcase_item_cat == ['Shotguns']:
            briefcase_item = random.choices(shotguns)
        elif briefcase_item_cat == ['Assault Rifles']:
            briefcase_item = random.choices(assault_rifles)
        elif briefcase_item_cat == ['Sniper Rifles']:
            briefcase_item = random.choices(sniper_rifles)
        elif briefcase_item_cat == ['Melee']:
            briefcase_item = random.choices(melees)
        elif briefcase_item_cat == ['Tools']:
            briefcase_item = random.choices(tools)
        elif briefcase_item_cat == ['Distractions']:
            briefcase_item = random.choices(distractions)
        elif briefcase_item_cat == ['Poisons']:
            briefcase_item = random.choices(poisons)
        elif briefcase_item_cat == ['Explosives']:
            briefcase_item = random.choices(explosives)
        else:
            print("How did you manage this?")
            briefcase_item = "Null"

        item_two = item_two[0] + ", smuggling in " + briefcase_item[0]
        item_two = [item_two]

    elif item_two_cat == ['Melee']:
        item_two = random.choices(non_briefcase_melees)

    elif item_two_cat == ['Tools']:
        item_two = random.choices(tools)

    elif item_two_cat == ['Distractions']:
        item_two = random.choices(distractions)

    elif item_two_cat == ['Poisons']:
        item_two = random.choices(poisons)

    elif item_two_cat == ['Explosives']:
        item_two = random.choices(explosives)

    print('----------------------------------------------------------------------')
    print("Map:", level[0])
    print("Suit:", suit[0])
    print("Weapon:", weapon[0])
    print("Smuggled Item:", smuggled_item[0])
    print("Item One:", item_one[0])
    print("Item Two:", item_two[0])
    print('----------------------------------------------------------------------')

answer = str(input("Would you like to generate a loadout? Y/N: "))

while answer == 'Y' or answer == 'y':
    random_loadout()
    answer = str(input("Would you like to generate another loadout? Y/N: "))

print("Thanks for randomizing!")
print("ASCII Source: https://www.asciiart.eu/video-games/hitman")

terminate = input("Press enter to quit")