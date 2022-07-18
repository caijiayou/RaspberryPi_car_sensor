from sub.compass import compass

while True:
    try:
        heading = compass()
        print ("Heading Angle = %d°" %heading)
    except:
        print('error')
        continue