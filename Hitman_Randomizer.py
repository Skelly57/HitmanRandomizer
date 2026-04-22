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
        "Hawke's Bay", 'Miami', 'Santa Fortuna', 'Mumbai', 'Whittleton Creek', 'Ambrose Island', 'Isle of Sgail', 
        'New York', 'Haven Island', 'Dubai', 'Dartmoor', 'Berlin', 'Chongqing', 'Mendoza']

concealed_weapons = ['"El Matador"', '"Rude Ruby"', 'Concept 5', 'Custom 5MM', 'Custom 5MM DTI',
                     'HWK21', 'HWK21 Covert', 'HWK21 MK II', 'HWK21 Pale Homemade Silencer', 'ICA DTI Stealth',
                     'ICA19', 'ICA19 Black Lily', 'ICA19 Chrome', 'ICA19 Classicballer', 'ICA19 F/A',
                     'ICA19 F/A Stealth', 'ICA19 F/A Stealth "Ducky" Edition', 'ICA19 Goldballer', 'ICA19 Iceballer', 'ICA19 Shortballer', 'ICA19 Silverballer',
                     'ICA19 Silverballer MK II', 'Kalmer 1 - Tranquilizer', 'Kalmer 2 - Tranquilizer', 'Krugermeier 2-2', 'Krugermeier 2-2 Dark',
                     'Krugermeier 2-2 Silver', 'Sieker 1', 'Striker', 'Striker V3', 'The Cherry Blossom Baller', 'The Ducky Gun',
                     'The Floral Baller', "The Serpent's Tongue", 'The Taunton Dart Gun', 'DAX X2 Covert', 'Brine-Damaged SMG', 'Slapdash SMG', 'ICA Combat Axe', 'Ice Axe']

containers = ['Arctic Toolbox', 'Black Leather Briefcase', 'Chinese Briefcase', 'Golden Briefcase', "Hunter's Briefcase",
              'ICA Briefcase', 'ICA Briefcase MK III', 'ICA Executive Briefcase', 'ICA Executive Briefcase Mk II', 'Orange Pinstripe Briefcase', 'Sieger 300 Sniper Case',
              'Toolbox']

gear =        ['Antique Curved Knife', 'Banana', 'Bat Shuriken', 'Blueberry Muffin', 'Burial Dagger',
               'Burj Al-Ghazali Snowglobe', 'Claw Hammer', 'Cocktail Shaker', 'Combat Knife', 'Concealable Baton',
               'Concealable Knife', 'Crystal Ball', 'Durian', 'Earphones', 'Feather Duster', 'Fiber Wire',
               'Fiber Wire Classic', 'Fiber Wire Red Tie', 'Fish', 'Fishing Line', 'Hobby Knife',
               'Hook', 'IO Elite S2VP Earphones', 'Ice Pick',
               'Janbiya', 'Kukri Knife', 'Measuring Tape', 'Meaty Bone', 'Okinawan Tonfa', 'Pinot Noir',
               'Piton', 'Pretzel', 'Quickdraw', 'Sacrificial Knife', 'Shuriken',
               'Small Goldbar', 'Snowball', 'Tanto', "The Black Almond's Dagger", "The Cat's Claw", 'The Sapienza FC-Sanguine Boot',
               'The Straitjacket Belt', 'Unicorn Horn', 'Violin', 'Bone Lockpick', 'Classic Lockpick', 'Disposable Scrambler', 'Electronic Key Hacker', 'Electronic Key Hacker MK III',
               'Emetic Gas Grenade', 'Emetic Grenade', "Guru's Emetic Grenade", 'Handyman Wrench', 'ICA Flash Phone', 'ICA Proximity Micro Taser',
               'ICA Proximity Taser', 'ICA Remote Micro Taser', 'ICA Remote Taser', 'ICA Titanium Crowbar', 'Lockpick',
               'Lockpick MK II', 'Lockpick MK III', 'Professional Screwdriver', 'RFID Triggered Taser', 'Remote EMP Charge', 'Remote Emetic Gas Device',
               'Breaching Charge MK III', 'Concussion Grenade', 'Explosive Baseball', 'Explosive Compound', 'Explosive Golf Ball', 'Explosive Pen', 'Explosive Xmas Gift'
               'Flash Grenade', 'Flash Grenade MK III', 'Fragmentation Grenade', 'Goldbrick Proximity Mine', 'ICA Explosive Phone', 'ICA Impat Explosive',
               'ICA Micro Remote Explosive', 'ICA Proximity Concussion Device', 'ICA Proximity Concussion Device MK III', 'ICA Proximity Explosive', 'ICA Proximity Explosive MK II',
               'ICA Proximity Explosive MK III', 'ICA Proximity Micro Explosive', 'ICA Remote Concussion Devivce', 'ICA Remote Explosive', 'ICA Remote Explosive MK II',
               'ICA Remote Explosive MK III', 'ICA Remote Flash Device', 'ICA Tripwire Mine', "Lil' Flashy", 'Magnesium Pouch', 'Molotov Cocktail',
               'Napoleon Blownaparte', 'Nitroglycerin', 'Proximity CX Demo Block', 'Proximity CX Demo Block MK II', 'Proximity Explosive Duck MK III', 'Proximity Explosive Duck',
               'Proximity Explosive Rubber Duck MK II', 'Proximity Lucky Cat Figurine', 'Proximity Semtex Demo Block MK III', 'RFID Triggered Explosive', 'Remote Breaching Charge', 'Remote CX Demo Block',
               'Remote CX Demo Block MK II', 'Remote Concussion Collectors Duck', 'Remote Concussion Rubber Duck', 'Remote Explosive Classic Rubber Duck', 'Remote Explosive Devil Rubber Duck',
               'Remote Explosive Duck', 'Remote Explosive Rubber Duck MK II', 'Remote Semtex Demo Block MK III', 'Shaman Powder', 'Sunset Rubber Duck', 'The Ancestral Fountain Pen', 
               'The Iconator', 'The Pale Duck', 'The Party Cracker', 'The Roar Flash Grenade', "The Serpent's Bite"]

