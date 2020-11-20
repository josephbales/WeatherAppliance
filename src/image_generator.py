import base64
import os
import subprocess
import svgwrite

# For alert messages
# Bottom message should be no more than 60 characters total. If larger than 60 characters
# then take 56 characters and append " ..."

STYLES = """.conditions { font-family: sans-serif; font-size: 18px; font-weight: bold; fill: black; }
.message { font-family: monospace; font-size: 18px; font-weight: bold; fill: black; }
.last-updated { font-family: sans-serif; font-size: 12px; font-weight: 900; fill: black; }
.temperature { font-family: sans-serif; font-size: 80px; font-weight: bold; text-transform: uppercase; fill: black; }"""


class ImageGenerator(object):

    def __init__(self, config):
        self.__img_width = int(config['imageParams']['width'])
        self.__img_height = int(config['imageParams']['height'])
        self.__img_profile = config['imageParams']['profile']

    def draw_black_layer(self):
        pass

    def draw_red_layer(self):
        pass

    def get_main_drawing_container(self, image_path):
        main_drawing = svgwrite.Drawing(image_path, size=(self.__img_width, self.__img_height), profile=self.__img_profile)
        main_drawing.viewbox(minx=0, miny=0, width=self.__img_width, height=self.__img_height)
        return main_drawing

    def draw_sample_svg(self, image_path):
        desktop = '/home/jbales/dev/test_images'

        main_image_svg = os.path.join(desktop, 'test.svg')
        print(main_image_svg)

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

        left_top_width = int(self.__img_width * 0.375)
        right_top_width = self.__img_width - left_top_width

        top_height = int(self.__img_height * 0.78125)
        bottom_height = self.__img_height - top_height

        main_drawing = svgwrite.Drawing(main_image_svg, size=(self.__img_width, self.__img_height))
        main_drawing.add(svgwrite.shapes.Rect(insert=(0, 0), size=(self.__img_width, self.__img_height), stroke='black', stroke_width=10, fill='none'))

        top_left_g = main_drawing.g() # Can we method chain these and be less verbose?
        top_right_g = main_drawing.g()
        bottom_g = main_drawing.g()

        main_drawing.add(top_left_g)
        main_drawing.add(top_right_g)
        main_drawing.add(bottom_g)

        top_left_svg = svgwrite.container.SVG(insert=(0, 0), size=(left_top_width, top_height))
        top_right_svg = svgwrite.container.SVG(insert=(left_top_width, 0), size=(right_top_width, top_height))
        bottom_svg = svgwrite.container.SVG(insert=(0, top_height), size=(self.__img_width, bottom_height))

        top_left_g.add(top_left_svg)
        top_right_g.add(top_right_svg)
        bottom_g.add(bottom_svg)

        # Left Panel Stuff
        top_left_svg.add(svgwrite.shapes.Line(start=(0, top_height), end=(left_top_width, top_height), stroke='black', stroke_width=5))
        top_left_svg.add(svgwrite.shapes.Line(start=(left_top_width, 0), end=(left_top_width, top_height), stroke='black', stroke_width=5))
        temperature_text = svgwrite.text.Text('108°', x=['50%'], y=['50%'], dominant_baseline='middle',
                                              text_anchor='middle', class_="temperature", font_size='80px')
        top_left_svg.add(temperature_text);
        base64_weather_icon = base64.b64encode(open(image_path, 'rb').read())
        conditions_image = svgwrite.image.Image(href=f"data:image/png;base64,{base64_weather_icon.decode('utf-8')}")
        top_left_svg.add(conditions_image);

        # Right Panel Stuff
        top_right_svg.add(svgwrite.shapes.Line(start=(0, top_height), end=(right_top_width, top_height), stroke='black', stroke_width=5))
        top_right_svg.add(svgwrite.shapes.Line(start=(0, 0), end=(0, top_height), stroke='black', stroke_width=5))

        # Bottom Panel Stuff
        fortune_out = subprocess.Popen(['/usr/games/fortune'],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        f_stdout, f_stderr = fortune_out.communicate()
        fortune = f_stdout.decode('utf-8')
        fortune = fortune.replace('\n', '')
        fortune = fortune.replace('\t', ' ')
        fortune = fortune.replace('  ', ' ')
        print(f_stdout)
        print(fortune)
        print(f_stderr)
        bottom_svg.add(svgwrite.shapes.Line(start=(0, 0), end=(self.__img_width, 0), stroke='black', stroke_width=5))
        bottom_svg.add(svgwrite.text.Text(fortune, x=['50%'], y=['50%'], dominant_baseline='middle',
                                              text_anchor='middle', class_='message'))


        # left_top_svg = svgwrite.container.SVG(insert=(0, 0), size=(400, 300))
        #
        # base64_weather_icon = base64.b64encode(open(image_path, 'rb').read())
        #
        # conditions_image = svgwrite.image.Image(href=f"data:image/png;base64,{base64_weather_icon.decode('utf-8')}")
        # left_top_svg.add(conditions_image)
        # left_top_g.add(left_top_svg)
        #
        # right_top_g = svgwrite.container.Group()
        # right_top_svg = svgwrite.container.SVG(insert=(400, 0), size=(240, 300))
        # # Note that x and y must be sent as lists here because in the W3C spec it's a list and
        # # since class is a reserved word, we have to add an underscore behind it
        # temperature_text = svgwrite.text.Text('108°', x=['50%'], y=['50%'], dominant_baseline='middle', text_anchor='middle', class_="temperature")
        # right_top_svg.add(temperature_text)
        # right_top_g.add(right_top_svg)
        #
        # rt_top_g = svgwrite.container.Group()
        # rt_top_svg = svgwrite.container.SVG(insert=(0, 0), size=(240, 200))
        # # rt_top_svg.add(svgwrite.shapes.Rect(insert=(0, 0), size=(240, 200), stroke='green', stroke_width=20, fill='none'))
        # rt_top_g.add(rt_top_svg)
        #
        # rt_bottom_g = svgwrite.container.Group()
        # rt_bottom_svg = svgwrite.container.SVG(insert=(0, 180), size=(240, 100))
        # rt_bottom_g.add(rt_bottom_svg)
        #
        # right_top_svg.add(rt_top_g)
        # right_top_svg.add(rt_bottom_g)

        main_drawing.viewbox(minx=0, miny=0, width=self.__img_width, height=self.__img_height)
        # main_drawing.add(main_drawing.polyline(points=[(0, 0), (self.__img_width, 0), (self.__img_width, self.__img_height), (0, self.__img_height), (0, 0)], stroke='black',
        #                                        stroke_width=10, fill='none'))

        bottom_line_height = int(self.__img_height * 0.78125)
        side_line_width = int(self.__img_width * 0.625)

        # main_drawing.add(
        #     main_drawing.polyline(points=[(0, bottom_line_height), (self.__img_width, bottom_line_height), (self.__img_width, 0), (side_line_width, 0), (side_line_width, bottom_line_height)], stroke='black',
        #                           stroke_width=5, fill='none'))

        main_drawing.defs.add(main_drawing.style(STYLES))
        main_drawing.save()

        main_image_png = os.path.join(desktop, 'test.png')

        imagemagick_out = subprocess.Popen(['/usr/bin/convert', main_image_svg, main_image_png],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
        im_stdout, im_stderr = imagemagick_out.communicate()
        print(im_stdout)
        print(im_stderr)

