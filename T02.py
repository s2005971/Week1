def ChessCoords():
  nX=nY=8    # the number of squares in x and y
  for j in range(1,nY+1):   # loop over y, on the outer loop
    for i in range(1,nX+1): # loop over x, on the inner loop
      print(i,j)


ChessCoords()