nongear = ['"El Matador"', '"Rude Ruby"', 'Concept 5', 'Custom 5MM', 'Custom 5MM DTI',
            'HWK21', 'HWK21 Covert', 'HWK21 MK II', 'HWK21 Pale Homemade Silencer', 'ICA DTI Stealth',
            'ICA19', 'ICA19 Black Lily', 'ICA19 Chrome', 'ICA19 Classicballer', 'ICA19 F/A',
            'ICA19 F/A Stealth', 'ICA19 F/A Stealth "Ducky" Edition', 'ICA19 Iceballer', 'ICA19 Goldballer', 'ICA19 Shortballer', 'ICA19 Silverballer',
            'ICA19 Silverballer MK II', 'Kalmer 1 - Tranquilizer', 'Kalmer 2 - Tranquilizer', 'Krugermeier 2-2', 'Krugermeier 2-2 Dark',
            'Krugermeier 2-2 Silver', 'Sieker 1', 'Striker', 'Striker V3', 'The Cherry Blossom Baller', 'The Ducky Gun',
            'The Floral Baller', "The Serpent's Tongue", 'The Taunton Dart Gun',
            'Brine-Damaged SMG', 'DAK Black Covert', 'DAK Gold Covert', 'DAK X2 Covert', 'ICA SMG Raptor Covert',
            'Militia-Issued HX-10 SMG', 'SMG Raptor Rude Ruby Covert', 'Slapdash SMG', 'TAC-SMG', 'TAC-SMG Covert',
            'TAC-SMG MK II', 'TAC-SMG S',
            'Bartoli 12G Short H', 'Bartoli Hunting Shotgun Deluxe', 'Enram HV', 'Enram HV CM', 'Enram HV Covert', 'Enram HV Covert MK II', 'Golden Sawed-Off Bartoli 12G',
            'ICA Tactical Shotgun', 'ICA Tactical Shotgun Covert (Black)', 'ICA Tactical Shotgun Covert (White)', 'Sawed-Off Bartoli 12G', 'The Maximalist Shotgun'
            'RS-15', 'Shashka A33 Gold', 'Shashka A33 H', 'Sieger AR552 Tactical', 'TAC-4 AR Auto', 'TAC-4 AR Desert',
            'TAC-4 AR MK II', 'TAC-4 AR Stealth', 'TAC-4 S/A', 'TAC-4 S/A Jungle', 'The Shashka Beast',
            'A New Bat', 'Broadsword', 'HF Championship Bat', "Jarl's Pirate Saber", 'Kukri Machete', 'Mace',
            'Masamune', "Nne Obara's Machete", 'Ornate Scimitar', "The Devil's Cane", 'The Iridescent Katana', 'The Proud Swashbuckler', 'Walking Cane', 'White Katana', 'Oil Canister']

