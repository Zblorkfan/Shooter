def ptn(): 
    import pygame
    # importing tkinter module
    import random
    import time
    pygame.mixer.init() 
    gunsound = pygame.mixer.music.load("GUN.mp3") 

     
    # getting screen's height in pixels

    # infinite loop
    pygame.init()
    pygame.display.set_caption('Shooter game')


    Icon = pygame.image.load('bgrd.png')


    pygame.display.set_icon(Icon)
      
    # Creating a canvas of 600*400
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((infoObject.current_w , infoObject.current_h))
    image = pygame.image.load("bh.png").convert_alpha()
    image = pygame.transform.scale(image, (100, 200))
    surf = pygame.Surface((60, 60), pygame.SRCALPHA)
    pygame.draw.rect(surf, (255, 0, 0), [0, 25, 25, 10])
    pygame.draw.rect(surf, (255, 0, 0), [25, 25, 25, 10])
    pygame.draw.rect(surf, (255, 0, 0), [20, 35, 10, 25])
    pygame.draw.rect(surf, (255, 0, 0), [20, 0, 10, 25])
    cursor3 = pygame.cursors.Cursor((20, 5 ), surf)
    s = infoObject.current_w-200
    img_pos = random.randint(0, s) 
    mg_pos = infoObject.current_h-250 
    # the arguments to set_cursor can be a Cursor object
    # or it will construct a Cursor object
    # internally from the arguments
    pygame.mouse.set_cursor(cursor3)
    number_points = 0
    imagegun = pygame.image.load("gun.png").convert_alpha()
    imagegun = pygame.transform.scale(imagegun, (474, 355))
    background = pygame.image.load('bgrd.png')
    cotinu = True 
    ptnsamere = False
    while cotinu :

        screen.fill("white")
        screen.blit(background, (0, -200))
        rectplace = screen.blit(image, (img_pos, mg_pos ))
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        xBite, yBite = pygame.mouse.get_pos() 
        screen.blit(imagegun, (xBite, infoObject.current_h -405))
        if pressed1 :
              pygame.mixer.music.play(10, 0.0)  
        if rectplace.collidepoint(pos) and pressed1:
              number_points += 1
              s = infoObject.current_w-200
              img_pos = random.randint(0, s)
              mg_pos = infoObject.current_h-250
              rectplace = screen.blit(image, (img_pos,mg_pos ))
              
       
            
        
        for event in pygame.event.get():
      
           if event.type == pygame.KEYDOWN:

              pygame.quit()
              raise SystemExit

        
             

            
        pygame.display.flip()
ptn()
