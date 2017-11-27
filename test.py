import pygame
import os, sys
import logging
import time
import pendulum

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

pygame.mouse.set_visible(False)

lcd = pygame.display.set_mode((320, 240), pygame.FULLSCREEN)
font_big = pygame.font.SysFont('freemono', 40)
font_small = pygame.font.SysFont('freemono', 15)
bg_color = (0, 0, 0)
font_color = (255, 255, 255)

logger.info(pygame.font.get_fonts())

# TODO: How do I know what time zone the device is in?
now = pendulum.now('America/New_York')

try:
	while True:
		currTime = time.strftime('%l:%M%p %Z')
		currDate = time.strftime('%B %d, %Y')

		lcd.fill(bg_color)
		text_surface = font_big.render('%s'%currTime, True, font_color)
		text_surface1 = font_small.render('%s'%currDate, True, font_color)
		rect = text_surface.get_rect(center=(150,115))
		rect1 = text_surface1.get_rect(center=(160,140))
		lcd.blit(text_surface, rect)
		lcd.blit(text_surface1, rect1)
		pygame.display.update()

		time.sleep(0.9)
except KeyboardInterrupt:
	logger.info("Exiting from KeyboardInterrupt")
	sys.exit()
