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

    def test_rank(self):
        # 点击排行榜
        self.d.click(0.222, 0.872)
        sleep(2)
        # 滑动查看排名
        for i in range(0, 20):
            self.d.swipe(0.508, 0.611, 0.508, 0.304, duration=0.05)
            sleep(0.4)
        # 正常退出排行榜
        self.d.click(0.932, 0.193)
        sleep(3)
