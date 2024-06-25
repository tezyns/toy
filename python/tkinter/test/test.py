import tkinter
from tkwebview2.tkwebview2 import WebView2
from System.Threading import Thread,ApartmentState,ThreadStart    

def main():
    root = tkinter.Tk()

    frame=WebView2(root,100,100)
    frame.pack(side='left')
    frame.load_html('<h1>hi hi</h1>')

    frame2=WebView2(root,500,500)
    frame2.pack(side='left',padx=20,fill='both',expand=True)
    frame2.load_url('https://letskorail.com/')

    root.mainloop()

t = Thread(ThreadStart(main))
t.ApartmentState = ApartmentState.STA
t.Start()
t.Join()