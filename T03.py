def writeDistanced():

  nX=nY=8    #
  for a in range(1,nY+1):
    for b in range(1,nX+1):

      for a2 in range(1,nY+1):
        for b2 in range(1,nX+1):

          if((a2==a)&(b2==b)):
            continue

          distance=sqrt((a2-a)**2+(b2-b)**2)
          print(a,b,"to",a2,b2,"distance",distance)



  writeDistanced()
