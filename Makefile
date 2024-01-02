# Makefile
all: install run clean

install:
	@echo "確認 Python3 已安裝..."
	which python3 || (echo "Python3 未安裝" && exit 1)
	@echo "安裝 pysctp..."
	sudo pip3 install pysctp

run:
	@echo "執行 SCTP_socket/client.py..."
	python3 client.py

clean:
	@echo "清理安裝的套件..."
	sudo pip3 uninstall -y pysctp

