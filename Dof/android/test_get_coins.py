from time import sleep

import uiautomator2 as u2


class TestGetCoins:

    def setup_class(self):
        self.d = u2.connect("127.0.0.1:7555")
        self.d.app_start("puzzle.game.find.differences")
        sleep(15)

        # 跳过第一关教程
        self.d.click(0.602, 0.177)
        sleep(1)
        self.d.click(0.34, 0.24)
        sleep(0.5)
        self.d.click(0.266, 0.164)
        sleep(0.5)
        self.d.click(0.446, 0.39)
        sleep(0.5)
        self.d.click(0.682, 0.308)
        sleep(3)

        # 返回主页
        self.d.click(0.504, 0.833)
        sleep(2)

        # 打开Cheat
        self.d.click(0.216, 0.951)
        sleep(1)

        # 点击Cheat
        self.d.click(0.316, 0.552)
        sleep(1)
        # 主线关卡跳转到第10关
        self.d.send_keys("10", clear=True)
        sleep(1)
        # 点击确定
        self.d.click(0.958, 0.914)
        sleep(1)
        # 应用设置
        self.d.click(0.498, 0.554)
        sleep(0.5)
        # 设置中恢复用户数据
        self.d.click(0.892, 0.058)
        sleep(1)
        self.d.click(0.708, 0.655)
        sleep(2)
        # 关闭设置
        self.d.click(0.814, 0.237)
        sleep(1)

    def teardown_class(self):
        self.d.app_stop('puzzle.game.find.differences')

    def test_get_coins_from_chests(self):
        # 第十关通关后，会有赠送金币宝箱

        # 进入第十关
        self.d.click(0.512, 0.688)
        sleep(3)
        # 通关
        self.d.click(0.294, 0.243)
        sleep(0.5)
        self.d.click(0.58, 0.186)
        sleep(0.5)
        self.d.click(0.804, 0.192)
        sleep(0.5)
        self.d.click(0.496, 0.271)
        sleep(0.5)
        self.d.click(0.54, 0.354)
        sleep(6)

        # 点击继续将获得等额金币
        self.d.click(0.504, 0.77)
        sleep(4)
        # 返回主页查看金币数值
        self.d.click(0.502, 0.834)
        sleep(3)

    def test_use_coin(self):
        # 进入关卡
        self.d.click(0.508, 0.689)
        sleep(3)
        # 使用放大镜
        self.d.click(0.508, 0.852)
        sleep(3)
        # 点击提示的不同点
        self.d.click(0.516, 0.632)
        sleep(0.5)

        # 游戏失败，使用金币继续
        for i in range(0, 5):

            self.d.click(0.912, 0.292)
            sleep(0.5)
        # 点击继续
        sleep(1.5)
        self.d.click(0.726, 0.594)
        sleep(3)





