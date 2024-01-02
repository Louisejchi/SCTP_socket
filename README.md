# README.md

## 安裝與執行指南

* git clone : git https://github.com/Louisejchi/SCTP_socket.git

1. 確認您的系統已安裝 Python3。
2. 使用 `sudo pip3 install pysctp` 安裝 `pysctp` 套件。
3. 執行 `client.py`。
4. 結束後，使用 `sudo pip3 uninstall pysctp` 移除 `pysctp` 套件。

或者，您可以使用提供的 `Makefile` 來自動完成以上步驟：

```bash
make all

