import cairo
import math

PIC_SIZE=512
class Fractal:

    def __init__(self,n,stroke,deg):
        self.stroke=stroke
        self.n=n
        self.deg=deg
        self.verts=[]

    def draw_line(self,ctx):
        ctx.set_line_width(math.log2(self.stroke)*2)
        l=[]
        N=100
        for x,y in self.verts:
            ctx.set_source_rgb(0, 1, 0)
            ctx.move_to(x,y)
            xx,yy= x-100*math.sin(-195*self.n),y+100*math.cos(-195*self.n)
            ctx.line_to(xx,yy)
            l.append((xx,yy))
            ctx.stroke()

            ctx.set_source_rgb(1, 0, 0)
            ctx.move_to(x,y)
            xx,yy= x+100*math.sin(-195*self.n),y+100*math.cos(-195*self.n)
            ctx.line_to(xx,yy)
            l.append((xx,yy))
            ctx.stroke()

        self.verts.clear()
        self.verts=list(set(l))

        ctx.stroke()

    def draw(self):
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, PIC_SIZE*4, PIC_SIZE*4)
        ctx = cairo.Context(surface)
        ctx.set_source_rgb(1, 1, 1)
        ctx.paint()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.move_to(PIC_SIZE*2,PIC_SIZE*2)
        ctx.line_to(PIC_SIZE*2,PIC_SIZE*2+200)
        self.verts=[(PIC_SIZE*2,PIC_SIZE*2+200)]

        while self.stroke!=0:
            self.draw_line(ctx)
            self.stroke//=2
            self.n+=1

        surface.write_to_png("out.png")

f=Fractal(0,2**10,10)
f.draw()
