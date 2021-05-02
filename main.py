import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # 親の画面状態をpackする。
        self.pack()
        self.create_widgets()

    # widgetsを生成して、packする関数
    def create_widgets(self):
        # ラベルwidgetsを作成する。
        # text : ラベルにつける名前を設定する。
        self.label = tk.Label(self, text="初めてのTkinter")
        # ラベルのwidgetをpackする。配置をtopとする。
        self.label.pack(side="top")

        # ボタンwidgetsを作成する。
        # text : ボタンにつける名前を設定する。
        # highlightthickness : ボタン要素からの余白を指定する。
        # fg : 文字色を変更する。
        # command : ボタンがクリックされた場合に、関数を呼び出す。
        self.hi_there = tk.Button(self,
                                  text="(click me)",
                                  highlightthickness=10,
                                  fg="purple",
                                  command=self.say_hi,
                                  )
        # ラベルのwidgetをpackする。配置をbottomとする。
        self.hi_there.pack(side="bottom")

    # ボタンを押された場合に、呼び出させる関数
    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
# インスタンスを呼び出す。
app = Application(master=root)
# 作成するアプリケーションをループさせてGUI表示を続けるように命令する。
# 何か動作したタイミングでGUIが閉じるような設計にする。
app.mainloop()
