import os


class BitBar:
    bar = []

    def __make(self, line, color=None, size=None, font=None, onclick=None, terminal=None, href=None):
        send = f'{line} | '
        if color is not None:
            send += f'color={color} '
        if size is not None:
            send += f'size={size} '
        if font is not None:
            send += f'font={font} '
        if terminal is not None:
            send += f"terminal={terminal} "
        if onclick is not None:
            send += f"bash='{self.__AddMacOS(onclick)}' "
        if href is not None and onclick is None:
            send += f'href={href} '
        return send

    def __AddMacOS(self, path):
        if path.find != -1:
            app = os.listdir(f'{path}/Contents/macos/')
            path += f'/Contents/macos/{app[0]}'
        return path

    def BarLine(self, line, color=None, size=None, font=None):
        send = self.__make(line, color=color, size=size, font=font)
        self.bar.append(send)
        self.bar.append('---')

    def newline(self, line, color=None, size=None, font=None, onclick=None, terminal=None, href=None):
        send = self.__make(line, color=color, size=size, font=font, onclick=onclick, terminal=terminal, href=href)
        self.bar.append(send)

    def submenusHead(self, line, color=None, size=None, font=None):
        self.newline(line, color=color, size=size, font=font)

    def submenus(self, line, color=None, size=None, font=None, onclick=None, terminal=None, href=None):
        send = self.__make(line, color=color, size=size, font=font, onclick=onclick, terminal=terminal, href=href)
        self.bar.append('--' + send)

    def show(self):
        for send in self.bar:
            send = str(send)
            print(send)
