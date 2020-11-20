import cairo
import math

PIC_SIZE=512
class Fractal:

    def __init__(self,n,stroke,deg):
        self.stroke=stroke
        self.n=n
        self.deg=deg
        self.verts=[]
    def rotate_point(self,ox,oy,x,y):
        pxx = math.cos(self.deg*self.n) * (x-ox) - math.sin(self.deg*self.n) * (y-oy) + ox
        pyy = math.sin(self.deg*self.n) * (x-ox) + math.cos(self.deg*self.n) * (y-oy) + oy
        return (pxx,pyy);

    def draw_line(self,ctx):
        ctx.set_line_width(math.log2(self.stroke)*2)
        l=[]
        N=100-math.log2(self.stroke)*0.5
        for x,y in self.verts:
            ctx.move_to(x,y)
            xx= x-N*math.sin(self.deg*self.n)
            yy= y+N*math.cos(self.deg*self.n)
            ctx.line_to(xx,yy)
            l.append((xx,yy))
            
            ctx.move_to(x,y)
            xx= x+N*math.sin(self.deg*self.n)
            yy= y+N*math.cos(self.deg*self.n)
            ctx.line_to(xx,yy)
            l.append((xx,yy))

        self.verts.clear()
        self.verts=list(set(l))

        ctx.stroke()

    def draw(self):
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, PIC_SIZE*2, PIC_SIZE*2)
        ctx = cairo.Context(surface)
        ctx.set_source_rgb(1, 1, 1)
        ctx.paint()
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        self.verts=[(PIC_SIZE,0)]
        while self.stroke!=0:
            self.draw_line(ctx)
            self.stroke//=2
            self.n+=1

        surface.write_to_png("out.png")

f=Fractal(0,2**9,25)
f.draw()
