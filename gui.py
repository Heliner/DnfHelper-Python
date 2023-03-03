import _thread
import time

import xcgui._xcgui as gui
from xcgui import XApp, XWindow, XButton, XEdit, XShapeText

from common import logger, helper, convert

svgIcon = '<svg t="1674984352573" class="icon" viewBox="0 0 1024 1024" version="1.1" ' \
          'xmlns="http://www.w3.org/2000/svg" p-id="10315" width="16" height="16"><path d="M901.957085 ' \
          '349.126786c-60.072164-87.975001-153.76426-100.09183-187.170868-101.49977-79.698013-8.106329-155.59885 ' \
          '46.931378-196.0025 46.931377-40.40365 0-102.779718-45.822091-168.86763-44.627473-86.908379 ' \
          '1.279947-166.990375 50.515229-211.788509 128.421315-90.32157 156.665472-23.12437 388.762468 64.850631 ' \
          '515.818508 43.048873 62.248073 94.332069 132.133161 161.6146 129.615933 64.850631-2.559893 ' \
          '89.425607-41.982251 167.673013-41.982251 78.418066 0 100.433149 41.982251 169.03829 40.702304 ' \
          '69.799758-1.279947 114.000583-63.400025 156.665473-125.818758 49.405941-72.188992 69.714429-141.98875 ' \
          '70.909045-145.572601-1.578601-0.725303-135.973001-52.221824-137.380942-207.095371-1.279947-129.573268 ' \
          '105.68093-191.778676 110.502062-194.893213zM715.852839 0.042665c-51.496521 2.133244-113.829924 ' \
          '34.302571-150.820382 77.479438-33.107954 38.3984-58.706887 99.622516-50.899213 158.414733 57.51227 ' \
          '4.479813 112.720637-29.182784 148.473814-72.530311 35.710512-43.176868 59.816174-103.377026 ' \
          '53.245781-163.36386z" fill="#1afa29" opacity=".65" p-id="10316"></path></svg>'


version = '1.0.0'

class DemoWindow(XWindow):
    def __init__(self):
        super(DemoWindow, self).__init__(0, 0, 300, 400, "情歌 √ 当前时间 {}".format(convert.get_now_date()), 0,
                                         gui.window_style_modal)
        _thread.start_new_thread(self.title_time, ())

        # 设置窗口图标
        self.setIcon(gui.XImage.loadSvgString(svgIcon))
        # 禁止改变大小
        self.enableDragBorder(False)
        # 设置边框
        self.setBorderSize(0, 30, 0, 0)

        XShapeText(0, 35, 60, 30, "卡号:", self)
        self.card_edit = XEdit(35, 35, 200, 30, self)
        self.card_edit.setText("19930921")
        self.card_edit.enablePassword(True)
        self.card_edit.setTextAlign(gui.edit_textAlign_flag_center)

        self.activation_but = XButton(244, 35, 50, 30, "激活", self)
        self.activation_but.regEvent(gui.XE_BNCLICK, self.activation)

        self.edit_content = XEdit(1, 70, 300, 310, self)
        self.edit_content.enableMultiLine(True)
        self.edit_content.enableReadOnly(True)
        self.edit_content.autoScroll()
        self.edit_content.showSBarV(True)
        self.edit_content.showSBarH(True)
        self.edit_content.scrollBottom()

        self.run_time_label = XShapeText(1, 375, 60, 30, "运行时间:", self)
        self.run_time_value = XShapeText(56, 375, 60, 30, "00:00:00", self)
        _thread.start_new_thread(self.app_run_time, ())

        self.version_label = XShapeText(220, 375, 60, 30, "版本号:", self)
        self.version_value = XShapeText(260, 375, 60, 30, version, self)

    def activation(self, event, userdata):
        card_edit_val = self.card_edit.getText()
        logger.info(card_edit_val)
        if card_edit_val == "":
            return 1

    def app_run_time(self):
        while 1:
            time.sleep(1)
            self.run_time_value.setText(helper.get_app_run_time())
            self.run_time_value.redraw()
            self.edit_content.addTextUser("{}\n".format(convert.get_now_date()))
            self.edit_content.redraw()

    def title_time(self):
        while 1:
            time.sleep(1)
            self.setTitle("情歌 √ 当前时间 {}".format(convert.get_now_date()))
            self.redraw()


def main():
    app = XApp()
    window = DemoWindow()
    window.showWindow()
    app.run()
    app.exit()


if __name__ == '__main__':
    main()