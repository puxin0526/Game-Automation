import uiautomator2 as u2
from time import sleep

'''
case主要检查图片的缩放功能
执行case条件：
已经跳过新手教程，界面处于主界面且即将进入第2关卡

'''


class TestZoom:
    def setup_class(self):
        self.d = u2.connect()
        self.d.app_start("puzzle.game.find.differences")

        # 进入到关卡2游戏内
        self.d.click(0.505, 0.687)
        sleep(2)

    def test_zoom_in(self):
        # 测试放大功能
        self.d().pinch_out()
        sleep(0.5)
        # 点击图中的不同点
        self.d.click(0.513, 0.33)
        sleep(0.5)

    def test_zoom_out(self):
        # 测试缩小功能
        self.d().pinch_in()
        sleep(0.5)
        # 点击图中的不同点
        self.d.click(0.765, 0.391)
        sleep(1)
