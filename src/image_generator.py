from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import subprocess


def get_fortune():
    fortune_out = subprocess.Popen(['/usr/games/fortune'],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    f_stdout, f_stderr = fortune_out.communicate()
    fortune = f_stdout.decode('utf-8')
    return fortune


def process_message(
        drawing: ImageDraw,
        message_text: str,
        font: ImageFont,
        line_spacing: int,
        max_width: int,
        max_lines: int):
    message_text = message_text.replace('\r\n', ' ')
    message_text = message_text.replace('\n', ' ')
    message_text = message_text.replace('  ', ' ')
    number_of_lines = 1
    lw, lh = drawing.multiline_textsize(text=message_text, font=font, spacing=line_spacing)

    if lw > max_width:
        message_words = message_text.split()
        message_text = ''
        has_more_text = True
        while has_more_text:
            for i in range(0 , len(message_words)):
                line = ' '.join(message_words[0:i + 1])
                lw, lh = drawing.multiline_textsize(text=line, font=font, spacing=line_spacing)
                if lw > max_width:
                    line = ' '.join(message_words[:i - 1])
                    message_text += f'{line}\n'
                    number_of_lines += 1
                    if number_of_lines > max_lines:
                        has_more_text = False
                        message_text = f'{message_text[:len(message_text) - 3]}...'
                        break
                    message_words = message_words[i - 1:]
                    line = ' '.join(message_words)
                    lw, lh = drawing.multiline_textsize(text=line, font=font, spacing=line_spacing)
                    if lw <= max_width:
                        has_more_text = False
                        message_text += f'{line}'
                        break
                    break

    lw, lh = drawing.multiline_textsize(text=message_text, font=font, spacing=line_spacing)
    number_of_lines = message_text.count('\n') + 1
    return message_text, number_of_lines, lw, lh


class ImageGenerator(object):

    def __init__(self):
        self.__temp_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 80)
        self.__cond_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 28)
        self.__cc_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 18)
        self.__alert_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 70)
        pass

    def draw_black_image(self, **kwargs) -> str:
        icon_path = kwargs.get('icon_path')
        temperature = kwargs.get('temperature')
        curr_conds = kwargs.get('curr_conds')
        feels_like = kwargs.get('feels_like')
        rel_hum = kwargs.get('rel_hum')
        pressure = kwargs.get('pressure')
        wind_speed = kwargs.get('wind_speed')
        wind_dir = kwargs.get('wind_dir')
        sunrise = kwargs.get('sunrise')
        sunset = kwargs.get('sunset')
        updated = kwargs.get('updated')
        message = kwargs.get('message', '')
        save_path = kwargs.get('save_path')

        # create an image
        img = Image.new(mode='L', size=(630, 374), color=255)

        png = Image.open(icon_path)

        img.paste(png, (20, 15), png)

        # get a drawing context
        d = ImageDraw.Draw(img)

        # draw lines
        d.line(xy=[(240, 0), (240, 300)], fill=0, width=5)
        d.line(xy=[(0, 300), (640, 300)], fill=0, width=5)

        # draw multiline text
        w, h = d.textsize(temperature, font=self.__temp_fnt)
        x_coord = (215 - w) / 2
        d.multiline_text((x_coord, 190), f'{temperature}°', font=self.__temp_fnt)
        d.multiline_text((260, 12), 'Current Conditions:', font=self.__cc_fnt)
        d.multiline_text((260, 32), curr_conds, font=self.__cond_fnt)
        d.multiline_text((260, 80), f'Feels Like: {feels_like}°', font=self.__cc_fnt)
        d.multiline_text((260, 102), f'Relative Humidity: {rel_hum}%', font=self.__cc_fnt)
        d.multiline_text((260, 124), f'Barometric Pressure: {pressure} inches', font=self.__cc_fnt)
        d.multiline_text((260, 146), f'Wind Speed: {wind_speed} mph', font=self.__cc_fnt)
        d.multiline_text((260, 168), f'Wind Direction: {wind_dir}', font=self.__cc_fnt)
        d.multiline_text((260, 204), f'Sunrise: {sunrise}', font=self.__cc_fnt)
        d.multiline_text((260, 226), f'Sunset: {sunset}', font=self.__cc_fnt)
        d.multiline_text((260, 262), f'Updated at: {updated}', font=self.__cc_fnt)

        # bottom message
        if len(message) > 0:
            msg, lines, width, height = process_message(drawing=d, message_text=message, font=self.__cc_fnt, line_spacing=3,
                                                        max_width=616, max_lines=3)
            x_coord = (630 - width) / 2
            y_coord = (74 - height) / 2 + 298
            d.multiline_text(xy=(x_coord, y_coord), text=msg, font=self.__cc_fnt, spacing=3)

        # add the border
        with_border = ImageOps.expand(image=img, border=5, fill='black')

        # save it out
        saved_file = os.path.join(save_path, 'img_black.bmp')
        with_border.save(fp=saved_file)
        return saved_file


    def draw_red_image(self, **kwargs) -> str:
        message = kwargs.get('message', '')
        save_path = kwargs.get('save_path')

        # create an image
        img = Image.new(mode='L', size=(640, 384), color=255)

        # get a drawing context
        d = ImageDraw.Draw(img)

        # draw the stuff
        if len(message) > 0:
            msg, lines, width, height = process_message(drawing=d, message_text=message, font=self.__cc_fnt, line_spacing=3,
                                                        max_width=390, max_lines=3)
            d.rectangle(xy=[(13, 311), (237, 375)], fill='black')
            d.multiline_text(xy=(18, 293), text='ALERT', font=self.__alert_fnt, fill='white')
            x_coord = (400 - width) / 2 + 242
            y_coord = (84 - height) / 2 + 298
            d.multiline_text(xy=(x_coord, y_coord), text=msg, font=self.__cc_fnt, spacing=3, fill='black')

        # save it out
        saved_file = os.path.join(save_path, 'img_red.bmp')
        img.save(fp=saved_file)
        return saved_file
