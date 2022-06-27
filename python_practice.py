

val = 5
for val_low in range(val):    #5번 반복해준다
     for val_de in range(val-val_low-1): #5-val_low-1을 한만큼 반복한다.
          print(" ",end = "")    # 공백을 출력하고 마지막은 없음을 출력해준다.
     
     val_add=(val_low+1)*2-1  
     for val_hi in range(val_add):  #별을 출력할수 있는 횟수
          if val_hi == 0 or val_hi == val_add-1 or val_add == 9: #val_hi가 val_add값이 같아야 마지막부분에 별을 출력시킬수있다.
               print("*",end="")
          else:                                                  # 조건값이 아닌경우에는 공백을 출력해준다.
               print(" ", end="")     
               
           
     print() # 코드가 넘어 오면 줄을 바꿔준다.
     
     

     