suits = ['Default Suit', "47's Signature Suit", "47's Signature Suit with Gloves", 'Absolution Suit', 'Blood Money Suit',
         'Phantom Suit', 'Ashen Suit with Gloves', 'The Undying Look', 'Suburban Suit with Driving Gloves', 'The Public Enemy Suit', 'Requiem Suit',
         "Agent 17's Signature Suit", 'White Sunset Suit', 'Platform Specific Suit', 'Terminus', 'The Sangfroid Suit', 'The Sniper Challenge Suit', 'Black & White Tuxedo Set with Gloves', 'Tuxedo with Gloves',
         'Classic All-Black Suit', 'Tuxedo, Mask and Gloves', 'The Cashmerian', 'Imperial Classic with Gloves', 'Classic Cut Long Coat Suit with Gloves',
         'Number Six with Gloves', 'Neon City Suit with Gloves', 'The New Yorker with Gloves', 'Winter Suit', 'Snow Festival Suit', 'The Tropical Islander',
         'Casual Suit with Gloves', 'Italian Suit with Gloves', 'Florida Fit with Gloves', 'Casual Tourist with Gloves', 'Summer Suave Suit', 'Summer Sightseeing Suit with Gloves',
         'Casual Undercover', 'Midnight Black Suit', 'Summer Suit with Gloves', 'The Tropical Suit', 'Smart Casual Suit',
         'The Raver', 'The Lucky Ducky Suit', 'Tactical Wetsuit', 'Guerilla Wetsuit', 'Tactical Turtleneck', 'Tactical Turtleneck with Gloves',
         'Raven Suit', "Tactical Gear with Hunter's Hat", 'Freedom Phantom Suit', 'Polar Survival Suit', 'The Egg Hunt Suit', 'White Yukata', 'VIP Patient',
         'Winter Sports Suit', 'Cowboy Suit', 'Lynch Suit', 'Futo Suit', 'The Neon Ninja Suit', 'The Pastel Suit', 'Subjet 47',
         'Rave On Suit', 'The Yellow Rabbit Suit', 'The Ruby Rude Track Suit', 'The Big, Bad Wolf Suit', 'The Arkian Tuxedo', 'Blue Flamingo Suit',
         'Clown Suit', 'The Buccaneer', 'The Sandman Suit', "The Jack-O'-Lantern Suit", 'Plague Doctor', 'Super Fan', 'THe Krampus Little Helper Suit', 'The Cozy Christmas Suit', 'Little Helper 47', 'Santa 47', 
         'The Codename 47 Suit', 'Trendy Tourist Suit', 'The Black Bruiser Suit', 'The Gauze Suit', "The Devil's Own", 'Formal Hunting Attire',
         'The Black Dragon', 'Guru Suit', 'The White Shadow', 'The Straitjacket', 'The Rapacious Suit',
         'The Narcissus Suit', 'The Lotophage Suit', 'The Scarlet Suit', 'The Profligacy Suit', 'The Odium Suit', 'The Temper Suit']

print("Welcome to the Hitman Randomizer. Before we start, here's some options to customize your experience.")
answer = str(input("Include items from the Trinity Pack? Y/N: "))
if answer == 'Y' or answer == 'y':
    concealed_weapons += ['ICA19 Whtie Trinity', 'ICA19 Red Trinity', 'ICA19 Black Trinity']
    nongear += ['ICA19 Whtie Trinity', 'ICA19 Red Trinity', 'ICA19 Black Trinity']
    containers += ['Premier White Briefcase', 'Crimson Red Briefcase', 'Ultimate Black Briefcase']
    suits += ['Premier White Suit', 'Crimson Red Suit', 'Ultimate Black Suit']

answer = str(input("Include items only available from Progress Transfer (ICA Performance Coins, Explosive Pen, etc.)? Y/N: "))
if answer == 'Y' or answer == 'y':
    gear += ['ICA Performance Coin']
    containers += ['Aluminum Travel Briefcase']
    suits += ['Black Winter Suit']

answer = str(input("Include items from the Street Art Pack? Y/N: "))
if answer == 'Y' or answer == 'y':
    concealed_weapons += ['The Concrete Bunny Pistol']
    nongear += ['The Concrete Bunny Pistol', 'The Shark SMG', 'The Concrete Shotgun', 'The Concrete Assault Rifle', 'The Concrete Sniper Rifle', 'The Concrete Bat']
    suits += ['The Graffiti Hoody Suit']

answer = str(input("Include items from the Makeshift Pack? Y/N: "))
if answer == 'Y' or answer == 'y':
    concealed_weapons += ['The Scrap Gun', 'The Scrap SMG']
    nongear += ['The Scrap Gun', 'The Scrap SMG', 'The Makeshift Scrap Shotgun', 'The Makeshift Scrap Assault Rifle', 'The Scrappy Sniper Rifle', 'The Makeshift Katana']
    suits += ['The Scrap Poncho Suit']

freelancer_level = int(input("What is your Freelancer Mastery Level?: "))
if freelancer_level >= 5:
    nongear += ['The Ornamental Pistol']
    concealed_weapons += ['The Ornamental Pistol']
if freelancer_level >= 10:
    nongear += ['The Ornamental Assault Rifle']
if freelancer_level >= 15:
    nongear += ['The Ornamental Katanas']
if freelancer_level >= 20:
    nongear += ['The Ornamental Shotgun']
if freelancer_level >= 25:
    nongear += ['The Ornamental SMG']
if freelancer_level >= 30:
    nongear += ['The Ornamental Sniper Rifle']
