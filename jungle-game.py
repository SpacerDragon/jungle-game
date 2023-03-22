# Simple text game made while learnin python
# Date 22.03.23
# Author: Per Idar Rød.
# Mail: python@peridar.net
# ------------------------------------------

from sys import exit
from random import randint
from textwrap import dedent


# game main runner
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


# global variables
scenes_visited = []
food_in_pocket = False
matches = None
fireworks = False
princess = None


class Scene(object):

    def enter(self):
        print('Hello there.')
        exit(1)


# scenes classes
class Jungle(Scene):

    def enter(self):
        if 'jungle' not in scenes_visited:
            print(dedent("""
                You find yourself in the middle of nowhere, in a jungle.
                You have abolutely no idea how you got there.
                The last thing you remember is that you
                were drinking coffey with your neighbor.
                Here you see monkeys, small snakes,
                and all sorts of animals, climbing around.
                In there, between some trees, you see a house.
                What would you like to do?
                Climb(1), walk in the jungle(2) or go to the house(3)?
                """))
        else:
            scenes_visited.append('jungle')
            print(dedent("""
                You are now outside the house.
                What do you want to do?
                """))
            action = input('Go back inside(1) or go into the jungle(2)\n> ')
            if action == '1':
                return 'hall'
            elif action == '2':
                print(dedent("""
                    You decide to walk away from the house
                    and deeper into the jungle.
                    Suddenly there was a giant white lamb.
                    Mary's white lamb. Oh no, you start
                    running but a little too late. The giant lamb steps on you,
                    and well, you're flat
                    and in two pieces.
                    """))
                return 'death'

        action = input('> ')
        if action == '1':
            print(dedent("""
                You start climbing one of the largest trees you find.
                Up, up, up, you go. Step on a rotten branch, and fall.
                You thought you were going to die from the fall,
                but just before you hit the ground, a dinosaur-bird
                like createure grabs you with its claws,
                throws you up in the air and swallaws you whole.
                """))
            return 'death'

        elif action == "2":
            print(dedent("""
                You decide to walk away from the house,
                and deeper into the jungle.
                Suddenly there was a giant white lamb.
                Mary's white lamb. Oh no, you start
                running but a little too late. The giant lamb steps on you,
                and well, you're flat and in two pieces.
                """))
            return 'death'

        elif action == '3':
            scenes_visited.append('jungle')
            print(dedent("""
                You walk towards the house.
                Then you open the door, and go inside.
                """))
            return 'hall'

        else:
            print('DOES NOT COMPUTE')
            return 'jungle'


class Hall(Scene):

    def enter(self):

        text = (dedent("""
            In here you see three doors.
            One on your left, one in front of you,
            and one on your right side.
            Which one do you want to open?
            """))

        if scenes_visited[-1] == 'jungle':
            print(text)
            action = input('Left(1), Front(2) or Right(3) \n> ')
            if action == '1':
                return 'food_room'

            elif action == '2':
                return 'cow_room'

            elif action == '3':
                return 'stair_room'

            else:
                return 'hall'

        elif scenes_visited[-1] == 'food_room':
            print(text)
            action = input('Left(1), Front(2) or Right(3) \n> ')
            if action == '1':
                return 'cow_room'

            elif action == '2':
                return 'stair_room'

            elif action == '3':
                return 'jungle'

            else:
                return 'hall'

        elif scenes_visited[-1] == 'stair_room':
            print(text)
            action = input('Left(1), Front(2) or Right(3) \n> ')
            if action == '1':
                return 'jungle'

            elif action == '2':
                return 'food_room'

            elif action == '3':
                return 'cow_room'

            else:
                return 'hall'

        elif scenes_visited[-1] == 'cow_room':
            print(text)
            action = input('1Left(1), Front(2) or Right(3) \n> ')
            if action == '1':
                return 'stair_room'

            elif action == '2':
                return 'jungle'

            elif action == '3':
                return 'food_room'

            else:
                return 'hall'
        elif scenes_visited[-1] == 'tunnel':
            print(text)
            action = input('Left(1), Front(2) or Right(3) \n> ')
            if action == '1':
                return 'jungle'

            elif action == '2':
                return 'food_room'

            elif action == '3':
                return 'cow_room'

            else:
                return 'hall'
        else:
            return 'hall'


class CowRoom(Scene):

    def enter(self):
        scenes_visited.append('cow_room')
        global food_in_pocket
        global matches
        print(dedent("""
            This is a special room. In this room there is a cow.
            A cow with a human face. It says it it really hungry.
            What do you do?
            """))
        text = (dedent("""
            "Do you think you can leave this room without giving me some food?"
            The cow says. "Sure I can", you say, and walk towards the door.
            Kaboom. Something hit you hard from behind,
            and crushes you againts the wall.
            That's the last feeling you'll ever have.
            """))
        if food_in_pocket:
            action = input('Feed the cow(1), leave(2)\n> ')
            if action == '1' or action == 'feed the cow' or action == 'feed':
                food_in_pocket = False
                print(dedent("""
                    You open some cans of food and give to the cow.
                    It's really grateful and thanks you a lot.
                    It gives you a box of matches for the food.
                    You then go for the door back to the hall.
                    """))
                matches = True
                return 'hall'
            elif action == '2' or action == 'leave':
                print(text)
                return 'death'

        else:
            action = input('leave(1)\n> ')
            if action == '1' or action == 'leave':
                print(text)
                return 'death'


