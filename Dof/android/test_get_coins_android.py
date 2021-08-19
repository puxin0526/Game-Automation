from time import sleep

import uiautomator2 as u2

'''
执行该case条件：需要启动游戏打开cheat
将游戏返回到主界面

'''


class TestGetCoins:

    def setup_class(self):
        self.d = u2.connect()
        self.d.app_start("puzzle.game.find.differences")
        sleep(2)

        # 打开Cheat
        self.d.click(0.205, 0.955)
        sleep(1)

        # 点击主线关卡
        self.d.click(0.321, 0.551)
        sleep(1)
        # 主线关卡跳转到第10关
        self.d.send_keys("10", clear=True)
        sleep(1)
        # 点击确定
        self.d.xpath('//*[@text="确定"]').click()
        sleep(1)
        # 应用设置
        self.d.click(0.501, 0.553)
        sleep(0.5)
        # 设置中恢复用户数据
        self.d.click(0.888, 0.064)
        sleep(1)
        self.d.click(0.707, 0.657)
        sleep(2)
        # 关闭设置
        self.d.click(0.812, 0.235)
        sleep(1)

    def teardown_class(self):
        self.d.app_stop('puzzle.game.find.differences')

    def test_get_coins_from_chests(self):
        # 第十关通关后，会有赠送金币宝箱

        # 进入第十关
        self.d.click(0.512, 0.688)
        sleep(3)
        # 通关
        self.d.click(0.281, 0.288)
        sleep(0.5)
        self.d.click(0.498, 0.316)
        sleep(0.5)
        self.d.click(0.541, 0.401)
        sleep(0.5)
        self.d.click(0.584, 0.227)
        sleep(0.5)
        self.d.click(0.819, 0.235)
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
        self.d.click(0.505, 0.941)
        sleep(3)
        # 点击提示的不同点
        self.d.click(0.516, 0.314)
        sleep(0.5)

        # 游戏失败，使用金币继续
        for i in range(0, 5):
            self.d.click(0.88, 0.17)
            sleep(0.5)
        # 点击继续
        sleep(1.5)
        self.d.click(0.726, 0.594)
        sleep(3)
