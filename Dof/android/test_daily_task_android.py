from time import sleep
import uiautomator2 as u2

'''
执行该类需一起执行，
请清除手机app数据
honor6为测试机

本case主要测试点
1.能够正常玩到前5关
2.每日任务正常领取宝箱功能
'''


class TestGameInterface:

    def setup_class(self):
        self.d = u2.connect()
        self.d.app_start("puzzle.game.find.differences")
        sleep(15)

        # 跳过第一关教程
        self.d.click(0.602, 0.177)
        sleep(1)
        self.d.click(0.34, 0.24)
        sleep(1)
        self.d.click(0.266, 0.164)
        sleep(1.5)
        self.d.click(0.444, 0.44)
        sleep(1)
        self.d.click(0.682, 0.308)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 正常玩过第6关

        # 关卡2
        self.d.click(0.12, 0.196)
        sleep(0.5)
        self.d.click(0.436, 0.189)
        sleep(0.5)
        self.d.click(0.74, 0.306)
        sleep(0.5)
        self.d.click(0.501, 0.405)
        sleep(0.5)
        self.d.click(0.257, 0.833)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 关卡3
        self.d.click(0.384, 0.179)
        sleep(0.5)
        self.d.click(0.591, 0.202)
        sleep(0.5)
        self.d.click(0.436, 0.343)
        sleep(0.5)
        self.d.click(0.748, 0.313)
        sleep(0.5)
        self.d.click(0.542, 0.444)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 关卡4
        self.d.click(0.26, 0.264)
        sleep(0.5)
        self.d.click(0.36, 0.37)
        sleep(0.5)
        self.d.click(0.515, 0.393)
        sleep(0.5)
        self.d.click(0.635, 0.252)
        sleep(0.5)
        self.d.click(0.848, 0.318)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 关卡5
        self.d.click(0.292, 0.401)
        sleep(0.5)
        self.d.click(0.374, 0.281)
        sleep(0.5)
        self.d.click(0.584, 0.266)
        sleep(0.5)
        self.d.click(0.749, 0.198)
        sleep(0.5)
        self.d.click(0.855, 0.289)
        sleep(3)
        # 下一关
        self.d.click(0.504, 0.722)
        sleep(2)

        # 关卡6
        self.d.click(0.129, 0.423)
        sleep(0.5)
        self.d.click(0.476, 0.16)
        sleep(0.5)
        self.d.click(0.534, 0.294)
        sleep(0.5)
        self.d.click(0.805, 0.314)
        sleep(0.5)
        self.d.click(0.902, 0.476)
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
