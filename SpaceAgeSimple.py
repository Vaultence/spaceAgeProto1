import time, random, os
gamebeaten = False
def chance():
    return random.randint(1,10)
saveScumCounter = 0
playername = ""
autoShipyard = False
planetShipyard = False
asteroidStore = False
prestige = 0
eventDifficulty = 0

def callSave(string):
    if string.lower()[0:4] == "save":
        print("\n\n/////////////////////////////////////////////////////////\n\n")
        getSaveFile(playername, hull, maxhull, shield, engines, weapon, scrap, living, difficulty, zoneSafety, prestige, eventDifficulty)
        print("\n\n/////////////////////////////////////////////////////////\n\n")
        input("Hit 'Enter' when you have put your save code in a safe place.")
        return 1
    return -2
def getSaveFile(playername, hull, maxhull, shield, engines, weapon, scrap, living, difficulty, zoneSafety, prestige, eventDifficulty):
    print(str(playername)+":"+str(hull)+":"+str(maxhull)+":"+str(shield)+":"+str(engines)+":"+str(weapon)+":"+str(scrap)+":"+str(living)+":"+str(difficulty)+":"+str(zoneSafety)+":"+str(prestige)+":"+str(eventDifficulty))

def getDifficulty(x):
    difficulty = input('\n 1. Very Easy.'
                       '\n 2. Easy'
                       '\n 3. Normal'
                       '\n 4. Hard'
                       '\n 5. Expert'
                       '\n 6. True Masochist\n')

    print('\n' * 100)
    if difficulty == 'god':
        hull = 1000
        maxhull = 1000
        shield = 1000
        engines = 1000
        weapon = 1000
        scrap = 10000
        living = True
        difficulty = 'Godless'
        zoneSafety = 0

    elif difficulty == '1':
        hull = 90+x*5
        maxhull = 90+x*5
        shield = 4+x
        engines = 4+x
        weapon = 4+x
        scrap = 55+x*20
        living = True
        difficulty = 'Very Easy'
        zoneSafety = 0

    elif difficulty == '2':
        hull = 65+x*5
        maxhull = 65+x*5
        shield = 3+x
        engines = 3+x
        weapon = 3+x
        scrap = 45+x*20
        living = True
        difficulty = 'Easy'
        zoneSafety = 5
        
    elif difficulty == '3':
        hull = 40+x*5
        maxhull = 40+x*5
        shield = 2+x
        engines = 2+x
        weapon = 2+x
        scrap = 30+x*20
        living = True
        difficulty = 'Normal'
        zoneSafety = 15

    elif difficulty == '4':
        hull = 25+x*5
        maxhull = 25+x*5
        shield = 1+x
        engines = 1+x
        weapon = 1+x
        scrap = 20+x*20
        living = True
        difficulty = 'Hard'
        zoneSafety = 15

    elif difficulty == '5':
        hull = 10+x*5
        maxhull = 15+x*5
        shield = 0+x
        engines = 1+x
        weapon = 1+x
        scrap = 0+x*20
        living = True
        difficulty = 'Expert'
        zoneSafety = 15

    elif difficulty == '6':
        hull = 7+x*5
        maxhull = 10+x*5
        shield = 0+x
        engines = 0+x
        weapon = 0+x
        scrap = 0+x*20
        living = True
        difficulty = 'True Masochist'
        zoneSafety = 20

    else:
        hull = 40+x*5
        maxhull = 40+x*5
        shield = 2+x
        engines = 2+x
        weapon = 2+x
        scrap = 30+x*20
        living = True
        difficulty = 'Normal'
        zoneSafety = 15

    return str(hull)+":"+str(maxhull)+":"+str(shield)+":"+str(engines)+":"+str(weapon)+":"+str(scrap)+":"+str(living)+":"+str(difficulty)+":"+str(zoneSafety)
print("If you need to save, just type 'Save' when prompted to hit 'Enter' between events. \n"
      "You cannot save during boss fights. However, if you decide you want to savescum your way\n"
      "to an easy achievement screen I will find out magically and punish you. Ok? Great.")
