import os
import svgwrite

STYLES = """.conditions { font-family: sans-serif; font-size: 18px; font-weight: bold; fill: black; }
.message { font-family: sans-serif; font-size: 18px; font-weight: bold; fill: black; }
.last-updated { font-family: sans-serif; font-size: 12px; font-weight: 900; fill: black; }
.temperature { font-family: sans-serif; font-size: 80px; font-weight: bold; text-transform: uppercase; fill: black; }
"""


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
        # bottom_image = os.path.join(desktop, 'bottom.svg')
        # left_image = os.path.join(desktop, 'left.svg')
        # right_image = os.path.join(desktop, 'right.svg')
        print(main_image)

        # bottom_bar = svgwrite.Drawing(bottom_image, size=(640, 84), x=0, y=0)
        # bottom_bar.viewbox(minx=0, miny=0, width=640, height=84)
        # bottom_bar.add(bottom_bar.text('There are currently no weather alerts for your location.',
        #                                insert=('50%', '50%'),
        #                                stroke='none',
        #                                fill='black',
        #                                font_size='18px',
        #                                font_weight='bold',
        #                                font_family='sans-serif',
        #                                dominant_baseline='middle',
        #                                text_anchor='middle'))
        # bottom_bar.save()
        left_top_g = svgwrite.container.Group()

        bottom_g = svgwrite.container.Group()

        left_top_svg = svgwrite.container.SVG(insert=(0, 0), size=(400, 300))
        # ideally would rather read this SVG as XML and insert it here?
        conditions_image = svgwrite.image.Image(href='C:\\Users\\josep\\source\\repos\\WeatherAppliance\\images\\drop_weather_cloud_rain_forecasticon.svg')
        left_top_svg.add(conditions_image)
        left_top_g.add(left_top_svg)

        right_top_g = svgwrite.container.Group()
        right_top_svg = svgwrite.container.SVG(insert=(400, 0), size=(240, 300))
        # Note that x and y must be sent as lists here because in the W3C spec it's a list and
        # since class is a reserved work, we have to add an underscore behind it
        temperature_text = svgwrite.text.Text('108°', x=['50%'], y=['50%'], dominant_baseline='middle', text_anchor='middle', class_="temperature")
        right_top_svg.add(temperature_text)
        right_top_g.add(right_top_svg)

        rt_top_g = svgwrite.container.Group()
        rt_top_svg = svgwrite.container.SVG(insert=(0, 0), size=(240, 200))
        rt_top_g.add(rt_top_svg)

        rt_bottom_g = svgwrite.container.Group()
        rt_bottom_svg = svgwrite.container.SVG(insert=(0, 180), size=(240, 100))
        rt_bottom_g.add(rt_bottom_svg)

        right_top_svg.add(rt_top_g)
        right_top_svg.add(rt_bottom_g)

        main_drawing = svgwrite.Drawing(main_image, size=(640, 384))
        main_drawing.viewbox(minx=0, miny=0, width=640, height=384)
        main_drawing.add(main_drawing.polyline(points=[(0, 0), (640, 0), (640, 384), (0, 384), (0, 0)], stroke='black',
                                               stroke_width=10, fill='none'))
        main_drawing.add(
            main_drawing.polyline(points=[(0, 300), (640, 300), (640, 0), (400, 0), (400, 300)], stroke='black',
                                  stroke_width=5, fill='none'))
        main_drawing.add(left_top_g)
        main_drawing.add(right_top_g)
        main_drawing.defs.add(main_drawing.style(STYLES))
        main_drawing.save()
