def fade(strip,LED_COUNT):
     """try and change light values by small increments to
     see if ligts continue to fuck up"""
     r = 0
     g = 155
     b = 250

     ri = 1
     gi = 2
     bi = 2

     while True:
        if (r <= 0) or (r >= 250):
             ri *= 1
        if (g <= 0) or (g >= 250):
             gi *= 1
        if (b <= 0) or (b >= 250):
            bi *= 1

        r += ri
        g += gi
        b += bi
        for i in range(LED_COUNT):
      	   strip.setPixelColor(r, g, b)
        strip.show()
        sleep(50)
