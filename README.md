# README.md
## 說明
* 這個實驗室用來量測目前有多少台NAT支援SCTP(Stream Control Transmission Protocol)
* 測試各住家所在位置房東提供的網速，若成功，未來將提供表單，供所有暨大生山下住宿考量之一。

## 安裝與執行指南

* 建議使用 Ubuntu 環境
* git clone : `git clone https://github.com/Louisejchi/SCTP_socket.git`

1. 確認您的系統已安裝 Python3。
2. 使用 `sudo pip3 install pysctp` 安裝 `pysctp` 套件。
3. 執行 `SCTP_socket/client.py`。
4. 執行 `SCTP_socket/tcp_test.py`。
5. 執行 `SCTP_socket/sctp_test.py`。
6. 結束後，使用 `sudo pip3 uninstall pysctp` 移除 `pysctp` 套件。
7. 為確認測試資料地理位置，測試完成之後請填寫表單:`https://forms.gle/4RcVsndVPZyiX5Me7`
或者，您可以使用提供的 `Makefile` 來自動完成以上步驟：
(需先進入 SCTP_socket 目錄中)

```bash
make all

