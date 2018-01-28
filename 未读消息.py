from PIL import Image,ImageDraw,ImageFont
im = Image.open("D:\\Downloads\\first.jpg")#创建图片对象
w,h = im.size#获取图片对象的宽和高
font = ImageFont.truetype('D:\\Downloads\\HBuilder.8.8.7.windows\\HBuilder\\jre\\lib\\fonts\\LucidaSansRegular.ttf',int(h/5))
#创建字体对象，
ImageDraw.Draw(im).pieslice([(w/4*3,0),(w,h/4)],0,360,fill='red')
ImageDraw.Draw(im).text((w*0.8,h*0.02),'5',font=font,fill='white')
im.show()