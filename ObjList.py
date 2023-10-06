from tkinter import *
from Settings import *
from tkinter.colorchooser import askcolor
from numpy import array


class ObjList(Frame):
    def __init__(self, board, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.names = []
        self.board = board
        self.entrylabel = Label(parent,
                                text="\nИмя добавляемого объекта:",
                                font='Arial 10', bg='salmon')
        self.entry = Entry(parent, font='Arial 12')
        self.btn_submit = Button(parent,
                                 text="Создать", font='Arial 10',
                                 command=self.new_object)
        self.btn_clear = Button(parent,
                                text="Удалить", font='Arial 10',
                                command=self.delete)
        self.btn_showing = Button(parent,
                                  text="Информация", font='Arial 10',
                                  command=self.setting)
        self.box = Listbox(parent, selectmode=SINGLE)
        self.scroll = Scrollbar(parent, command=self.box.yview)
        self.placeall()

    def placeall(self):
        self.entrylabel.grid(row=0, column=0, columnspan=3)
        self.entry.grid(row=1, column=0, columnspan=3)
        self.btn_submit.grid(row=2, column=0)
        self.btn_clear.grid(row=2, column=1)
        self.btn_showing.grid(row=2, column=2)
        self.box.grid(row=3, column=0, columnspan=3, sticky=W + E)
        self.scroll.grid(row=3, column=3, sticky=N + S)
        self.box.config(yscrollcommand=self.scroll.set)

    def new_object(self):
        if self.entry.get() != '' and\
                not self.names.count(self.entry.get()):
            self.box.insert(END, self.entry.get())
            self.names.append(self.entry.get())
            self.board.addobj(self.entry.get())
        self.entry.delete(0, END)

    def delete(self):
        x = self.names.pop(self.box.curselection()[0])
        self.board.delobj(x)
        self.box.delete(self.box.curselection())

    def setting(self):
        x = self.board.lis[self.box.curselection()[0]]
        SettingWindow(self.board, x, self.names,
                      self.box.curselection()[0], self.box)


class SettingWindow(Tk, Settings):
    def __init__(self, board, x, names, i, box):
        super().__init__()
        self['bg'] = self.SettingColor
        self.title("Изменение параметров")
        self.geometry(self.SettingScale)
        self.resizable(width=False, height=False)
        self.board, self.box = board, box
        self.ball, self.i = x, i
        self.names, self.entlis = names, []
        r, col = self.ball[0].getgeom()
        self.collab = Label(self, bg=col, anchor='e')
        self.initlabels()
        self.initentries()
        self.initbtns()

    def initlabels(self):
        self.collab.place(x=190, y=70, height=40, width=60)
        xs = array([['Название:', 40, 10, 20, 60],
                    ['x:=', 7, 40, 20, 60],
                    ['y:=', 7, 60, 20, 60],
                    ['rad:=', 7, 80, 20, 60],
                    ['velocity:=', 7, 100, 20, 60],
                    ['k:=', 7, 120, 20, 60],
                    ['m:=', 7, 140, 20, 60]])
        for i in xs:
            Label(self, text=i[0], anchor='e').\
                place(x=i[1], y=i[2], height=i[3], width=i[4])

    def initentries(self):
        name = self.ball[0].getname()
        x, y = self.ball[0].getcoords()
        m, v, k = self.ball[0].getphys()
        r, col = self.ball[0].getgeom()
        xs = array([[140, 10, 25, 50, name],
                    [68, 40, 20, 60, x],
                    [68, 60, 20, 60, y],
                    [68, 80, 20, 60, r],
                    [68, 100, 20, 60, f"{v[0]} {v[1]}"],
                    [68, 120, 20, 60, k],
                    [68, 140, 20, 60, m]])
        for i in xs:
            e = Entry(self)
            self.entlis.append(e)
            e.place(x=i[0], y=i[1], height=i[2], width=i[3])
            e.insert(0, i[4])

    def initbtns(self):
        Button(self, text="Изменить цвет", command=self.change_color)\
            .place(x=170, y=40)
        Button(self, text='Сохранить', command=self.save_info)\
            .place(x=180, y=115)

    def change_color(self):
        (rgb, hx) = askcolor()
        self.collab.config(bg=hx)

    def save_info(self):
        name = self.ball[0].getname()
        self.names[self.names.index(name)] = self.entlis[0].get()
        self.box.delete(self.i)
        self.box.insert(self.i, self.entlis[0].get())
        velocity = array([float(self.entlis[4].get().split(' ')[0]),
                          float(self.entlis[4].get().split(' ')[1])])
        self.board.setobj(name, self.entlis[0].get(),
                          float(self.entlis[1].get()),
                          float(self.entlis[2].get()),
                          float(self.entlis[6].get()),
                          velocity,
                          float(self.entlis[5].get()),
                          float(self.entlis[3].get()),
                          self.collab["background"])
        self.destroy()
