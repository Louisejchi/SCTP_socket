import speedtest

def test_speed():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    print('Download speed:', res['download'])
    print('Upload speed:', res['upload'])
    print('Ping:', res['ping'])

test_speed()

