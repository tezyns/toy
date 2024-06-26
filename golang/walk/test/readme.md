## golang 설치

사전에 python 가상환경 tool인 [mambaforge](https://github.com/conda-forge/miniforge) 설치가 된 상태에서...

mamba create -n golang

mamba activate golang

mamba install go=1.22

## 작업 폴더 생성, 환경 설정

"test" 폴더 생성, 폴더로 이동

go mod init test

이제 여기부터는 [golang gui 강좌](https://modu-print.com/%EA%B0%9C%EB%B0%9C%EA%B4%80%EB%A0%A8/go%EB%A1%9C-ms-%EC%9C%88%EB%8F%84-%EB%84%A4%EC%9D%B4%ED%8B%B0%EB%B8%8C-gui-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EB%A7%8C%EB%93%A4%EA%B8%B0-1/) 참고하였음...

go get github.com/lxn/win

go get github.com/lxn/walk

go get github.com/akavel/rsrc

test.manifest 파일 생성

[GOPATH]\bin\rsrc -manifest test.manifest -o test.syso

## 코드 작성, 빌드

go get github.com/pirogom/walkmgr

go 코드 작성 후 빌드는 빌드는 아래와 같이

go build -ldflags "-s -w -H windowsgui"