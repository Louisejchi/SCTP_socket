# Makefile
all: install run clean

install:
	@echo "確認 Python3 已安裝..."
	which python3 || (echo "Python3 未安裝" && exit 1)
	@echo "安裝 pysctp..."
	sudo pip3 install pysctp
	@echo "安裝 iperf3..."
	sudo apt-get install -y iperf3
run:
	@echo "執行 SCTP_socket/client.py..."
	python3 client.py
	@echo "執行 SCTP_socket/tcp_test.py..."
	python3 tcp_test.py
	@echo "執行 SCTP_socket/sctp_test.py..."
	python3 sctp_test.py

clean:
	@echo "清理安裝的套件..."
	sudo pip3 uninstall -y pysctp
	sudo apt-get remove -y iperf3