if freelancer_level >= 35:
    suits += ['The Golden Contender Suit']
if freelancer_level >= 40:
    nongear += ['The Ancestral Pistol']
    concealed_weapons += ['The Ancestral Pistol']
if freelancer_level >= 45:
    nongear += ['The Ancestral Shotgun']
if freelancer_level >= 50:
    nongear += ['The Ancestral Assault Rifle']
if freelancer_level >= 55:
    nongear += ['The Ancestral Sniper Rifle']
if freelancer_level >= 60:
    gear += ['The Ancestral Knife']
if freelancer_level >= 65:
    suits += ['The Ancestral Hunter Suit']
if freelancer_level == 100:
    suits += ['The Master Freelancer Suit']

answer = str(input("Include items from Celebrity DLC Packs? Y/N: "))
if answer == 'Y' or answer == 'y':
    concealed_weapons += ['Bartoli 75S "Lucky Knight"', 'The Banker Silenced Pistol', 'The Prank Pistol', 'Kali Sticks']
    containers += ['The Club Boom 12" Flightcase']
    gear += ['"Good Quark Vol. 3" VHS Tape', 'Golden Dragon Scissors', 'Jade Dagger', "Jar of Mom's Spaghetti Sauce", 'Kronstadt IOI-1998X Surround Earphones', 'Sickle Sacrificus', 'The Banker Rope', 'The Club Boom 12" Vinyl Sampler', 'The Disruptor Kettlebell',
             'The Disruptor Resistance Band', 'The Splitter Kukri Knife', 'Manypass', 'The In-flu-ential Duck', 'The "Casino Monarchique" Chip (1.000.000)',
             'Kronstadt Explosive Pen (Gen 2)', 'Kronstadt Mini Flash Robo XOI-2900', 'Mr. Chainsaw Jr.', 'The Chainsaw Duck', 'The Red Light Flash Grenade']
    suits += ['Breach Response Gear', 'The Urban Maverick with Gloves', 'The MC Fit', 'Only Overalls', 'The Yellow Tracksuit', 'The Master Martial Artist Suit', 'The Banker King of Cards Suit', 'The Banker Suit', 'The Splitter Boxer Suit',
              'The Splitter Suit', 'The Disruptor Fur Coat', 'The Disruptor MMA Suit', 'The Club Boom DJ Suit', 'The Greek Fire Suit', 'The Ephemeral Suit with Eye Patch', 'The Ephemeral Suit']
    
answer = str(input("Include items from Twitch drops? Y/N: "))
if answer == 'Y' or answer == 'y':
    concealed_weapons += ['The Purple Streak ICA19 Classic Baller']
    containers += ['The Purple Streak ICA Briefcase']
    gear += ['The Purple Streak Fiber Wire', 'The Purple Streak Crowbar', 'The Purple Streak Screwdriver', 'Purple Easter Egg', 'Star Apple', 'The "Casino Monarchique" Chip (100.000)', 'The Purple Streak Coin', 'Bomb-Ass Dynamite', 'The Dragon Duck',
             'The IOI Showcase Duck', 'The Neon Duck', 'The Purple Streak Explosive Duck']
    nongear += ['The Purple Streak ICA19 Classic Baller', 'The Purple Streak Baseball Bat']
    suits += ['The Purple Streak Suit', 'The Purple Streak Swimwear Suit', 'The Purple Streak Boxer Suit']

all_gear = gear + nongear

def random_loadout(campaign, map):
    if (campaign == 1):
        level = maps[map]
    else:
        level = random.choices(maps)
    suit = random.choices(suits)
    weapon = random.choices(concealed_weapons)
    smuggled_item = random.choices(all_gear)
    item_one = random.choices(gear)
    briefcase = random.choices(containers)
    item_two = random.choices(nongear)
    print('----------------------------------------------------------------------')
    print("Map:", level)
    print("Suit:", suit[0])
    print("Weapon:", weapon[0])
    print("Smuggled Item:", smuggled_item[0])
    print("Item One:", item_one[0])
    print("Item Two:", item_two[0], "in", briefcase[0])
    print('----------------------------------------------------------------------')

answer = str(input("Would you like to generate a full randomized campaign? Y/N: "))
if answer == 'Y' or answer == 'y':
    while answer == 'Y' or answer == 'y':
        for x in range(0, 20):
            random_loadout(campaign = 1, map = x)
        answer = str(input("Would you like to generate another campaign? Y/N: "))
else:
    random_loadout()
    answer = str(input("Would you like to generate another loadout? Y/N: "))
    while answer == 'Y' or answer == 'y':
        random_loadout()
        answer = str(input("Would you like to generate another loadout? Y/N: "))

print("Thanks for randomizing!")
print("ASCII Source: https://www.asciiart.eu/video-games/hitman")

terminate = input("Press enter to quit")