next=True
while next==True:
  print('''
    1. Aries
    2. Leo
    3. Cancer
    4. Pisces
    5. Scorpio
    6. Taurus
    7. Sagittarius
    8. Gemini
    9. Virgo
    10. Libra
    11. Capricorn
    12. Aquarius
    ''')
  s=int(input("Pick your zodiac and press Enter\n"))
  if s==1:
    print("Today will be somehow good.Money which was stuck will be recovered now, it will increase liquidity in the business.\nThere will be some good news in terms of job, your performance will be good, and you will expect promotions.\nThere will be some good news in terms of legal matters also.")
  elif s==2:
    print("Today you will be happy.You will spend good time with your family or friends;\nyou may buy something for family or friends. Domestic harmony will be improved but you are advised to control your straightforwardness and harsh speaking.")   
  elif s==3:
    print("Today,you may likely feel internal strength; your internal energy may be helpful to complete your projects before the timeline.\nYou may likely hear some good news related to siblings.\nThere may likely to be some short trips related to business also possible.")
  elif s==4:
    print("Today,you will be blessed by a positive moon.Things will be under control now.\nIn partnerships, many issues will be resolved. You will start implementing new plans in your business.\nStudents will make quick decisions in terms of their career.Job seekers will hear good news in terms of new job opportunities.\nEgo issues between couples will be resolved now.")
  elif s==5:
    print("Today your losses will convert into profits now, which will increase your liquidity in the business.You will generate some extra income.\nKids' health will improve now.Love birds will make some decisions in terms of marriage.\nWith the help of wisdom, you will keep yourself safe from conspiracy against you.")
  elif s==6:
    print("Today,you may feel a positive energy.You may plan for higher studies to groom your career.\nYou may be busy with the kids.Students are advised to focus themselves towards their studies to achieve their desired goal.")
  elif s==7:
    print("Today,you will be busy at work.You will plan to make investments in the business in terms of growth.\nYou will be able to implement your plans easily, which will boost your confidence.You will be praised by your seniors; you will expect to get some important position in your work.")
  elif s==8:
    print("Today the moon is not favourable for you.Situations may be somehow disappointing; you may be impatient and not able to focus towards your goals.\nInvestments in the fixed assets are advised to be postponed for a while.")
  elif s==9:
    print("Today,time will be favourable.Your focus will be good.You will be busy with the implementation of your plans in terms of growth in the business.\nYour prestige in society will be increased.You will make some new partners in the business, which will give you benefits in the near future.")
  elif s==10:
    print("Today,you will feel dull;you will feel negativity pulling you back from making strong decisions,which will affect your professional commitments.\nYou will not be able to complete the task on time.It is advised to avoid adventure tours or rush driving.")
  elif s==11:
    print("Today,you will get ample opportunities in terms of work,which will grow your work.With the help of an influential person in terms of the partnership,you will get benefits in terms of your work.\nThere will be mental peace and happiness around you.Job seekers will hear good news in terms of suitable jobs.\nYou will plan to visit some spiritual places.")
  elif s==12:
    print("Today,the moon is negative,there will be some dullness in your nature,you will be arrogant,and it will affect your professional and domestic life.\nIt is advised to drive safely and shall avoid going on adventure tours.Couples and love birds are advised to keep some distance and control their tongue while speaking.")
  else:
    print("Hey.You entered invalid number.")
  next=True if input("Want to try again?? (Y/N)")=="Y" else False
  
  