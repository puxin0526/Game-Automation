from time import sleep

import uiautomator2 as u2

'''
执行该类需一起执行，
请清除手机app数据

'''


class TestShowRank:

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
        # 返回主页
        self.d.click(0.504, 0.833)
        sleep(2)

    def teardown_class(self):
        self.d.app_stop("puzzle.game.find.differences")

    def test_rank(self):
        # 点击排行榜
        self.d.click(0.222, 0.872)
        sleep(2)
        # 滑动查看排名
        for i in range(0, 18):
            self.d.swipe(0.508, 0.611, 0.508, 0.334, duration=0.08)
            sleep(1)
        # 正常退出排行榜
        self.d.click(0.932, 0.193)
        sleep(3)