class FoodRoom(Scene):

    def enter(self):
        scenes_visited.append('food_room')
        global food_in_pocket
        if not food_in_pocket:
            print(dedent("""
                This room is full of shelves.
                The shelves is stacked up with food in cans.
                What do you do? Fill up your pockets, or leave it all as it is?
                """))
            action = input('stack up(1) or leave(2) ? \n> ')
            if action == 'stack' or action == '1':
                print(dedent("""
                    You stack your pockets full of food.
                    It just might come in handy...
                    Then you go back out.
                    """))
                food_in_pocket = True
                return 'hall'
            elif action == 'leave' or action == '2':
                print(dedent("""
                    You leave the food as it is.
                             """))
                return 'hall'
        elif food_in_pocket:
            print(dedent("""
            This room is full of shelves.
            The shelves is stacked up with food in cans.
            Your pockets is already filled to the
            rim with food cans.
            What do you do?
            """))
            action = input('Go back out(1), or Lie down(2)\n> ')
            if action == '1' or action == 'go back':
                print('You go back out')
                return 'hall'
            elif action == '2' or action == 'lie down':
                print(dedent("""
                You take a break and lie down to rest.
                You fall asleep, and in your sleep,
                you're stung by a poisenous scorpion.
                """))
                return 'death'


class StairRoom(Scene):

    def enter(self):
        scenes_visited.append('stair_room')
        print(dedent("""
            In here you see a stairwell leading down.
            That's all there is.
            What do you do?
            Go down the stairs, or go back out?
            """))
        action = input('Go down(1) or go back out(2)? \n> ')
        if action == '1' or action == 'go down':
            print('You walk down the dark stairs')
            return 'cave_entrance'

        elif action == '2' or action == 'go back':
            print('You go back out the door')
            return 'hall'
        else:
            print('DOES NOT COMPUTE')
            return 'stair_room'


class CaveEntrance(Scene):

    def enter(self):
        global princess
        if princess:
            scenes_visited.append('cave_entrance')
            print(dedent("""
            You are now back in the cave with the beautiful
            princess. You go back around the corner, and
            through the iron door.
            The princess and you are standing there,
            staring at the big old oak door.
            'I wonder what's in there', she says.
            'Let's find out' you say.
            You try to kick the door in, but you failed
            miserably. Not beeing as cool as the hero you
            want to be. 'Do you need this?' she asks you.
            She's holding up a old iron key.
            'Where did you get that?'
            'I had it in my pocket, I stole it from the man who
            tied me up.'
            You take the key and try it in the door. It works.
            Both of you slowly push the door open, and go in."""))
            return 'snake_room'
        elif not fireworks:
            scenes_visited.append('cave_entrance')
            print(dedent("""
            You are now in a small cave.
            On your right you see a solid oak door.
            Straight ahead you see a door made of iron bars.
            Where do you go?
            """))
            action = input('Oak door(1) or Iron-door(2) ? \n> ')
            if action == '1' or action == 'oak':
                print(dedent("""
                You go over to the oak door.
                You open it and go through.
                """))
                return 'snake_room'

            elif action == '2' or action == 'iron':
                print(dedent("""
                You walk ahead to the iron door.
                You see that the lock is damaged.
                You push the heavy door open,
                and go in.
                """))
            return 'cave'
        elif fireworks and scenes_visited[-1] == 'cave':
            print(dedent("""
            You are now back in the small cave.
            On your left side is the oak door.
            Behind you is the door to the large cave.
            In front of you is the stairs.
            What do you want to do?
            """))
            action = input('Left(1) or Back(2) or Stairs(3) ?\n > ')
            if action == '1' or action == 'left':
                print(dedent("""
            You try to open the door with one hand,
            while holding the box of fireworks with your other.
            Of course you drop the box, it self-ignites, and you
            burn to an agonizing death with the sound of fireworks
            ringing in your ears.
            """))
                return 'death'
            elif action == '2' or action == 'back':
                print(dedent("""
            You decide to go back into the large cave.
            Suddenly a giant spider comes out from the shadows.
            You must have awoken it the last time you were in here.
            The spider is super fast and it eats you.
            """))
                return 'death'
            elif action == '3' or action == 'stairs':
                print(dedent("""
            You try to walk up the stairs with the heavy
            box of fireworks in your hands. You take a bad
            step and fall. You go up in flames, along with all
            the fireworks.
            """))
                return 'death'


