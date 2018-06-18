#made by J-VdS on 18-06-2018

from PIL import Image
import os, glob

namefolder = input('give name of folder you want to make. ')
os.mkdir(namefolder)

for name in glob.glob('*.png'):
    a = Image.open(name)
    w, h= a.size
    a.resize((30*w//8,30*h//8)).save(namefolder+'/'+name[:-4]+'.gif')


