# author：Nicolo
# time：2017/7/23
# function:生成汉字字库并转换为图片
import codecs 
import os 
import pygame 
start,end = (0x4E00, 0x9FA5) 
with codecs.open("chinese.txt", "wb", encoding="utf-8") as f: 
 for codepoint in range(int(start),int(end)): 
  f.write(chr(codepoint)) 


chinese_dir = 'chinese' 
if not os.path.exists(chinese_dir): 
 os.mkdir(chinese_dir) 
 
pygame.init() 
start,end = (0x4E00, 0x9FA5)#汉字编码范围 
for codepoint in range(int(start),int(end)): 
 word = chr(codepoint) 
 font = pygame.font.Font("C:\Windows\Fonts\STZHONGS.TTF", 22)#当前目录下要有微软雅黑的字体文件msyh.ttc,或者去c:\Windows\Fonts目录下找 
 rtext = font.render(word, True, (0, 0, 0), (255, 255, 255)) 
 pygame.image.save(rtext, os.path.join(chinese_dir,word+".png")) 