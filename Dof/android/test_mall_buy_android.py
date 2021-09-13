import uiautomator2 as u2
from time import sleep

'''
case执行条件：已跳过新手教程
已添加谷歌账号为内购账号

'''


class TestMallBuy:

    def setup_class(self):
        self.d = u2.connect()
        self.d.settings["wait_timeout"] = 10
        self.d.app_start("puzzle.game.find.differences")
        sleep(3)

    def test_buy_seccess(self):
        # 点击主界面的+图标，进入商城购买界面
        self.d.click(0.321, 0.06)
        sleep(1)
        # 充值100金币
        self.d.click(0.217, 0.33)
        self.d.xpath('//*[@text="一键购买"]').click()
        sleep(5)
        # 点击x图标，返回到主界面
        self.d.click(0.942, 0.075)
        sleep(1)

        # 进入到游戏内
        self.d.click(0.505, 0.687)
        sleep(2)
        # 点击游戏内+图标，进入商城购买界面
        self.d.click(0.935, 0.028)
        sleep(1)
        # 充值100金币
        self.d.click(0.217, 0.33)
        self.d.xpath('//*[@text="一键购买"]').click()
        sleep(5)
        # 点击x图标，返回游戏
        self.d.click(0.942, 0.075)
        sleep(2)

        # 游戏界面中点击返回图标
        self.d.click(0.083, 0.024)
        sleep(1)
        # 确定退出游戏
        self.d.click(0.516, 0.59)
        sleep(2)

    def test_buy_fail(self):
        # 点击主界面的+图标，进入商城购买界面
        self.d.click(0.321, 0.06)
        sleep(1)
        # 充值100金币
        self.d.click(0.217, 0.33)
        sleep(1)
        self.d.press('back')
        sleep(3)
        # 点击x图标，返回到主界面
        self.d.click(0.942, 0.075)
        sleep(1)

        # 进入到游戏内
        self.d.click(0.505, 0.687)
        sleep(2)
        # 点击游戏内+图标，进入商城购买界面
        self.d.click(0.935, 0.028)
        sleep(1)
        # 充值100金币
        self.d.click(0.217, 0.33)
        sleep(1)
        self.d.press('back')
        sleep(3)
