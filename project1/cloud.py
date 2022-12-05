
import random
adjective = [];
noun = [];
noun1 = [];
noun2 = [];



option1 = int(input("enter 1 for for monster story, enter 2 for pet story, enter 3 to exit"));

while option1 != 3:
    if option1 == 1:

        for i in range(3):
            adj = input("please enter a adjective");
            adjective.append(adj);

        for i in range(3):
            animal3 = input("please enter a animal");
            noun.append(animal3);

        for i in range(1):
            person1 = input("please enter a person");
            noun1.append(person1);

        for i in range(3):
            fruit2 = input("please enter a place");
            noun2.append(fruit2);

        animal = random.choice(noun);
        person = random.choice(noun1);
        print("your story is: There once was a " + " " + random.choice(adjective) + " " + animal + " that lived on a abandon farm. Who would scare all the children that lived in the town. One day a "
              + person + " rose up and decided that he has had enough of the " + random.choice(adjective) +
              " " + animal + " and decided he would do all in his power to bring a end to the " + animal +
              ". So he grabbed his knife and went into the woods to find the " + animal +
              ". After many days of hiking in the woods he finally found the " + animal + " lying in a " + random.choice(noun2)
              + " fast asleep. after see the " + animal + " sleeping. The " + person + " quickly sliced the "
              + animal + " til it came to a end. When the man returned with the news of the " + animal +
              " being dead, all of the people in town were happy and gave the " + person + " a great big hug. The end.");
        break

    elif option1 == 2:

        for i in range(3):
            adj = input("please enter a adjective");
            adjective.append(adj);

        for i in range(3):
            animal3 = input("please enter a animal");
            noun.append(animal3);

        for i in range(2):
            person1 = input("please enter a person");
            noun1.append(person1);

        animal = random.choice(noun);
        person = random.choice(noun1);

        print("your story is: There once was a boy who owned a " + animal + ". The boy loved his " + animal +
              " more than anything in the world. One day a " + person + " saw the boy playing with his " + animal +
              " in the woods and ran to the king to tell him that he saw a " + random.choice(adjective) + animal +
              " in the woods. The king said he would send some of his knights to look into the "
              + person + "s story. After looking all over the woods, one of the knights told the rest of them "
                         "that he found the " + random.choice(adjective) +
              animal + " sleeping with the boy. After hearing that the beast was found. The men quickly"
                       "ran up to the boy and push him out of the way and tackled the " + random.choice(adjective) +
              " " + animal + " to the ground. The boy screamed in anger as the knights hauled the " + animal +
              " away. After the knights had left, the boy quickly ran to the king to beg him to release his pet "
              + animal + " the king told the boy that the "
              + animal + " was a threat to the kingdom and that it had to be extinguished "
                         "the boy was sad that they were putting his pet " +
              animal + " down, but he knew deep down that it was to dangerous to be kept alive. As the beast "
                       " was slowly dying the boy could hear it faintly say I will always love you. The end");
        break;
