a, b = 179, 37

delitel = 0
umnozhenie = 0
while umnozhenie <= a:
    delitel += 1
    umnozhenie = b*delitel

delitel -= 1
print("Целочисленное деление a на b дает", delitel)
