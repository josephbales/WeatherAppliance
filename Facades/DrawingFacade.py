import os
import svgwrite as draw


class DrawingFacade:

    def draw_sample_svg(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + os.path.sep
        main_image = desktop + 'test.svg'
        bottom_image = desktop + 'bottom.svg'
        left_image = desktop + 'left.svg'
        right_image = desktop + 'right.svg'
        print(main_image)

        bottom_bar = draw.Drawing(bottom_image, size=(640, 84), x=0, y=0)
        bottom_bar.viewbox(minx=0, miny=0, width=640, height=84)
        bottom_bar.add(bottom_bar.text('There are currently no weather alerts for your location.',
                                       insert=('50%', '50%'),
                                       stroke='none',
                                       fill='black',
                                       font_size='18px',
                                       font_weight='bold',
                                       font_family='sans-serif',
                                       dominant_baseline='middle',
                                       text_anchor='middle'))
        bottom_bar.save()

        main_drawing = draw.Drawing(main_image, size=(640, 384), profile="tiny")
        main_drawing.viewbox(minx=0, miny=0, width=640, height=384)
        main_drawing.add(main_drawing.polyline(points=[(0, 0), (640, 0), (640, 384), (0, 384), (0, 0)], stroke='black',
                                               stroke_width=10, fill='none'))
        main_drawing.add(
            main_drawing.polyline(points=[(0, 300), (640, 300), (640, 0), (400, 0), (400, 300)], stroke='black',
                                  stroke_width=5, fill='none'))
        main_drawing.add(main_drawing.image(bottom_image, insert=(0, 300)))
        main_drawing.save()
