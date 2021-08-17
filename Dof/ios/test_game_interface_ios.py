from time import sleep

import wda

'''
执行该类需一起执行，
请清除手机app数据

'''


class TestGameInterface:

    def setup_class(self):
        self.d = wda.USBClient()
        self.d.session().app_start('puzzle.game.find.differences')
        sleep(10)

        # 跳过第一关教程
        self.d.click(0.602, 0.177)
        sleep(1.5)
        self.d.click(0.34, 0.24)
        sleep(1.5)
        self.d.click(0.266, 0.164)
        sleep(0.5)
        self.d.click(0.446, 0.39)
        sleep(0.5)
        self.d.click(0.682, 0.308)
        sleep(3)

    def teardown_class(self):
        self.d.app_stop('puzzle.game.find.differences')

    # 结束游戏功能
    def test_quit_game(self):
        self.d.click(0.508, 0.719)
        sleep(3)
        self.d.click(0.51, 0.683)
        sleep(2)
        self.d.click(0.086, 0.023)
        sleep(2)
        self.d.click(0.496, 0.588)
        sleep(4)

    # 游戏失败->结束游戏
    def test_game_fail_quit(self):
        self.d.click(0.494, 0.688)
        sleep(2)

        # 连续5次点击错误
        for i in range(0, 5):
            sleep(0.5)
            self.d.click(0.912, 0.292)
        sleep(1.5)
        self.d.click(0.292, 0.594)
        sleep(4)

    # 测试有金币的时候使用放大镜功能
    def test_hint_have_coin(self):
        self.d.click(0.514, 0.703)
        sleep(3)
        self.d.click(0.504, 0.853)
        sleep(2)
        self.d.click(0.502, 0.358)
        sleep(2)
        self.d.click(0.746, 0.325)
        sleep(0.5)
        self.d.click(0.448, 0.155)
        sleep(0.2)
        self.d.click(0.132, 0.155)
        sleep(0.2)
        self.d.click(0.274, 0.404)
        sleep(3)

    # 测试没有金币时候使用放大镜功能
    def test_hint_no_coin(self):
        sleep(1)
        self.d.click(0.5, 0.718)
        sleep(2)
        self.d.click(0.5, 0.851)

        # 点击关闭广告
        # self.d.xpath('//*[@resource-id="close_button_icon"]').wait(timeout=90).click()
        sleep(50)

        # 关闭广告
        self.d.click(0.938, 0.036)
        sleep(3)
        # 放大镜使用成功，自动出现目标框并点击
        self.d.click(0.542, 0.391)
        sleep(5)

    # 游戏失败->继续游戏
    def test_game_fail_continue(self):
        # 连续5次点击错误
        for i in range(0, 5):
            sleep(0.5)
            self.d.click(0.926, 0.244)
        sleep(2)
        self.d.click(0.718, 0.593)
        sleep(50)
        # 点击关闭
        self.d.click(0.932, 0.041)
        sleep(2)
