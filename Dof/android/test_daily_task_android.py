from time import sleep
import uiautomator2 as u2

'''
执行该类需一起执行，
请清除手机app数据

'''


class TestGameInterface:

    def setup_class(self):
        self.d = u2.connect("127.0.0.1:7555")
        self.d.app_start("puzzle.game.find.differences")
        sleep(15)

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
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 正常玩过第6关

        # 关卡2
        self.d.click(0.134, 0.159)
        sleep(0.5)
        self.d.click(0.442, 0.152)
        sleep(0.5)
        self.d.click(0.74, 0.306)
        sleep(0.5)
        self.d.click(0.506, 0.355)
        sleep(0.5)
        self.d.click(0.266, 0.405)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 关卡3
        self.d.click(0.39, 0.14)
        sleep(0.5)
        self.d.click(0.586, 0.162)
        sleep(0.5)
        self.d.click(0.44, 0.296)
        sleep(0.5)
        self.d.click(0.748, 0.313)
        sleep(0.5)
        self.d.click(0.538, 0.388)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 关卡4
        self.d.click(0.26, 0.264)
        sleep(0.5)
        self.d.click(0.368, 0.325)
        sleep(0.5)
        self.d.click(0.514, 0.344)
        sleep(0.5)
        self.d.click(0.626, 0.211)
        sleep(0.5)
        self.d.click(0.83, 0.273)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 关卡5
        self.d.click(0.3, 0.717)
        self.d.click(0.378, 0.599)
        self.d.click(0.582, 0.586)
        self.d.click(0.736, 0.522)
        self.d.click(0.844, 0.61)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 关卡6
        self.d.click(0.142, 0.736)
        self.d.click(0.474, 0.481)
        self.d.click(0.534, 0.618)
        self.d.click(0.794, 0.635)
        self.d.click(0.882, 0.787)
        sleep(3)
        # 点击主页
        self.d.click(0.506, 0.832)
        sleep(2)

    def teardown_class(self):
        self.d.app_stop('puzzle.game.find.differences')

    def test_daily_task(self):
        # 点击每日任务
        self.d.click(0.792, 0.871)
        sleep(1)
        # 领取宝箱奖励
        self.d.click(0.71, 0.195)
        sleep(2)
        # 返回继续
        self.d.click(0.502, 0.688)
        sleep(4)
