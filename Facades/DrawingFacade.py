import os
import svgwrite


class DrawingFacade(object):

    def __init__(self, config):
        self._image_width = config['imageParams']['width']
        self._image_height = config['imageParams']['height']
        self._image_profile = config['imageParams']['profile']

    def draw_black_layer(self):
        pass

    def draw_red_layer(self):
        pass

    def get_main_drawing_container(self, image_path):
        main_drawing = svgwrite.Drawing(image_path, size=(self._image_width, self._image_height), profile=self._image_profile)
        main_drawing.viewbox(minx=0, miny=0, width=self._image_width, height=self._image_height)
        return main_drawing

    def draw_sample_svg(self):
        if os.name == 'nt':
            home_dir = os.environ['USERPROFILE']
        else:
            home_dir = "/mnt/c/Users/josep"
        desktop = os.path.join(os.path.join(home_dir), 'Desktop')

        main_image = os.path.join(desktop, 'test.svg')
        bottom_image = os.path.join(desktop, 'bottom.svg')
        left_image = os.path.join(desktop, 'left.svg')
        right_image = os.path.join(desktop, 'right.svg')
        print(main_image)

        bottom_bar = svgwrite.Drawing(bottom_image, size=(640, 84), x=0, y=0)
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

        main_drawing = svgwrite.Drawing(main_image, size=(640, 384), profile="tiny")
        main_drawing.viewbox(minx=0, miny=0, width=640, height=384)
        main_drawing.add(main_drawing.polyline(points=[(0, 0), (640, 0), (640, 384), (0, 384), (0, 0)], stroke='black',
                                               stroke_width=10, fill='none'))
        main_drawing.add(
            main_drawing.polyline(points=[(0, 300), (640, 300), (640, 0), (400, 0), (400, 300)], stroke='black',
                                  stroke_width=5, fill='none'))
        main_drawing.add(main_drawing.image(bottom_image, insert=(0, 300)))
        main_drawing.save()
