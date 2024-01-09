import time

import pygetwindow

from common import helper, logger, globle, file
from game import init, mem

if __name__ == '__main__':
    try:
        globle.cmd = "cmd"
        model_name = "DNF.exe"
        process_id = helper.get_process_id_by_name(model_name)
        if process_id == 0:
            logger.info("等待游戏运行...", 1)
            while True:
                window = pygetwindow.getWindowsWithTitle("地下城与勇士：创新世纪")
                if window:
                    process_id = helper.get_process_id_by_name(model_name)
                    if process_id != 0:
                        mem.set_process_id(process_id)
                        print("附加游戏成功")
                        break
                time.sleep(0.2)

        # 全局刷图计次初始化
        countCfgName = "C:\\config.ini"
        confExists = file.path_exists(countCfgName)
        if not confExists:
            file.write_ini(countCfgName, "default", "count", "0")

        # 判断是否有图标
        if mem.read_int(0x140000000) != 9460301:
            raise Exception("无读写权限")

        # 初始化全局空白地址
        init.init_empty_addr()

        logger.info("加载成功-欢迎使用", 1)
        logger.info("当前时间：{}".format(helper.get_now_date()), 1)
        init.hotkey()
    except KeyboardInterrupt as e:
        print("信道推出")
    except Exception as err:
        helper.print_trace("main", err)