save = input("If you have a save file, enter it here. Otherwise just press 'Enter'")

if save != "":
    save = save.split(":")
    playername = str(save[0])
    hull = int(save[1])
    maxhull = int(save[2])
    shield = int(save[3])
    engines = int(save[4])
    weapon = int(save[5])
    scrap = int(save[6])
    living = bool(save[7])
    difficulty = str(save[8])
    zoneSafety = int(save[9])
    prestige = int(save[10])
    eventDifficulty = int(save[11])
else:
    statArray = getDifficulty(prestige).split(":")
    hull = int(statArray[0])
    maxhull = int(statArray[1])
    shield = int(statArray[2])
    engines = int(statArray[3])
    weapon = int(statArray[4])
    scrap = int(statArray[5])
    living = bool(statArray[6])
    difficulty = str(statArray[7])
    zoneSafety = int(statArray[8])
    playername = input('Enter your name\n')

while living:
    if saveScumCounter >= 5:
        thisFile = os.path.abspath(__file__)
        os.remove(thisFile)
    eventDifficulty = min(prestige*5, eventDifficulty+0.05)
    if hull <= 0:
        living = False
    print('\nHull: ', hull, '/', maxhull,
          '\nScrap: ', scrap,
          '\nShield: ', shield,
          '\nEngines: ', engines,
          '\nWeapons: ', weapon)
    event = random.randint(1,9)
    if gamebeaten == False and maxhull >= 50+prestige*10 and shield >= 25+round(prestige*1.5) and engines >= 25+round(prestige*1.5) and weapon >= 25+round(prestige*1.5):
        print('A strange subspace signal is intercepted... It\'s getting stronger.')
        time.sleep(4)
        print('5')
        time.sleep(1)
        print('4')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        event = 10
    if living == False:
        event = 0
    # Death
    if event == 0:
        print('\n\n\n\n\n\nYour ship (remains) will forever drift in space, or until looters destroy it.')
        print('Your difficulty was: ' + difficulty)
        if prestige >= 1:
            print("Crystal Core level: " + str(prestige))
            print("Your crystal core glows... And you somehow find yourself back at the start! I'm so merciful.")
            input("Press \'Enter\' to continue")
            statArray = getDifficulty(prestige).split(":")
            hull = int(statArray[0])
            maxhull = int(statArray[1])
            shield = int(statArray[2])
            engines = int(statArray[3])
            weapon = int(statArray[4])
            scrap = int(statArray[5])
            living = bool(statArray[6])
            difficulty = str(statArray[7])
            zoneSafety = int(statArray[8])
            gamebeaten = False

    # Shipyardigans
    if event == 1 and autoShipyard == False:
        autoShipyard = True
        print('You arrive at an automated shipyard in the nebula.')
        eventinput = input('\n 1. You have no need of its services.'
                           '\n 2. Upgrade your shields. (' + str(20+round(eventDifficulty)) + ' scrap)'
                           '\n 3. Upgrade your engines. (' + str(20+round(eventDifficulty)) + ' scrap)'
                           '\n 4. Upgrade the hull. (' + str(18+round(eventDifficulty)) + ' scrap)'
                           '\n 5. Full hull repair. (2 scrap per hull point) \n')
        if eventinput == '2':
            if scrap < 20+round(eventDifficulty):
                print('You can\'t afford it.')
            else:
                print('You wait as they install it onto your ship')
                scrap -= 20+round(eventDifficulty)
                shield += 1
        elif eventinput == '3':
            if scrap < 20+round(eventDifficulty):
                print('You can\'t afford it.')
            else:
                print('You\'re a little anxious as the old engines are replaced and the system is upgraded.')
                scrap -= 20+round(eventDifficulty)
                engines += 1
        elif eventinput == '4':
            if scrap < 18+round(eventDifficulty):
                print('You can\'t afford it.')
            else:
                print('It takes several hours, but eventually it\'s done and, you got a nice little room on the outside.')
                maxhull += 5
                hull += 5
                scrap -= 18+round(eventDifficulty)
        elif eventinput == '5':
            if (maxhull - hull) * 2 > scrap:
                print('Unfortunately, hull repairs are quite expensive.')
            else:
                print('After a long time, your ship is basically good as new. Minus the grease in the engines.')
                scrap -= (maxhull - hull) * 2
                hull = maxhull
    elif event == 1 and autoShipyard == True:
        event = random.randint(2, 9)

    # Store
    if event == 2 and asteroidStore == False:
        asteroidStore = True
        print('There\'s a small store nested into an asteroid here.')
        eventinput = input('\n 1. You have no need for it.'
                           '\n 2. Look for the best bargain. (' + str(2+round(eventDifficulty)) + "-" + str(7+3*round(eventDifficulty)) + " scrap)"
                           '\n 3. Find the best weapon here. (' + str(12+2*round(eventDifficulty)) + "-" + str(30+6*round(eventDifficulty)) + " scrap)"
                           '\n 4. Repair the hull where you can. (4 scrap)\n')
        if eventinput == '2':
            print('You search and compare...')
            eventchance = chance()
            if eventchance >= 9:
                print('You find a Burst Laser Mk2 for a very cheap price.')
                if scrap < 7+3*round(eventDifficulty):
                    print('Somehow you can\'t even afford that.')
                else:
                    scrap -= 7+3*round(eventDifficulty)
                    weapon += 3
            elif eventchance >= 6:
                print('You find a discarded prototype of a Flak Cannon, variant A.')
                if scrap < 4+2*round(eventDifficulty):
                    print('How the heck can\'t you afford this???')
                else:
                    scrap -= 4+2*round(eventDifficulty)
                    weapon += 2
            elif eventchance >= 3:
                print('You find a barely functioning piece of actual garbage. Still a weapon.')
                if scrap < 2+round(eventDifficulty):
                    print('Excuse me but buy things when you have more than 2 scrap you moron.')
                else:
                    scrap -= 2+round(eventDifficulty)
                    weapon += 1
            else:
                print('You fail to find a good bargain.')
        elif eventinput == '3':
            print('You begin searching for the best weapon you can get here.')
            eventchance = chance()
            if eventchance >= 9:
                print('A Burst Laser, variant 9, awaits.')
                if scrap < 30+6*round(eventDifficulty):
                    print('Its frickin\' expensive though.')
                else:
                    scrap -= 30+6*round(eventDifficulty)
                    weapon += 9
            elif eventchance >= 6:
                print('A glaive beam, it reads "A staple of destructive power.')
                if scrap < 20+4*round(eventDifficulty):
                    print('Unfortunately, you can\'t afford the weapon of mass destruction.')
                else:
                    scrap -= 20+4*round(eventDifficulty)
                    weapon += 7
            elif eventchance >= 3:
                print('You find a fairly basic but none-the-less brutal Heavy Laser Mk2')
                if scrap < 12+2*round(eventDifficulty):
                    print('Can\'t afford it, however.')
                else:
                    scrap -= 12+2*round(eventDifficulty)
                    weapon += 4
            else:
                print('You run out of time being that you can\'t find anything outstanding.')
        elif eventinput == '4' and hull < maxhull:
            if scrap < 4:
                print('Not enough materials for the patch or payment.')
            else:
                print('You wait shortly as the major hull breaches are sealed and some minor fires are put out.')
                scrap -= 4
                hull += 4
                if hull > maxhull:
                    hull = maxhull
        elif eventinput == '4':
            print('Uh you have no damage to your hull lol')
    elif event == 2 and asteroidStore == True:
        event = random.randint(3, 9)

    # Get Better Ship
    if event == 3 and planetShipyard == False:
        planetShipyard = True
        print('You arrive at a planetary shipyard.')
        eventinput = input('\n 1. Buy a slightly better ship than your current. ('+str(68+4*round(eventDifficulty))+'+2 per hull scrap)'
                            '\n 2. Buy a much better ship than your current. ('+str(132+7*round(eventDifficulty))+'+2 per hull scrap)'
                            '\n 3. Buy a significantly better ship than your current. ('+str(200+10*round(eventDifficulty))+'+2 per hull scrap)'
                            '\n 4. Don\'t buy anything.\n')
        if eventinput == '1':
            if scrap < ((68+4*round(eventDifficulty)) + ((maxhull - hull) * 2)):
                print('You cannot afford this.')
            else:
                hull += 5
                maxhull += 5
                shield += 1
                engines += 1
                weapon += 1
                scrap -= (68+4*round(eventDifficulty)) + ((maxhull - hull) * 2)
                hull = maxhull

        elif eventinput == '2':
            if scrap < ((132+7*round(eventDifficulty)) + ((maxhull - hull) * 2)):
                print('You cannot afford this.')
            else:
                hull += 10
                maxhull += 10
                shield += 2
                engines += 2
                weapon += 2
                scrap -= (132+7*round(eventDifficulty)) + ((maxhull - hull) * 2)
                hull = maxhull

        elif eventinput == '3':
            if scrap < ((200+10*round(eventDifficulty)) + ((maxhull - hull) * 2)):
                print('You cannot afford this.')
            else:
                hull += 20
                maxhull += 20
                shield += 3
                engines += 3
                weapon += 3
                scrap -= (200+10*round(eventDifficulty)) + ((maxhull - hull) * 2)
                hull = maxhull
    elif event == 3 and planetShipyard == True:
        event = random.randint(4, 9)

    # Asteroid field
    if event == 4:
        planetShipyard = False
        asteroidStore = False
        autoShipyard = False
        eventchance = chance()
        print('You jump to an asteroid field.')
        eventinput = input('\n 1. Leave it alone'
                           '\n 2. Look for materials\n')
        if eventinput == '2':
            if shield >= 5+round(eventDifficulty)/5:
                print('You need not fear the asteroids with advanced shielding.')
                scrap += 4
            elif engines >= 6+round(eventDifficulty)/5:
                print('You avoid the asteroids, but it requires your concentration.')
                scrap += 2
            elif eventchance >= 4+round(eventDifficulty)/5:
                print('You mine the asteroids without interuption')
                scrap += 3
            else:
                print('A few of the asteroids hit your hull but you manage to mine a little bit.')
                scrap += 1
                hull -= (5+round(eventDifficulty)/5 - shield)

    # Debris field
    elif event == 5:
        planetShipyard = False
        asteroidStore = False
        autoShipyard = False
        print('You come to a debris field, or maybe a pirate arena. Prefferably the first.')
        eventinput = input('\n 1. Make a search in the debris field.'
                           '\n 2. Leave it.\n')
        eventchance = chance()
        if eventinput == '1':
            if eventchance >= 5+round(eventDifficulty)/20:
                print('You find a fairly sizable amount of scrap easily salvaged from the wreckage.')
                scrap += 5
            elif shield < 6+round(eventDifficulty)/4:
                print('Turns out it was booby trapped, you still manage to salvage a bit... of your own ship.')
                scrap += 1
                hull -= (6+round(eventDifficulty)/4 - shield)
            else:
                print('It was trapped, but your shields absorb all the possible damage.')
                scrap += 4

    # Signal A
    elif event == 6:
        planetShipyard = False
        asteroidStore = False
        autoShipyard = False
        print('A low wavelength signal is emmited from the nearby planet.')
        eventinput = input('\n 1. Investigate.'
                           '\n 2. Wait.'
                           '\n 3. Leave.\n')
        if eventinput == '1':
            print('You come closer to the beacon, but some planetary defense begins firing upon you. You have to retreat.')
            if shield < 7+round(eventDifficulty)*3:
                hull -= (7+round(eventDifficulty)*3 - shield)
        if eventinput == '2':
            print('You recieve a hail noting the coordinates of a nearby beacon.')
            eventinput = input('\n 1. This isn\'t your battle.'
                               '\n 2. Go to the indicated location.\n')
            if eventinput == '2':
                print('A massive ship is here, or what\'s left of it.')
                eventchance = chance()
                if eventchance >= 60:
                    scrap += 6
                elif shield < 3+round(eventDifficulty)/6:
                    print('Some debris hits your ship in attempting to salvage.')
                    scrap += 4
                    hull -= (3+round(eventDifficulty)/6 - shield)
                else:
                    scrap += 4

    # Fire
    elif event == 7:
        planetShipyard = False
        asteroidStore = False
        autoShipyard = False
        print('As soon as you jump to this beacon, a lone station immediately hails you, needing help for a fire broken out.')
        eventinput = input('\n 1. It\'s too dangerous.'
                           '\n 2. Board and try to help put it out.\n')
        eventchance = chance()
        if eventinput == '2':
            if eventchance >= 6:
                print('The station, once the fire is put out, rewards you with scrap.')
                scrap += 5
            elif engines >= 8+round(eventDifficulty)/3:
                print('You manage to escape from the station when it becomes clear that it was going to explode.')
                scrap += 1
            else:
                print('Despite your best efforts, one of the station\'s room explode, leading to a chain reaction'
                      '\nthat tears apart the rest of the station.')
                scrap += 1
                hull -= (8+round(eventDifficulty)/3 - engines)

    # Mining Operation    
    elif event == 8:
        planetShipyard = False
        asteroidStore = False
        autoShipyard = False
        print('You find a currently unworked mining field, you find an asteroid that appears to have a blast door sealed.')
        eventinput = input('\n 1. Attempt to blast it open'
                           '\n 2. Leave it.\n')
        if eventinput == '1':
            if random.randint(5+round(eventDifficulty)/5,8+round(eventDifficulty)/3) < weapon:
                print('You succeed in blasting open the door.')
                scrap += 3
            else:
                print('You do not succeed in getting the door open.')

    # Regular Pirate Encounter
    elif event == 9 and zoneSafety <= 0:
        planetShipyard = False
        asteroidStore = False
        autoShipyard = False
        ftl = 0
        paverage = round((shield + engines + weapon + maxhull/25)/4)
        pweapons = random.randint(round(paverage*0.6), round(paverage*1.4))
        pshields = random.randint(round(paverage*0.6), round(paverage*1.4))
        pengines = random.randint(round(paverage*0.6), round(paverage*1.4))
        phull = random.randint(round(paverage*4), round(paverage*10))
        salvage = round((pweapons+pshields+phull+pengines)/6)
        motive = True
        if engines == 0:
            ftlChargeTime = 100000
        else:
            ftlChargeTime = round(pengines*3/engines)
        turn = 0
        skip = False
        ftlJump = '2'
        print('A pirate is located at this beacon, it begins its advance.')
        print('\nPirate Stats:'
              '\nHull: ', phull,
              '\nShield: ', pshields,
              '\nEngines: ', pengines,
              '\nWeapons: ', pweapons)
        if weapon > pshields:
            if input('Skip all text and fight? (y/n)') == 'y':
                skip = True

        while living == True and phull > 0 and ftlJump == '2' and motive == True:
            if turn == 0:
                if skip == False:
                    print('\nHull: ', hull, '/', maxhull)
                turn = 1
                ftl += 1
                if skip == False:
                    if ftl >= ftlChargeTime:
                        ftlJump = input('\n 1. Jump away.'
                                        '\n 2. Stay and fight.')
                if skip == False:
                    print('You fire upon the pirate')
                if weapon <= pshields:
                    if skip == False:
                        print('You are unable to breach the pirate\'s defences.')
                else:
                    phull -= (weapon - pshields)
                    if skip == False:
                        print('The pirate has', phull, 'hull left.')
            elif turn == 1:
                turn = 0
                if skip == False:
                    print('The pirate fires upon you')
                if pweapons < shield:
                    if skip == False:
                        print('The pirate fails to breach your shields')
                else:
                    hull -= (pweapons - shield)
            if hull <= 0:
                living == False
            if pweapons <= shield and weapon <= pshields:
                print('You and the pirate both quickly realize that neither'
                      '\ncan end the fight, and the pirate jumps away.')
                motive = False
                
        if motive == True and ftlJump == '2':
            scrap += salvage
    elif event == 9 and zoneSafety > 0:
        print('You see a pirate stationed near this beacon, and you jump away before it sees you.')
        zoneSafety += 1
    # The Scourge
    if event == 10:
        print('The one true pirate lord, responsible for the destruction of entire systems,'
              '\nappears before you. Due to its ftl disabling field you are unable to'
              '\nescape this fight. In addition to that your sensors are being jammed'
              '\nand you cannot see how powerful they are. The Scourge opens fire!.')
        cshield = shield
        cengines = engines
        cweapon = weapon
        pweapons = random.randint(round(shield*0.6), round(shield*0.8))
        pcweapons = pweapons
        pshields = random.randint(round(weapon*1.2), round(weapon*1.6))
        pcshields = pshields
        pengines = random.randint(round(weapon*1.2), round(weapon*1.6))
        pcengines = pengines
        phull = random.randint(round(maxhull*20), round(maxhull*30))
        salvage = (round(maxhull*0.1) + round(shield*0.1) + round(engines*0.1) + round(weapon*0.1))
        turn = 0
        railgunCharged = False
        weaponrow = 0.1
        shieldrow = 0.1
        enginesrow = 0.1
        while living == True and phull > 0:
            if turn == 0:
                scourgeRepair = False
                scourgeAttack = random.randint(0, 3)
                if railgunCharged == True:
                    if railgunShieldBuffer == 0:
                        pcshields += pshields * 0.6
                    else:
                        pcshields = railgunShieldBuffer
                    if railgunEnginesBuffer == 0:
                        pcengines += pengines * 0.6
                    else:
                        pcengines = railgunEnginesBuffer
                    print('The Scourge fires it\'s main weapon, a railgun that appears to run through the'
                          '\nrest of the ship and you clearly see the projectile pierce your shields and'
                          '\ngo out through the opposite side relative to where it entered')
                    systemDamage = random.randint(1, 3)
                    if systemDamage == 1:
                        print('Your shields are critically damaged by the attack!')
                        cshield -= round(0.4 * shield)
                        if cshield < 0:
                            cshield = 0
                    if systemDamage == 2:
                        print('Your engines are critically damaged by the attack!')
                        cengines -= round(0.4 * engines)    
                        if cengines < 0:
                            cengines = 0
                    if systemDamage == 3:
                        print('Your weapons are critically damaged by the attack!')
                        cweapon -= round(0.4 * weapon)
                        if cweapon < 0:
                            cweapon = 0
                    railgunCharged = False
                else:
                    # Repair Damaged System
                    if scourgeAttack <= 0:
                        if pcshields < pshields or pcweapons < pweapons or pcengines < pengines:
                            print('The Scourge doesn\'t appear to do anything')
                            repairSystem = random.randint(1, 3)
                            if repairSystem == 1 and pcshields <pshields:
                                pcshields += round(pshields * 0.2)
                                if pcshields > pshields:
                                    pcshields = pshields
                            elif repairSystem == 1:
                                repairSystem = random.randint(2, 3)
                            if repairSystem == 2 and pcengines < pengines:
                                pcengines += round(pengines * 0.2)
                                if pcengines > pengines:
                                    pcengines = pengines
                            elif repairSystem == 2:
                                repairSystem = 3
                            if repairSystem == 3:
                                pcweapons += round(pweapons * 0.2)
                                if pcweapons > pweapons:
                                    pcweapons = pweapons
                            scourgeRepair = True

                    if scourgeAttack <= 0 and scourgeRepair == False:
                        scourgeAttack = random.randint(1, 3)
                    
                    # Regular Laser Attack
                    if scourgeAttack == 1:
                        print('The Scourge prepares it\'s hail of laserfire!')
                        if pcweapons <= cshield:
                            print('The barrage is deflected harmlessly off of your shields.')
                        else:
                            print('Your shields fail to repel the attack and are forced to endure the attack.')
                            systemDamage = random.randint(1, 3)
                            if systemDamage == 1:
                                print('Your shields are damaged by the attack!')
                                cshield -= round(0.2 * shield)
                                hull -= pweapons - cshield
                                if cshield < 0:
                                    cshield = 0
                            if systemDamage == 2:
                                print('Your engines are damaged by the attack!')
                                cengines -= round(0.2 * engines)
                                hull -= pweapons - cshield
                                if cengines < 0:
                                    cengines = 0
                            if systemDamage == 3:
                                print('Your weapons are damaged by the attack!')
                                cweapon -= round(0.2 * weapon)
                                hull -= pweapons - cshield
                                if cweapon < 0:
                                    cweapon = 0
                    # Regular Rocket Attack
                    if scourgeAttack == 2:
                        print('The Scourge unleashes a salvo of small unguided rockets!')
                        if pcweapons <= cengines:
                            print('You manage to avoid the rockets with your incredible piloting')
                        else:
                            print('The rockets go straight through your shields and explode upon your ship')
                            systemDamage = random.randint(1, 3)
                            if systemDamage == 1:
                                print('Your shields are damaged by the attack!')
                                cshield -= round(0.2 * shield)
                                hull -= pweapons - cengines
                                if cshield < 0:
                                    cshield = 0
                            if systemDamage == 2:
                                print('Your engines are damaged by the attack!')
                                cengines -= round(0.2 * engines)
                                hull -= pweapons - cengines
                                if cengines < 0:
                                    cengines = 0
                            if systemDamage == 3:
                                print('Your weapons are damaged by the attack!')
                                cweapon -= round(0.2 * weapon)
                                hull -= pweapons - cengines
                                if cweapon < 0:
                                    cweapon = 0
                    # Railgun Charging
                    if scourgeAttack == 3:
                        print('The Scourge reroutes power to charge a more powerful attack!')
                        railgunCharged = True
                        railgunShield = pcshields - pshields * 0.6
                        railgunEngines = pcengines - pengines * 0.6
                        if railgunShield < 0:
                            railgunShieldBuffer = pcshields
                            pcshields = 0
                        else:
                            railgunShieldBuffer = 0
                        if railgunEngines < 0:
                            railgunEnginesBuffer = pcengines
                            pcengines = 0
                        else:
                            railgunEnginesBuffer = 0
                        pcshields -= pshields * 0.6
                        pcengines -= pengines *0.6
                        
                if hull <= 0:
                    living = False
                turn = 1
                input()
            else:
                print('\nHull: ', hull, '/', maxhull,
                      '\nScrap: ', scrap,
                      '\nShield: ', cshield, '/', shield,
                      '\nEngines: ', cengines, '/', engines,
                      '\nWeapons: ', cweapon, '/', weapon)
                eventinput = input('\n1. Fire regular weapons.'
                                   '\n2. Fire rockets.'
                                   '\n3. Repair shields.'
                                   '\n4. Repair engines.'
                                   '\n5. Repair weapons.'
                                   '\n6. Run a deeper scan of The Scourge.\n')
                if eventinput == '1':
                    if cweapon <= pcshields:
                        print('It doesn\'t appear that your lasers pierced The Scourge\'s shields.')
                    else:
                        print('Your lasers erupt on The Scourge\'s hull.')
                        systemDamage = random.randint(1, 3)
                        if systemDamage == 1:
                            pcshields -= round(0.2 * pshields)
                            phull -= round(weapon - pcshields)
                            if pcshields < 0:
                                pcshields = 0
                        if systemDamage == 2:
                            pcengines -= round(0.2 * pengines)
                            phull -= round(weapon - pcshields)
                            if pcengines < 0:
                                pcengines = 0
                        if systemDamage == 3:
                            pcweapons -= round(0.2 * pweapons)
                            phull -= round(weapon - pcshields)
                            if pcweapons < 0:
                                pcweapons = 0
                if eventinput == '2':
                    if cweapon <= pcengines:
                        print('The Scourge outmaneuvers your rockets.')
                    else:
                        print('The explosions of the rockets blossom upon The Scourge.')
                        systemDamage = random.randint(1, 3)
                        if systemDamage == 1:
                            pcshields -= round(0.2 * pshields)
                            phull -= round(weapon - pcshields)
                            if pcshields < 0:
                                pcshields = 0
                        if systemDamage == 2:
                            pcengines -= round(0.2 * pengines)
                            phull -= round(weapon - pcshields)
                            if pcengines < 0:
                                pcengines = 0
                        if systemDamage == 3:
                            pcweapons -= round(0.2 * pweapons)
                            phull -= round(weapon - pcshields)
                            if pcweapons < 0:
                                pcweapons = 0
                if eventinput == '3':
                    print('Your shield generators have been repaired somewhat.')
                    cshield += round(shield * shieldrow)
                    if cshield > shield:
                        cshield = shield
                    enginesrow = 0.1
                    weaponrow = 0.1
                    shieldrow += 0.1
                if eventinput == '4':
                    print('Your engines have been repaired somewhat.')
                    cengines += round(engines * enginesrow)
                    if cengines > engines:
                        cengines = engines
                    enginesrow += 0.1
                    weaponrow = 0.1
                    shieldrow = 0.1
                if eventinput == '5':
                    print('Your weapon systems have been repaired somewhat.')
                    cweapon += round(weapon * weaponrow)
                    if cweapon > weapon:
                        cweapon = weapon
                    enginesrow = 0.1
                    weaponrow += 0.1
                    shieldrow = 0.1
                if eventinput == '6':
                    print('\nScourge Hull:', phull,
                          '\nScourge Shields:', pcshields,
                          '\nScourge Engines:', pcengines,
                          '\nScourge Weapons:', pcweapons)
                input()
                turn = 0
        gamebeaten = True
        if phull <= 0:
            print('Congratulations! You have destroyed the scourge and beaten the game!'
                  '\nYou are free to continue if you wish.')
            if prestige == 0:
                print(playername, 'has beaten SpaceAge on: ' + difficulty + ' difficulty.')
            else:
                print(playername, 'has beaten SpaceAge on: ' + difficulty + ' difficulty, Crystal Core: ' + str(prestige))
        if hull <= 0:
            living = False
        if difficulty == 'True Masochist' and prestige == 0:
            print("""Since you've beaten the game on True Masochist, you now gain
                  access to\n the Crystal Core prestige levels, this ramps up the difficulty
                  of each event, but you get a \nbuff to your stats at the start and get to
                  brag to the friends you may or may not have. Note: this is supposed to be secret\n
                  content so please do not tell anyone that this exists!""")
        if difficulty == 'True Masochist':
            prestige += 1
        try:
            playAgain = input("Would you like to do another run? (y/n)").lower()[0]
        except:
            playAgain = "y"
        if playAgain == "y":
            statArray = getDifficulty(prestige).split(":")
            hull = int(statArray[0])
            maxhull = int(statArray[1])
            shield = int(statArray[2])
            engines = int(statArray[3])
            weapon = int(statArray[4])
            scrap = int(statArray[5])
            living = bool(statArray[6])
            difficulty = str(statArray[7])
            zoneSafety = int(statArray[8])
            gamebeaten = False
        saveScumCounter += callSave(input('Press \'Enter\' to continue'))
        saveScumCounter = max(0, saveScumCounter)
        print('\n' * 100)
    zoneSafety -= 1
    saveScumCounter += callSave(input('Press \'Enter\' to continue'))
    saveScumCounter = max(0, saveScumCounter)
    print('\n' * 100)
    
print('The last explosions mark the fate of your ship as it is ripped apart.')
input('oof')
