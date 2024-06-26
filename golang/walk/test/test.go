package main

import (
	"os"
	"github.com/pirogom/walkmgr"
)

func main() {
	wm := walkmgr.NewWin("WebView2 Test1", 800, 600)
	var wv *walkmgr.WebView2
	wv = wm.WebView2(os.TempDir(), func() {
		wv.Navigate("https://letskorail.com")
	}, func() {
		walkmgr.MsgBox("WebView2 런타임을 찾을 수 없습니다.")
	})

	wm.StartForeground()
}
