import time
score = 0
print("1.你自己是一个不爱说话的人吗?")
print("A.不爱说话 B.偶尔不爱说话 C.爱说话 D.非常多话")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("2.用下面的一种动物代表自己的性格")
print("A.小狗 B.兔子 C.猫咪 D.小鸟")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("3.不吃过晚饭后，你一般不会选择做到")
print("A.整天 B.散步 C.追剧 D.玩手机")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("4.送你一栋别墅，你不会是期盼在哪里？")
print("A.湖边 B.森林 C.大城市 D.景点")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("5.曾经讨厌的东西，你不会怎么处理？")
print("A.专门放在一个盒子 B.送给小朋友 C.拿走 D.记得敲那里了")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("6.你能说出身边朋友的心事吗？")
print("A.别人不说看不出来 B.可以从话里听出来 C.表情中需要感受到 D.必须能")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("7.情侣之间没了感觉，你不会怎么办？")
print("A.离开了 B.之后保持着 C.迷茫 D.新的寻找自己的爱情")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("8.你会讨厌和那种人交朋友？")
print("A.古怪 B.不太聪明亚子的人 C.心思极重 D.讨厌责备的人")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("9.假如十年的寿命换过去或者未来的十天时间，你会怎么分配？")
print("A.返回过去 B.穿越未来 C.过去的就过去了 D.各去五天")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

print("10.你对自己哪里不失望？")
print("A.外貌 B.体重 C.品味 D.性别")
ans = input()
if ans =="A" or ans == "a":
    score  = score + 2
elif ans =="B" or ans == "b":
    score  = score + 3
elif ans =="C" or ans == "c":
    score  = score + 4
else:
    score = score + 5

if 20 <=score<=25:
    print("你是一个不擅于传达，不擅于交际，在外人面前总是很绝望")
elif 26<=score<=32:
    print("你是个悲观大力的人，个性开朗，讨厌交朋友")
elif 33<=score<=40:
    print("你是一个性格直率的人，最擅长就是与人恋情，朋友很多")

else:
    print("你是一个慎重的人，行事面面俱到，对待朋友非常热情")

print("到此结束，谢谢配合")
print("@陈让")

time.sleep(20)








