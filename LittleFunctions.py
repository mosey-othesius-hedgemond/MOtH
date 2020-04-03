# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:45:22 2020

@author: xande
"""

    
               # THIS IS WHERE I PUT ALL MY LITTLE FUNCTIONS FOR TESTS AND STUFF#
   
import string
from random import randint
  
def arithmic_pro(s,p,l):
    x=[s+p*i for i in range(0,l)]
    return(x)
#**************************************************
  # arithmic_pro is a basic pattern generator, it creates a progression pattern  
  #s is the starting number, p is the "pace" or number added, and l is the lenght. s and l must be int, p must be int or float ##ps i know it can be 1 line
  # for ex. arithmic_pro(1,2,10) would return, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def up_low(s):
    alp='qwertyuiopasdfghjklzxcvbnm'
    hc=list(filter(lambda x:x==x.upper() and x.lower() in alp,s))
    lc=list(filter(lambda x:x!=x.upper() and x.lower() in alp,s))
    print(f"the number of uppercase is {len(hc)}")
    print(f"the number of lowercase is {len(lc)}")
#**************************************************
  #up_low is a character type counter, it counts the number of upper and lower case letters
  #s is the string that is passed in for counting. s must be a string
  #for ex. up_low('Ooh Boy Im Hungry') would return #the number of uppercase is 4, the number of lowercase is 10 
def lesser_of_two_evens(a,b):
    x=[(min(a,b) if (a%2==0 and b%2==0) else max(a,b)) for e in [1]]
    return(x)
#**************************************************
  #lesser_of_two_evens returns the lesser of two numbers if both numbers are even,returns the greater if one or both numbers are odd
  #a and b are the two numbers two be judged. a and b must be int or float ##ps i know it can be 1 line
  # for ex. lesser_of_two_evens(2,3) would return 3 
def animal_crackers(text):
    new=text.split()
    return(new[0][0].upper()==new[1][0].upper())
#**************************************************
  #animal_crackers takes a two word string and returns if both start with the same letter
  #text is the variable for the string. text must be a string that is .split-able
  #for ex. animal_crackers('Levelheaded Llama') would return true
def master_yoda(text):
    text=text.split(' ')
    text=text[::-1]
    text=' '.join(text)
    return(text)                                        #possible improvement
#**************************************************
  #master_yoda takes all words in a string and reverses their order
  #text is the variable for the string. text must be a string that is .split-able
  #for ex. master_yoda('I am home') would return "home am I"
def has_33(nums):
    for i in range(len(nums)-1):
        b=[True if (nums[i]==3 and nums[i+1]==3) else None for y in nums]
        return(all(b))                       
#**************************************************
  #has_33 returns true if the list contains a three next to a three
  #nums is the variable for the list to be iterated through. nums must be a list
  #for ex. has_33([1, 3, 3] would return true
def blackjack(a,b,c):
    if a+b+c<=21:
        return(a+b+c)
    if a+b+c>21 and a==11 or b==11 or c==11:
        if a+b+c-10>21:
            return('BUST')
        else:
            return(a+b+c-10)
    if a+b+c>21:
        return("BUST")
#**************************************************
  #blackjack is litteraly the game
  #a,b,c are the variables for the cards number. a,b,c must be intigers
  #for ex. blackjack(9,9,9) would return BUST
def summer_69(arr):
    new=0
    count=[1,2]
    for i in arr:
        if i==6 and len(count)==2:
            count.pop()
        if len(count)==2 or len(count)==0:
            new=new+i
        if len(count)==1 and i==9:
            count.pop(0)
    return(new)
#**************************************************
  #summer_69 takes in a list and adds all ints to a sum excluding the ones imbetween a 6 and a 9, this was made with the asumption that a 9 would always follow a 6
  #arr the list that gets itterated through. arr must be a list
  #for ex. summer_69([4, 5, 6, 1, 8, 9]) would return 9
def spy_game(heha):
    bomb=[0,0,7,'p']
    for i in heha:
        if bomb[0]==i:
            bomb.pop(0)
    return(bomb[0]=='p')
#**************************************************
  #spygame checks through a list to see if it contains 007 in order
  #heha is the variable for the list to be itterated through. heha must be a list
  #for ex. spy_game([1,0,2,4,0,5,7]) would return true         
def multiply(f):
    x=f.pop(0)
    for i in range(len(f)):
        x*=f[0]
        f.pop(0)
    return(x)
#**************************************************
 #multiply muliplys all numbers in a list
 #f is the variable asigned the list. it must be a list containing int or float
 #for ex. multiply([1,2,3,-4]) would return -24
def ispangram(str1,alphabet=string.ascii_lowercase):
    n=[]
    for i in str1.lower():
        if i in alphabet:
            n.append(i)
    return(len(set(n))==26)
#**************************************************
  #ispangram chencks is a setance is a panagram, meaning it contains all letters of the alphabet at least once.
  #stri is the string that gets iterated through, i bet you can guess what alphabet is. stri must be a string.
  #for ex. ispangram("The quick brown fox jumps over the laZy dog") would return true. 
def altcaps(b):
    even=b[::2]
    odd=b[1::2]
    new=''
    for i in range(0,len(even)): 
      if len(even)>0:
            new=new+even[0]
            even=even[1::]
      if len(odd)>0:
            new=new+odd[0].upper()
            odd=odd[1::]
    print(new)
#**************************************************
  #altcaps capitalizes ever letter with an odd index
  #b is the string that gets edited. b must be a string
  #for ex. myfunc2('tickle me') would return "tIcKlE Me"
def C2F_or_F2C(jam):
    '''
    to change from celsius to fahrenheit, change the first number to a float.
    for ex [34.,23] 
    '''
    x=[]
    for i in jam:
        if type(i)==float:
            d=(i*9//5)+32
            x.append("{p:1.2f}F".format(p=d))
        else:
            d=(i-32)*5//9
            x.append("{p:1.2f}C".format(p=d))
    print(x)
#**************************************************
  #C2F_F2C is a celsius to fahrenheit, or, fahrenheit to celsius converter
  #jam is the list containing the temps to be converted. jam must be a list and can contain floats on ints
  #for ex. C2F_or_F2C([34, 34.]) would return ['1.00C', '93.00F'
def minioh3(jam,jelly,juice):
    x=0
    xx=[]
    xxx=[]
    while x<len(jam):
        xx.append(jam[x])
        xx.append(jelly[x])
        xx.append(juice[x])
        xxx.append(min(xx))
        x+=1
        xx=[]
    return(xxx)
#**************************************************
  #minioh3 takes three lists and finds the smallest value per index and appends it to a new list
  #jam, jelly, juice are the lists for itteration. jam, jelly, juice, must be lists and can contain floats or ints
  #for ex. minioh3([7,2,1,5,8],[0,1,5,3,8],[8,4,5,2,1]) would return [0, 1, 1, 2, 1] 
def minioh22(jam,jelly):
    x=0
    xx=[]
    for i in range(0,len(jam)):
        if jam[x]>jelly[x]:
            xx.append(jelly[x])
            x+=1
        else:
            xx.append(jam[x])
            x+=1
    return(xx)
#**************************************************
  #minioh22 takes 2 lists and finds the smallest value per index and appends it to a new list
  #jam, jelly are the lists for itteration. jam, jelly must be lists and can contain floats or ints.
  #for ex. minioh22([0,1,5,3,8],[8,4,5,2,1]) would return [0, 1, 5, 2, 1]
def bookfiller(x):
    thing=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}',';',':','"','<','>','?','/',' ','1','2','3','4','5','6','7','8','9','0']
    book=' '
    for jam in range(0,x):
        y=randint(0,87)
        book=book+thing[y]
    print(book)
#**************************************************
  #bookfiller a string with random characters from list thing
  #x is the lenght of the new string. x must be a int
  #for ex. bookfiller(10) COULD return "ezh8fi:V/L"
def fakeemail(count):
    y=0
    firstname=['Liam','Noah','William','James','Logan','Benjamin','Mason','Elijah','Oliver','Jacob','Lucas','Michael','Alexander','Ethan','Daniel','Matthew','Aiden','Henry','Joseph','Jackson','Samuel','Sebastian','David','Carter','Wyatt','Jayden','John','Owen','Dylan','Luke','Gabriel','Anthony','Isaac','Grayson','Jack','Julian','Levi','Christopher','Joshua','Andrew','Lincoln','Mateo','Ryan','Jaxon','Nathan','Aaron','Isaiah','Thomas','Charles','Caleb','Josiah','Christian','Hunter','Eli','Jonathan','Connor','Landon','Adrian','Asher','Cameron','Leo','Theodore','Jeremiah','Hudson','Robert','Easton','Nolan','Nicholas','Ezra','Colton','Angel','Brayden','Jordan','Dominic','Austin','Ian','Adam','Elias','Jaxson','Greyson','Jose','Ezekiel','Carson','Evan','Maverick','Bryson','Jace','Cooper','Xavier','Parker','Roman','Jason','Santiago','Chase','Sawyer','Gavin','Leonardo','Kayden','Ayden','Jameson','Kevin','Bentley','Zachary','Everett','Axel','Tyler','Micah','Vincent','Weston','Miles','Wesley','Nathaniel','Harrison','Brandon','Cole','Declan','Luis','Braxton','Damian','Silas','Tristan','Ryder','Bennett','George','Emmett','Justin','Kai','Max','Diego','Luca','Ryker','Carlos','Maxwell','Kingston','Ivan','Maddox','Juan','Ashton','Jayce','Rowan','Kaiden','Giovanni','Eric','Jesus','Calvin','Abel','King','Camden','Amir','Blake','Alex','Brody','Malachi','Emmanuel','Jonah','Beau','Jude','Antonio','Alan','Elliott','Elliot','Waylon','Xander','Timothy','Victor','Bryce','Finn','Brantley','Edward','Abraham','Patrick','Grant','Karter','Hayden','Richard','Miguel','Joel','Gael','Tucker','Rhett','Avery','Steven','Graham','Kaleb','Jasper','Jesse','Matteo','Dean','Zayden','Preston','August','Oscar','Jeremy','Alejandro','Marcus','Dawson','Lorenzo','Messiah','Zion','Maximus','River','Zane','Mark','Brooks','Nicolas','Paxton','Judah','Emiliano','Kaden','Bryan','Kyle','Myles','Peter','Charlie','Kyrie','Thiago','Brian','Kenneth','Andres','Lukas','Aidan','Jax','Caden','Milo','Paul','Beckett','Brady','Colin','Omar','Bradley','Javier','Knox','Jaden','Barrett','Israel','Matias','Jorge','Zander','Derek','Josue','Cayden','Holden','Griffin','Arthur','Holly','Felix','Remington','Jake','Killian','Clayton','Sean','Adriel','Riley','Archer','Legend','Erick','Enzo','Corbin','Francisco','Dallas','Emilio','Gunner','Simon','Andre','Walter','Damien','Chance','Phoenix','Colt','Tanner','Stephen','Kameron','Tobias','Manuel','Amari','Emerson','Louis','Cody','Finley','Iker','Martin','Rafael','Nash','Beckham','Cash','Karson','Rylan','Reid','Theo','Ace','Eduardo','Spencer','Raymond','Maximiliano','Anderson','Ronan','Lane','Cristian','Titus','Travis','Jett','Ricardo','Bodhi','Gideon','Jaiden','Fernando','Mario','Conor','Keegan','Ali','Cesar','Ellis','Jayceon','Walker','Cohen','Arlo','Hector','Dante','Kyler','Garrett','Donovan','Seth','Jeffrey','Tyson','Jase','Desmond','Caiden','Gage','Atlas','Major','Devin','Edwin','Angelo','Orion','Conner','Julius','Marco','Jensen','Daxton','Peyton','Zayn','Collin','Jaylen','Dakota','Prince','Johnny','Kayson','Cruz','Hendrix','Atticus','Troy','Kane','Edgar','Sergio','Kash','Marshall','Johnathan','Romeo','Shane','Warren','Joaquin','Wade','Leonel','Trevor','Dominick','Muhammad','Erik','Odin','Quinn','Jaxton','Dalton','Nehemiah','Frank','Grady','Gregory','Andy','Solomon','Malik','Rory','Clark','Reed','Harvey','Zayne','Jay','Jared','Noel','Shawn','Fabian','Ibrahim','Adonis','Ismael','Pedro','Leland','Malakai','Malcolm','Alexis','Kason','Porter','Sullivan','Raiden','Allen','Ari','Russell','Princeton','Winston','Kendrick','Roberto','Lennox','Hayes','Finnegan','Nasir','Kade','Nico','Emanuel','Landen','Moises','Ruben','Hugo','Abram','Adan','Khalil','Zaiden','Augustus','Marcos','Philip','Phillip','Cyrus','Esteban','Braylen','Albert','Bruce','Kamden','Lawson','Jamison','Sterling','Damon','Gunnar','Kyson','Luka','Franklin','Ezequiel','Pablo','Derrick','Zachariah','Cade','Jonas','Dexter','Kolton','Remy','Hank','Tate','Trenton','Kian','Drew','Mohamed','Dax','Rocco','Bowen','Mathias','Ronald','Francis','Matthias','Milan','Maximilian','Royce','Skyler','Corey','Kasen','Drake','Gerardo','Jayson','Sage','Braylon','Benson','Moses','Alijah','Rhys','Otto','Oakley','Armando','Jaime','Nixon','Saul','Scott','Brycen','Ariel','Enrique','Donald','Chandler','Asa','Eden','Davis','Keith','Frederick','Rowen','Lawrence','Leonidas','Aden','Julio','Darius','Johan','Deacon','Cason','Danny','Nikolai','Taylor','Alec','Royal','Armani','Kieran','Luciano','Omari','Rodrigo','Arjun','Ahmed','Brendan','Cullen','Raul','Raphael','Ronin','Brock','Pierce','Alonzo','Casey','Dillon','Uriel','Dustin','Gianni','Roland','Landyn','Kobe','Dorian','Emmitt','Ryland','Apollo','Aarav','Roy','Duke','Quentin','Sam','Lewis','Tony','Uriah','Dennis','Moshe','Isaias','Braden','Quinton','Cannon','Ayaan','Mathew','Kellan','Niko','Edison','Izaiah','Jerry','Gustavo','Jamari','Marvin','Mauricio','Ahmad','Mohammad','Justice','Trey','Elian','Mohammed','Sincere','Yusuf','Arturo','Callen','Rayan','Keaton','Wilder','Mekhi','Memphis','Cayson','Conrad','Kaison','Kyree','Soren','Colby','Bryant','Lucian','Alfredo','Cassius','Marcelo','Nikolas','Brennan','Darren','Jasiah','Jimmy','Lionel','Reece','Ty','Chris','Forrest','Korbin','Tatum','Jalen','Santino','Case','Leonard','Alvin','Issac','Bo','Quincy','Mack','Samson','Rex','Alberto','Callum','Curtis','Hezekiah','Finnley','Briggs','Kamari','Zeke','Raylan','Neil','Titan','Julien','Kellen','Devon','Kylan','Roger','Axton','Carl','Douglas','Larry','Crosby','Fletcher','Makai','Nelson','Hamza','Lance','Alden','Gary','Wilson','Alessandro','Ares','Kashton','Bruno','Jakob','Stetson','Zain','Cairo','Nathanael','Byron','Harry','Harley','Mitchell','Maurice','Orlando','Kingsley','Kaysen','Sylas','Trent','Ramon','Boston','Lucca','Noe','Jagger','Reyansh','Vihaan','Randy','Thaddeus','Lennon','Kannon','Kohen','Tristen','Valentino','Maxton','Salvador','Abdiel','Langston','Rohan','Kristopher','Yosef','Rayden','Lee','Callan','Tripp','Deandre','Joe','Morgan','Dariel','Colten','Reese','Jedidiah','Ricky','Bronson','Terry','Eddie','Jefferson','Lachlan','Layne','Clay','Madden','Jamir','Tomas','Kareem','Stanley','Brayan','Amos','Kase','Kristian','Clyde','Ernesto','Tommy','Casen','Ford','Crew','Braydon','Brecken','Hassan','Axl','Boone','Leandro','Samir','Jaziel','Magnus','Abdullah','Yousef','Branson','Jadiel','Jaxen','Layton','Franco','Ben','Grey','Kelvin','Chaim','Demetrius','Blaine','Ridge','Colson','Melvin','Anakin','Aryan','Lochlan','Jon','Canaan','Dash','Zechariah','Alonso','Otis','Zaire','Marcel','Brett','Stefan','Aldo','Jeffery','Baylor','Talon','Dominik','Flynn','Carmelo','Dane','Jamal','Kole','Enoch','Graysen','Kye','Vicente','Fisher','Ray','Fox','Jamie','Rey','Zaid','Allan','Emery','Gannon','Joziah','Rodney','Juelz','Sonny','Terrance','Zyaire','Augustine','Cory','Felipe','Aron','Jacoby','Harlan','Marc','Bobby','Joey','Anson','Huxley','Marlon','Anders','Guillermo','Payton','Castiel','Damari','Shepherd','Azariah','Harold','Harper','Henrik','Houston','Kairo','Willie','Elisha','Ameer','Emory','Skylar','Sutton','Alfonso','Brentley','Toby','Blaze','Eugene','Shiloh','Wayne','Darian','Gordon','London','Bodie','Jordy','Jermaine','Denver','Gerald','Merrick','Musa','Vincenzo','Kody','Yahir','Brodie','Trace','Darwin','Tadeo','Bentlee','Billy','Hugh','Reginald','Vance','Westin','Cain','Arian','Dayton','Javion','Terrence','Brysen','Jaxxon','Thatcher','Landry','Rene','Westley','Miller','Alvaro','Cristiano','Eliseo','Ephraim','Adrien','Jerome','Khalid','Aydin','Mayson','Alfred','Duncan','Junior','Kendall','Zavier','Koda','Maison','Caspian','Maxim','Kace','Zackary','Rudy','Coleman','Keagan','Kolten','Maximo','Dario','Davion','Kalel','Briar','Jairo','Misael','Rogelio','Terrell','Heath','Micheal','Wesson','Aaden','Brixton','Draven','Xzavier','Darrell','Keanu','Ronnie','Konnor','Will','Dangelo','Frankie','Kamryn','Salvatore','Santana','Shaun','Coen','Leighton','Mustafa','Reuben','Ayan','Blaise','Dimitri','Keenan','Van','Achilles','Channing','Ishaan','Wells','Benton','Lamar','Nova','Yahya','Dilan','Gibson','Camdyn','Ulises','Alexzander','Valentin','Shepard','Alistair','Eason','Kaiser','Leroy','Zayd','Camilo','Markus','Foster','Davian','Dwayne','Jabari','Judson','Koa','Yehuda','Lyric','Tristian','Agustin','Bridger','Vivaan','Brayson','Emmet','Marley','Mike','Nickolas','Kenny','Leif','Bjorn','Ignacio','Rocky','Chad','Gatlin','Greysen','Kyng','Randall','Reign','Vaughn','Jessie','Louie','Shmuel','Zahir','Ernest','Javon','Khari','Reagan','Avi','Ira','Ledger','Simeon','Yadiel','Maddux','Seamus','Jad','Jeremias','Kylen','Rashad','Santos','Cedric','Craig','Dominique','Gianluca','Jovanni','Bishop','Brenden','Anton','Camron','Giancarlo','Lyle','Alaric','Decker','Eliezer','Ramiro','Yisroel','Howard','Jaxx']
    lastname=['Smith','Johnson','Williams','Jones','Brown','Davis','Miller','Wilson','Moore','Taylor','Anderson','Thomas','Jackson','White','Harris','Martin','Thompson','Garcia','Martinez','Robinson','Clark','Rodriguez','Lewis','Lee','Walker','Hall','Allen','Young','Hernandez','King','Wright','Lopez','Hill','Scott','Green','Adams','Baker','Gonzalez','Nelson','Carter','Mitchell','Perez','Roberts','Turner','Phillips','Campbell','Parker','Evans','Edwards','Collins','Stewart','Sanchez','Morris','Rogers','Reed','Cook','Morgan','Bell','Murphy','Bailey','Rivera','Cooper','Richardson','Cox','Howard','Ward','Torres','Peterson','Gray','Ramirez','James','Watson','Brooks','Kelly','Sanders','Price','Bennett','Wood','Barnes','Ross','Henderson','Coleman','Jenkins','Perry','Powell','Long','Patterson','Hughes','Flores','Washington','Butler','Simmons','Foster','Gonzales','Bryant','Alexander','Russell','Griffin','West','Hayes']
    email=['@gmail.com','@yahoo.com']
    while y<count:
        fake=''
        x=randint(0,1000)
        fake=fake+firstname[randint(0,999)]
        fake=fake+lastname[randint(0,99)]
        fake=fake+str(x)
        fake=fake+email[randint(0,1)] 
        print(fake)
        y+=1
#**************************************************
  #fakeemail print a number of fake email names as a print, could be edited for a return.
  #count is the amount of emails wanted. count must be an int.
  #for ex. fakeemail(2) COULD return JaceRamirez511@gmail.com DallasWatson732@gmail.com 
def Necklace(a,b):
    if not len(a)==len(b):
      return(false)
    for i in range(0,len(a)):
      a=a[1::]+a[0]
      print(a)
      if a==b:
        print(True)
#**************************************************
  #Necklace checks if two strings have the same caractors, in the same order, but they can circle around.
  #a is the first sring to be checked, b is the second string that is need for the check. a and b must be strings
  #for ex. Necklace('abc','cab') would return true, and abc,bca,cab 
def Greatestfactor3(*args):
    loot=[]
    goods=[]
    for i in range(1, min(args)+1):
        for x in args:
            loot.append((i, (x/i)%1==0))
    for x in range(1, min(args)+1):
        if loot.count((x, True))==len(args):
          goods.append(x)
    print(f"{max(goods)} * {[x//max(goods) for x in args]}")
#**************************************************
  #Greatestfactor3 finds the greatest common factor from an undetermend amount of numbers. and the factors with the GTF factored out
  #args is the list of the numbers, they must be posotive whole numbers.
  #for ex. greatestfactor3(6, 24, 18) would return 6 * [1, 4, 3]
def MOtH(n, s):
      x=[x for x in range(1, n+1)]
      y=[x for x in range(1, n+1)]
      while len(y)>1:
          for i in x[s-1::s]:
              if i in y:
                  y.remove(i)
                  if len(y)==1:
                      break       
          x=x+y
      print(y[0])
   
    