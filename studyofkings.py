from dataclasses import dataclass

import pyxel


@dataclass
class Size:
    w: int
    h: int


@dataclass
class Pos:
    x: int
    y: int


class App:
    SQ_SIZE = 32
    SCROLL_X = 5
    SCROLL_Y = 4
    def __init__(self):
        self.scr_size = Size(w=24, h=16)  # 画面サイズ (マス数)
        self.map_size = Size(w=57, h=24)  # マップサイズ (マス数)
        self.dsp_pos = Pos(x=25, y=4)  # 画面表示位置 (左上、マスインデクス)
        self.cur_pos = Pos(x=37, y=9)  # カーソル表示位置 (マスインデクス)
        pyxel.init(self.scr_size.w * App.SQ_SIZE, self.scr_size.h * App.SQ_SIZE, title="Study of Kings", quit_key=pyxel.KEY_ESCAPE, display_scale=2)
        pyxel.load("assets/studyofkings.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_LEFT):
            self.cur_pos.x = max(self.cur_pos.x - 1, 1)
            if self.cur_pos.x == self.dsp_pos.x:
                self.dsp_pos.x = max(self.dsp_pos.x - App.SCROLL_X, 0)
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.cur_pos.x = min(self.cur_pos.x + 1, 55)
            if self.cur_pos.x == self.dsp_pos.x + self.scr_size.w - 1:
                self.dsp_pos.x = min(self.dsp_pos.x + App.SCROLL_X, 57 - self.scr_size.w)
        elif pyxel.btnp(pyxel.KEY_UP):
            self.cur_pos.y = max(self.cur_pos.y - 1, 1)
            if self.cur_pos.y == self.dsp_pos.y:
                self.dsp_pos.y = max(self.dsp_pos.y - App.SCROLL_Y, 0)
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.cur_pos.y = min(self.cur_pos.y + 1, 22)
            if self.cur_pos.y == self.dsp_pos.y + self.scr_size.h - 1:
                self.dsp_pos.y = min(self.dsp_pos.y + App.SCROLL_Y, 24 - self.scr_size.h)

    def draw(self):
        cx = self.cur_pos.x - self.dsp_pos.x
        cy = self.cur_pos.y - self.dsp_pos.y
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, self.dsp_pos.x * App.SQ_SIZE, self.dsp_pos.y * App.SQ_SIZE, self.scr_size.w * App.SQ_SIZE, self.scr_size.h * App.SQ_SIZE)
        pyxel.blt(cx * 32, cy * 32 + 8, 0, 16, 0, 16, 16, 15)


if __name__ == "__main__":
    App()
