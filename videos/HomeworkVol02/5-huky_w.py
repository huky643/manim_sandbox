#Created by @huky_w

#最水的代码，不接受反驳
#for?不存在的

from manimlib.imports import *
from manim_example.youtube import *
from manim_example.MyText import  *

class lianxi02(Scene):
    def construct(self):
        #证法5

        #<前言>

        #SCENE1:
        text1=Text("Created by huky_w",font="Monaco")
        text2=Text("我们的猜想:",font="楷体")
        text3=TexMobject("\\sum","^{n}","_{i=1}","{i^3}","=","(","\\sum","^{n}","_{i=1}","{i}",")","^2",stroke_width=0.5)
        
        text3.set_color_by_tex("^{n}",GOLD)
        text3.set_color_by_tex("\\sum",DARK_BLUE)
        text3.set_color_by_tex("{i=1}",YELLOW)
        text3.set_color_by_tex("(",RED)
        text3.set_color_by_tex(")",RED)

        group1=VGroup(text2,text3)

        text1.next_to(text2,UP)
        text2.scale(0.5)


        self.play(Write(text1))
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.play(text2.move_to,2*UP)
        self.play(Write(text3))
        self.wait()
        self.play(UnWriteRandom(group1))
        self.wait()


        #SCENE2:
        text4=Text("我们注意到",font="宋体",color=BLUE)
        text5=TexMobject("(","\\sum^","{n}_","{i=1}","{i}",")^","2")
        text6=Text("不就是一个边长为1+2+3+...+n的正方形的面积吗",font="楷体",stroke_width=0.5,color=GREEN)
        text7=Text("所以我们的目标就是构造正方形",font="仿宋",stroke_width=0.5,color=BLUE)

        text6.scale(0.5)
        text6.next_to(text5,DOWN)

        for i,color2 in zip(text5,[RED,PINK,ORANGE,YELLOW,GREEN,BLUE,PURPLE]):
            i.set_color(color2)

        group2=VGroup(text4,text5,text6)

        self.play(Write(text4))
        self.play(text4.move_to,2*UP)
        self.play(FadeInFromRandom(text5))
        self.play(Write(text6))
        self.wait()
        self.play(FadeOutFromRandom(group2))
        self.play(Write(text7),run_time=2)
        self.wait()
        self.play(UnWriteRandom(text7))

        #</前言>

        #<正片>

        #SCENE1:
        text8=Text("正片开始",font="宋体")
        self.play(ShowCreation(text8))
        self.play(FadeOutRandom(text8))
        self.wait()

        text9=Text("我们一出生就知道，一个数的立方等于其平方乘以它本身",font="宋体",color=DARK_BLUE)
        text10=Text("于是，我们可以把立方转化为平方",font="宋体",color=BLUE)
        text11=Text("这样就可以在平面上进行转化了",font="宋体",color=YELLOW)
        text12=TexMobject("1","^3","+","2","^3","+","3","^3","+","4","^3","+","5","^3","+","...","+","n","^3")

        for i,color3 in zip(text12,[RED,GOLD,ORANGE,PINK,GOLD,ORANGE,YELLOW,GOLD,ORANGE,GREEN,GOLD,ORANGE,BLUE,GOLD,ORANGE,GRAY,ORANGE,DARK_BLUE,GOLD]):
            i.set_color(color3)

        text9.scale(0.5)
        text9.move_to(2*UP)
        text10.next_to(text9,DOWN)
        text10.scale(0.5)
        text11.next_to(text10,DOWN)
        text11.scale(0.5)
        text12.next_to(text11,DOWN)

        group3=VGroup(text9,text10,text11)

        self.play(Write(text9),run_time=2.5)
        self.play(Write(text10),run_time=2.5)
        self.play(Write(text11),run_time=2.5)
        self.wait()
        self.play(Write(text12),run_time=2.5)
        self.play(UnWriteRandom(group3))

        #SCENE2:
        self.play(text12.to_edge,UP)
        text13=TexMobject("1×","1^2","+","2×","2^2","+","3×","3^2","+","4×","4^2","+","5×","5^2","+","...","+","n×","n^2")
        for i,color4 in zip(text13,[RED,GOLD,ORANGE,PINK,GOLD,ORANGE,YELLOW,GOLD,ORANGE,GREEN,GOLD,ORANGE,BLUE,GOLD,ORANGE,GRAY,ORANGE,DARK_BLUE,GOLD]):
            i.set_color(color4)
        
        text13.move_to(1.5*UP)

        self.play(TransformFromCopy(text12[0],text13[0]),TransformFromCopy(text12[1],text13[1]),TransformFromCopy(text12[2],text13[2]))
        self.play(TransformFromCopy(text12[3],text13[3]),TransformFromCopy(text12[4],text13[4]),TransformFromCopy(text12[5],text13[5]))
        self.play(TransformFromCopy(text12[6],text13[6]),TransformFromCopy(text12[7],text13[7]),TransformFromCopy(text12[8],text13[8]))
        self.play(TransformFromCopy(text12[9],text13[9]),TransformFromCopy(text12[10],text13[10]),TransformFromCopy(text12[11],text13[11]))
        self.play(TransformFromCopy(text12[12],text13[12]),TransformFromCopy(text12[13],text13[13]))
        self.play(TransformFromCopy(text12[14],text13[14]),TransformFromCopy(text12[15],text13[15]),TransformFromCopy(text12[16],text13[16]))
        self.play(TransformFromCopy(text12[17],text13[17]),TransformFromCopy(text12[18],text13[18]))
        self.play(FadeOut(text12),text13.move_to,3.5*UP)

        #SCENE3:
        #懒得用 for循环了()
        square1_1=Square(color=RED,fill_color=GRAY,fill_opacity=0.2,stroke_width=0.5)
        square2_1=Square(color=PINK,fill_color=GRAY,fill_opacity=0.2,stroke_width=0.5)
        square2_2=Square(color=PINK,fill_color=GRAY,fill_opacity=0.2,stroke_width=0.5)
        square3_1=Square(color=YELLOW,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square3_2=Square(color=YELLOW,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square3_3=Square(color=YELLOW,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square4_1=Square(color=GREEN,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square4_2=Square(color=GREEN,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square4_3=Square(color=GREEN,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square4_4=Square(color=GREEN,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square5_1=Square(color=BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square5_2=Square(color=BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square5_3=Square(color=BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square5_4=Square(color=BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        square5_5=Square(color=BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        squaren_1=Square(color=DARK_BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        squaren_2=Square(color=DARK_BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        squaren_3=Square(color=DARK_BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        squaren_4=Square(color=DARK_BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        squaren_5=Square(color=DARK_BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        squaren_6=Square(color=DARK_BLUE,fill_color=GRAY,fill_opacity=0.2,stroke_width=1)
        #不用copy和for是因为这样显得有排面=w=,而且很傻。。

        text14=Text("...",font="Monaco")
        text14.next_to(squaren_6,DOWN)

        square1_1.scale(0.1)
        square2_1.scale(0.2)
        square2_2.scale(0.2)
        square3_1.scale(0.3)
        square3_2.scale(0.3)
        square3_3.scale(0.3)
        square4_1.scale(0.4)
        square4_2.scale(0.4)
        square4_3.scale(0.4)
        square4_4.scale(0.4)
        square5_1.scale(0.5)
        square5_2.scale(0.5)
        square5_3.scale(0.5)
        square5_4.scale(0.5)
        square5_5.scale(0.5)
        squaren_1.scale(0.6)
        squaren_2.scale(0.6)
        squaren_3.scale(0.6)
        squaren_4.scale(0.6)
        squaren_5.scale(0.6)
        squaren_6.scale(0.6)

        square1_1.next_to(text13[0],DOWN)
        square2_1.next_to(text13[3],DOWN)
        square3_1.next_to(text13[6],DOWN)
        square4_1.next_to(text13[8],DOWN)
        square5_1.next_to(text13[12],DOWN)
        squaren_1.next_to(text13[17],DOWN)
        square2_2.next_to(square2_1,DOWN)
        square3_2.next_to(square3_1,DOWN)
        square3_3.next_to(square3_2,DOWN)
        square4_2.next_to(square4_1,DOWN)
        square4_3.next_to(square4_1,RIGHT)
        square4_4.next_to(square4_2,RIGHT)
        square5_2.next_to(square5_1,DOWN)
        square5_3.next_to(square5_2,DOWN)
        square5_4.next_to(square5_1,RIGHT)
        square5_5.next_to(square5_2,RIGHT)
        squaren_2.next_to(squaren_1,DOWN)
        squaren_3.next_to(squaren_2,DOWN)
        squaren_4.next_to(squaren_1,RIGHT)
        squaren_5.next_to(squaren_2,RIGHT)
        squaren_6.next_to(squaren_3,RIGHT)

        self.play(TransformFromCopy(text13[0],square1_1,run_time=0.25))
        self.play(TransformFromCopy(text13[3],square2_1,run_time=0.25))
        self.play(TransformFromCopy(square2_1,square2_2,run_time=0.25))
        self.play(TransformFromCopy(text13[6],square3_1,run_time=0.25))
        self.play(TransformFromCopy(square3_1,square3_2,run_time=0.25))
        self.play(TransformFromCopy(square3_2,square3_3,run_time=0.25))
        self.play(TransformFromCopy(text13[9],square4_1,run_time=0.25))
        self.play(TransformFromCopy(square4_1,square4_2,run_time=0.25))
        self.play(TransformFromCopy(square4_2,square4_3,run_time=0.25))
        self.play(TransformFromCopy(square4_3,square4_4,run_time=0.25))
        self.play(TransformFromCopy(text13[12],square5_1,run_time=0.25))
        self.play(TransformFromCopy(square5_1,square5_2,run_time=0.25))
        self.play(TransformFromCopy(square5_2,square5_3,run_time=0.25))
        self.play(TransformFromCopy(square5_3,square5_4,run_time=0.25))
        self.play(TransformFromCopy(square5_4,square5_5,run_time=0.25))
        self.play(TransformFromCopy(text13[17],squaren_1,run_time=0.25))
        self.play(TransformFromCopy(squaren_1,squaren_2,run_time=0.25))
        self.play(TransformFromCopy(squaren_2,squaren_3,run_time=0.25))
        self.play(TransformFromCopy(squaren_3,squaren_4,run_time=0.25))
        self.play(TransformFromCopy(squaren_4,squaren_5,run_time=0.25))
        self.play(TransformFromCopy(squaren_5,squaren_6,run_time=0.25))

        self.play(Write(text14),run_time=2)
        self.wait()

        #SCENE4:
        group4=VGroup(text13,text14,square1_1,square2_1,square2_2,square3_1,square3_2,square3_3,square4_1,square4_2,square4_3,square4_4,square5_1,square5_2,square5_3,square5_4,square5_5,squaren_1,squaren_2,squaren_3,squaren_4,squaren_5,squaren_6)
        self.play(FadeOutFromRandom(group4))

        text15=TextMobject("接下来需要一点小技巧")
        text16=TextMobject("切割")
        text17=Text("如果这个正方形的边长是偶数，那么我们就从中间切开它",font="仿宋",color=RED,stroke_width=0.5)
        text18=Text("举个栗子",font="楷体",stroke_width=0.8)

        text16.scale(2.5)
        text17.scale(0.5)

        text15.set_color([RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE])
        text16.set_color([BLUE,PINK])
        self.wait()
        text18.set_color([RED,ORANGE])

        self.play(Write(text15))
        self.wait()
        self.play(text15.move_to,2*UP)
        self.play(GrowFromCenter(text16))
        self.play(FadeOutFromRandom(text15),FadeOutFromRandom(text16))
        self.play(GrowFromCenter(text17))
        self.play(text17.move_to,2*UP)
        self.play(Write(text18),run_time=1.5)
        self.wait()
        self.play(FadeOutFromRandom(text17),FadeOutFromRandom(text18))

        #SCENE5:
        squaree=Square(side_length=1)
        l1=Line(start=3*UP,end=3*DOWN)
        rec1_1=Rectangle(height=1,width=0.5)
        rec1_2=Rectangle(height=1,width=0.5)
        rec2_1=Rectangle(height=2,width=1)
        rec2_2=Rectangle(height=2,width=1)
        rec3_1=Rectangle(height=3,width=3/2)
        rec3_2=Rectangle(height=3,width=3/2)
        
        decimal = DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=3,
            include_sign=False,
        )

        rec1_1.move_to(0.25*LEFT)
        rec1_2.move_to(0.25*RIGHT)
        rec2_1.move_to(0.5*LEFT)
        rec2_2.move_to(0.5*RIGHT)
        rec3_1.move_to(0.75*LEFT)
        rec3_2.move_to(0.75*RIGHT)
        decimal.next_to(squaree,LEFT)

        squaree.set_color([GREEN,BLUE])
        rec1_1.set_color([GREEN,BLUE])
        rec1_2.set_color([GREEN,BLUE])
        rec2_1.set_color([GREEN,BLUE])
        rec2_2.set_color([GREEN,BLUE])
        rec3_1.set_color([GREEN,BLUE])
        rec3_2.set_color([GREEN,BLUE])
        decimal.set_color([ORANGE,YELLOW])

        decimal.add_updater(lambda d:d.next_to(squaree,LEFT))
        decimal.add_updater(lambda d:d.set_value(2*squaree.get_height()))

        group5=VGroup(rec1_1,rec1_2)
        group6=VGroup(rec2_1,rec2_2)
        group7=VGroup(rec3_1,rec3_2)

        self.play(ShowCreation(squaree))
        self.play(Write(decimal))
        self.play(Write(l1))

        self.play(ReplacementTransform(squaree,group5))
        self.play(rec1_1.move_to,1*LEFT,rec1_2.move_to,1*RIGHT)
        self.play(FadeOutAndShiftDown(group5))

        self.play(squaree.scale,3/2,FadeOutRandom(l1))

        self.play(FadeInRandom(l1),squaree.scale,4/3)
        self.play(ReplacementTransform(squaree,group6))
        self.play(rec2_1.move_to,1.5*LEFT,rec2_2.move_to,1.5*RIGHT)
        self.play(FadeOutAndShiftDown(rec2_1),FadeOutAndShiftDown(rec2_2))

        self.play(FadeOutRandom(l1),squaree.scale,5/4)
        
        self.play(FadeInRandom(l1),squaree.scale,6/5)
        self.play(ReplacementTransform(squaree,group7))
        self.play(rec3_1.move_to,2*LEFT,rec3_2.move_to,2*RIGHT)
        self.play(FadeOutAndShiftDown(rec3_1),FadeOutAndShiftDown(rec3_2))
        self.play(FadeOut(l1),FadeOut(decimal))

        #SCENE6:
        text100=Text("我们来应用一下",font="楷体",stroke_width=0.5)
        self.play(Write(text100))
        self.play(UnWriteRandom(text100))

        square1_1.move_to(np.array([-2.5,2.5,0]))

        square2_1.move_to(np.array([-2.2,2.2,0]))
        square2_2.move_to(np.array([-2.2,2.6,0]))

        square3_1.move_to(np.array([-1.7,1.7,0]))
        square3_2.move_to(np.array([-1.7,2.3,0]))
        square3_3.move_to(np.array([-2.3,1.7,0]))

        square4_1.move_to(np.array([-1,1,0]))
        square4_2.move_to(np.array([-1,1.8,0]))
        square4_3.move_to(np.array([-1,2.6,0]))
        square4_4.move_to(np.array([-1.8,1,0]))

        square5_1.move_to(np.array([-0.1,0.1,0]))
        square5_2.move_to(np.array([-0.1,1.1,0]))
        square5_3.move_to(np.array([-0.1,2.1,0]))
        square5_4.move_to(np.array([-1.1,0.1,0]))
        square5_5.move_to(np.array([-2.1,0.1,0]))

        squaren_1.move_to(np.array([1,-1,0]))
        squaren_2.move_to(np.array([1,0.2,0]))
        squaren_3.move_to(np.array([1,1.4,0]))
        squaren_4.move_to(np.array([1,2.6,0]))
        squaren_5.move_to(np.array([-0.2,-1,0]))
        squaren_6.move_to(np.array([-1.4,-1,0]))


        self.play(ShowCreation(square1_1),run_time=0.25)
        self.play(ShowCreation(square2_1),run_time=0.25)
        self.play(ShowCreation(square2_2),run_time=0.25)
        self.play(ShowCreation(square3_1),run_time=0.25)
        self.play(ShowCreation(square3_2),run_time=0.25)
        self.play(ShowCreation(square3_3),run_time=0.25)
        self.play(ShowCreation(square4_1),run_time=0.25)
        self.play(ShowCreation(square4_2),run_time=0.25)
        self.play(ShowCreation(square4_3),run_time=0.25)
        self.play(ShowCreation(square4_4),run_time=0.25)
        self.play(ShowCreation(square5_1),run_time=0.25)
        self.play(ShowCreation(square5_2),run_time=0.25)
        self.play(ShowCreation(square5_3),run_time=0.25)
        self.play(ShowCreation(square5_4),run_time=0.25)
        self.play(ShowCreation(square5_5),run_time=0.25)
        self.play(ShowCreation(squaren_1),run_time=0.25)
        self.play(ShowCreation(squaren_2),run_time=0.25)
        self.play(ShowCreation(squaren_3),run_time=0.25)
        self.play(ShowCreation(squaren_4),run_time=0.25)
        self.play(ShowCreation(squaren_5),run_time=0.25)
        self.play(ShowCreation(squaren_6),run_time=0.25)

        line1=Line(start=4*LEFT+2.6*UP,end=4*RIGHT+2.6*UP,stroke_width=0.5)

        rect2_1=Rectangle(height=0.2,width=0.4,stroke_width=0.8,fill_color=WHITE,fill_opacity=0.3).move_to(np.array([-2.2,2.5,0]))
        rect2_2=Rectangle(height=0.2,width=0.4,stroke_width=0.8,fill_color=WHITE,fill_opacity=0.3).move_to(np.array([-2.2,2.7,0]))
        rect4_1=Rectangle(height=0.4,width=0.8,stroke_width=0.8,fill_color=WHITE,fill_opacity=0.3).move_to(np.array([-1,2.4,0]))
        rect4_2=Rectangle(height=0.4,width=0.8,stroke_width=0.8,fill_color=WHITE,fill_opacity=0.3).move_to(np.array([-1,2.8,0]))
        rect6_1=Rectangle(height=0.6,width=1.2,stroke_width=0.8,fill_color=WHITE,fill_opacity=0.3).move_to(np.array([1,2.3,0]))
        rect6_2=Rectangle(height=0.6,width=1.2,stroke_width=0.8,fill_color=WHITE,fill_opacity=0.3).move_to(np.array([1,2.9,0]))

        rect2_1.set_color(PINK)
        rect2_2.set_color(PINK)
        rect4_1.set_color(GREEN)
        rect4_2.set_color(GREEN)
        rect6_1.set_color(DARK_BLUE)
        rect6_2.set_color(DARK_BLUE)

        text19=TexMobject("\\ddots")
        text20=TexMobject("\\vdots")
        text21=TexMobject("\\cdots")

        text19.add_updater(lambda d:d.next_to(squaren_1,DR))
        text20.add_updater(lambda d:d.next_to(squaren_5,DOWN))
        text21.add_updater(lambda d:d.next_to(squaren_3,RIGHT))

        groupr1=VGroup(rect2_1,rect2_2)
        groupr2=VGroup(rect4_1,rect4_2)
        groupr3=VGroup(rect6_1,rect6_2)

        self.play(DrawBorderThenFill(line1))
        self.play(FadeOut(line1),ReplacementTransform(square2_2,groupr1),ReplacementTransform(square4_3,groupr2),ReplacementTransform(squaren_4,groupr3))

        self.play(rect2_2.rotate,PI/2)
        self.play(rect2_2.move_to,np.array([-2.5,2.2,0]))
        self.play(rect4_2.rotate,PI/2)
        self.play(rect4_2.move_to,np.array([-2.4,1,0]))
        self.play(rect6_2.rotate,PI/2)
        self.play(rect6_2.move_to,np.array([-2.3,-1,0]))

        groupd1=VGroup(text19,text20,text21)
        groups1=VGroup(square1_1)
        groups2=VGroup(square2_1,)
        groups3=VGroup(square3_1,square3_2,square3_3)
        groups4=VGroup(square4_1,square4_2,square4_4)
        groups5=VGroup(square5_1,square5_2,square5_3,square5_4,square5_5)
        groups6=VGroup(squaren_1,squaren_2,squaren_3,squaren_5,squaren_6)
        groupa1=VGroup(groups1,groups2,groups3,groups4,groups5,groups6,groupr1,groupr2,groupr3,groupd1)

        self.play(Write(groupd1))
        self.play(groupa1.scale,1.2)
        self.play(groupa1.move_to,1*DOWN)

        #</正片>

        #<结束>:
        br=Brace(groupa1,direction=UP,width_multiplier=4.2)
        text22=Text("√",font="宋体")
        text23=Text("Q . E . D",font="Monaco")
        text24=TexMobject("\\sum","^{n}","_{i=1}","{i^3}","=","(","\\sum","^{n}","_{i=1}","{i}",")","^2",stroke_width=0.5)

        text24.set_color_by_tex("^{n}",GOLD)
        text24.set_color_by_tex("\\sum",DARK_BLUE)
        text24.set_color_by_tex("{i=1}",YELLOW)
        text24.set_color_by_tex("(",RED)
        text24.set_color_by_tex(")",RED)

        text3.scale(0.5)
        text23.scale(2)
        text23.move_to(3*DOWN)
        br.add_updater(lambda d:d.next_to(groupa1,UP))
        text5.move_to(3.5*UP)

        text22.next_to(text24,RIGHT)
        text22.set_color([RED,PINK])
        text22.scale(2)

        self.play(Write(br),Write(text5))
        self.play(FadeOutRandom(groupa1),FadeOutRandom(br))
        self.play(text5.move_to,0*DOWN)
        self.wait()
        self.play(ReplacementTransform(text5,text24))
        self.wait()
        self.play(Write(text22),run_time=2)
        self.wait()
        """
        """
        #</结尾>

#这应该是最水的代码了。。
