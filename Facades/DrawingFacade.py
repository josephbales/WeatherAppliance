import os
import svgwrite as draw


class DrawingFacade:

    def draw_sample_svg(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        desktop += os.path.sep + 'test.svg'
        print(desktop)

        dwg = draw.Drawing(desktop)
        dwg.add(dwg.line((0, 0), (100, 100), stroke=draw.rgb(10, 10, 16, '%')))
        dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))

        dwg.save()