class SnakeRoom(Scene):

    def enter(self):
        global princess
        if not princess:
            print(dedent("""
            The door is locked, you do not
            have a key.
            """))
            return 'cave_entrance'
        else:
            scenes_visited.append('snake_room')
            print(dedent("""
            In here you see a giant anaconda.
            It's lying in front of another door.
            Both of you walk closer to the snake.
            'Hello there', the snake says.
            'Hello yourself', you reply.
            'What do you wantss'
            'We want to go through that door behind you'.
            'Imposssibles'
            'Why?'
            'You have to answers a riddles correctlyss,
            if you wantsss to go outsss thiss doorss'
            'What's the riddle then?'
            'What's my namessss?'
            """))
            action = input('Conda(1), Honda(2), Ponda(3)\n> ')
            if action == '1' or action == 'conda':
                print("That's wrongsss, now I will eats you boths")
                return 'death'
            elif action == '2' or action == 'honda':
                print("That's wrongsss, now I will eats you boths")
                return 'death'
            elif action == '3' or action == 'ponda':
                print(dedent("""
            Correctsss, you cans goess'
            The snake moves out of the way and both of you go
            through the door.
            You get the princess of the jungle out,
            and the two of you live happily ever after.
            Good job, you win.
            """))
            return 'finished'


class Cave(Scene):

    def enter(self):
        global fireworks
        global princess
        if not princess:
            scenes_visited.append('cave')
            print(dedent("""
            You are now in a huge cave.
            It's dimly lit by some small cracks,
            that lets small beams of sunlight in.
            To the right you see that the cave keeps on
            going as far as you can see.
            To the left you see that it turs left.
            You follow the left wall and spot a box of
            fireworks, standing beside the entrance to a tunnel.
            You see that the tunnel is filled with spideweb and spiders.
            What do you want to do?
            """))
            action = input('Ignite the fireworks in the tunnel(1)\n'
                           'Take the box of fireworks with you(2) '
                           '\n> ')
            if action == '1' or action == 'ignite':
                return 'tunnel'
            elif action == '2' or action == 'take':
                print(dedent("""
                    You take the fireworks, and go back out.
                """))
                fireworks = True
            return 'cave_entrance'
        elif princess:
            scenes_visited.append('cave')
            return 'cave_entrance'


class Tunnel(Scene):
    def enter(self):
        global princess
        global matches
        scenes_visited.append('tunnel')
        if matches:
            print(dedent("""
            You put the box of fireworks into the tunnel,
            take your matches and light up the fuse.
            You go a few steps away from it and wait...
            Kaboom. The sound of this reminds you of new years
            eve at twelve o'clock. When the echoing of the thunder-like
            sound in the tunnel finally ceases, you hear a womans voice
            calling for help. The voice comes from far into the tunnel.
            What do you do?
            """))
            action = input('Go into the tunnel to find the woman(1)\n'
                           'Go back out of the tunnel(2) \n> ')
            if action == '1' or action == 'find':
                print(dedent("""
                You crawl further into the tunnel to
                search for the woman. At last you come to a small door.
                You open it and crawl in. There you see the most
                beautiful woman you have ever seen. A princess of course.
                You see that she is tied up
                with rope to an anchor on the floor.
                I'm here to save you', you say. She smiles at you and say:
                'Finally, my hero, get me out of here,
                and I'll be yours forever'.
                You get her untied, and tell her to crawl out the tunnel."""))
                princess = True
                return 'cave'
            elif action == '2' or action == 'go out':
                print(dedent("""
                You back out of the tunnel, only
                thinking about yourself. Suddenly there
                is an earthquake and the whole cave
                comes down on top of you.
                """))
                return 'death'
        elif not matches:
            print(dedent("""
            You don't have anything to ignite the fireworks with.
            What do you do?
            """))
            action = input('Go back upstairs(1)\n'
                           'Try to ignite it with a rock you pick up(2)\n> ')
            if action == '1' or action == 'go up':
                print(dedent("""
                You go back to the small cave, and up the stairs.
                """))
                return 'hall'
            elif action == '2' or action == 'ignite':
                print(dedent("""
                You use your rock to try to make some sparks.
                You succede, but one spark hit directly at the
                base of the fuse. Kaboom!!!
                """))
                return 'death'


class Death(Scene):

    quips = [
        "Good job. You died.",
        "Better luck next time.",
        "It's good that this is just a game, don't you think?",
        "Come on, you can do better than this.",
        "Do you feel lucky, punk?"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class Finished(Scene):

    def enter(self):
        exit(0)


# this is for changing scenes
class Map(object):

    scenes = {
        'jungle': Jungle(),
        'hall': Hall(),
        'cow_room': CowRoom(),
        'food_room': FoodRoom(),
        'stair_room': StairRoom(),
        'cave_entrance': CaveEntrance(),
        'snake_room': SnakeRoom(),
        'tunnel': Tunnel(),
        'cave': Cave(),
        'finished': Finished(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        # print(type(val))
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('jungle')
a_game = Engine(a_map)
a_game.play()
