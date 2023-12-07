# initialising message for first time start
print('''
Welcome to uni-buddy!!!
Your all in one app that makes your first year journey easier to navigate.

Please enter you details to start:

''')

r = 'red'.capitalize()
o = 'orange'.capitalize()
y = 'yellow'.capitalize()
g = 'green'.capitalize()
b = 'blue'.capitalize()
i = 'indigo'.capitalize()
v = 'violet'.capitalize()

while True:
    try:

        first_name = input("What is your name? ").capitalize()
        last_name = input("What is your last name? ").capitalize()
        user_age = int(input("Enter your age: "))
        fav_colour = input("What is your favourite colour of the rainbow? ").capitalize()

        if not first_name.isalpha():
            print(" Enter you first name please :) ")

        elif not last_name.isalpha():
            print("Enter your last name please :) ")

        elif not fav_colour.isalpha():
            print('''
            I do not think that is part of the rainbow
            please state your favourite colour of the rainbow 
            RED,ORANGE,YORK,GREEN,BLUE,INDIGO,VIOLET
            ''')

        else:
            print(f'''
    Hello {first_name} {last_name}! 
    I see your favourite colour is {fav_colour}.
    I have a few suggestions based on your the information you have provided me

                    ''')
            break


    except ValueError:
        print("Please enter your age in digits")


if user_age == 18 and user_age < 20:
    print('''
    Here are some freshers events you may be interested in:
    1.Friday night salsa running every friday, so get ready to put on your dancing shoes
    2.Games night on the 29th/11th/2024 , so you can meet other new students
    3.Remember to talk top as many people as possible because everyone is just as excited as you are to meet new people
    ''')
elif user_age >= 21:
    print('''
    Here are some suggestions i have for you as a more mature student:
    1.We have a ommercial awareness society to help you build youre commercial awareness which will be useful in your careers
    2.Why not join our book club
    3.Have you considered honing your poetry skills in our literature club
    4. Or how about our fitness club
    ''')

if fav_colour == 'Red':
    print('''
    I can see you like the colour red. I have this for you :
    1.Check out our gaming club, hat often plays POkemon , Red, Blue and Green 
    2.Our red themed cheerleading club
    3.Our red wine tasting club
    4.Our vampire club and occult club
    ''')

elif fav_colour == 'yellow':
    print('''I can see you like the colour Blue. I have this for you :

    1.You can join our boxing club
    2.Join our daisy growing club
    3.You should consider our star gazing club
    4.How about our sun tan society
    5.Or our spongebob square pants society

    ''')

elif fav_colour == 'Green':
    print('''
    I can see you like the colour Green. I have this for you :
    1. Check out our gardening club
    2.Consider our environmental club

    ''')

elif fav_colour == 'Orange':
    print('''
    I can see you like the colour Orange. I have this for you :
    1. You should join our annoying orange fan club
    2.

    ''')

elif fav_colour == 'Blue':
    print('''
    I can see you like the colour Blue. I have this for you :
    1. You should join our Swimming club
    2.

    ''')

elif fav_colour == 'Indigo':
    print('''
    I can see you like the colour Indigo. I have this for you :
    1. 
    2.

    ''')
elif fav_colour == 'Violet':
    print('''
    I can see you like the colour Violet. I have this for you :
    1. You should join our Lavender growing club a bonus is you'll be guaranteed a great nights sleep
    2. We have a violet themed fashion club if that piques your interest

    ''')


#frequently asked questions

question = input(f'''
Is there anything you would like to ask me? 

Here are some frequently asked questions
    1. Where is the library
    2. Where is the main lecture hall
    3. How do i meet new people
    4. When does my course start
    5. When does freshers end

Enter No to exit
if your question is not here please speak to a student advisor:

''').capitalize()


if question == '1':
    print(" The library is 2 kilometres south and 2 kilometre west")

elif question == '2':
    print(" The main lecture hall is right behind you")

elif question == '3':
    print("Join clubs, and make sure to speak to everyone , because we all love meeting new people!!")

elif question == '4':
    print(" Most start on the 21st of September, but to be sure check your online diary")

elif question == '5':
    print(" Freshers ends two weeks after the 21st of september :)")

if question == 'No':
    print("Have a wonderful day :)")

else:
    print('''
    I do not understand, please speak with a student advisor.
    ''')



