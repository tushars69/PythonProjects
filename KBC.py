question=[
  ["What is the capital of India?", "Delhi", "Mumbai", "Chennai", "Kolkata", 1],
  ["What is the national bird of India?","Parrot","Crow","Peacock","Sparrow",3],
  ["What is the national animal of India?","Lion","Tiger","Elephant","Cow",2],
  ["What is the national flower of India?","Lotus","Rose","Sunflower","Lily",1],
  ["What is the national sport of India?","Cricket","Football","Hockey","Basketball",4],
  ["What is the national fruit of India?","Mango","Apple","Banana","Orange",1],
  ["What is the national river of India?","Ganga","Yamuna","Narmada","Brahmaputra",3],
  ["What is the national game of India?","Hockey","Cricket","Football","Kabaddi",2],
  ["What is the national language of India?","Hindi","English","Marathi","Tamil",1],
  ["What is the national currency of India?","Rupee","Dollar","Euro","Pound",1],
  ["What is the national flag of India?","Tricolor","Orange","White","Green",1],
  ["What is the national emblem of India?","Lion","Tiger","Elephant","Cow",2],
  ["What is the national motto of India?","Loyality","Dignity","Honesty","Unity",4],
  ["What is the national tree of India?","Banyan","Bamboo","Pine","Oak",2],
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
for i in range(0,len(question)):
  question=question[i]
  print(f"Question for Rs.{levels[i]}")
  print(f"{question[0]}")
  print(f"a.{question[1]}      b.{question[2]}")
  print(f"c.{question[3]}      d.{question[4]}")
  reply=int(input("Enter your answer(1-4)"))
  if(reply==question[-1]):
    print(f"Correct answer,you have won Rs.{levels[i]}")
    if(i==4):
      money=10000
    elif(i==9):
      money=320000
    elif(i==14):
      money=10000000
  else:
    print("Wrong answer!")
    break
print(f"Your take home money is {money}")
