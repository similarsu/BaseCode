from multiprocessing.dummy import Pool as ThreadPool, RLock  # 就把这边换了下

xiaoming = 8000
xiaozhang = 3000
xiaozhou = 5000


def test(lock):
    global xiaoming
    global xiaozhang
    global xiaozhou
    # 小明想一次搞定：
    with lock:
        # 小明转账2000给小张
        xiaoming -= 2000
        xiaozhang += 2000
        with lock:
            # 小明转账5000给小周
            xiaoming -= 5000
            xiaozhou += 5000


def main():
    print(f"[还钱前]小明{xiaoming},小张{xiaozhang},小周{xiaozhou}")
    lock = RLock()  # 就把这边换了下
    p = ThreadPool()
    p.apply_async(test, args=(lock, ))
    p.close()
    p.join()
    print(f"[还钱后]小明{xiaoming},小张{xiaozhang},小周{xiaozhou}")


if __name__ == '__main__':
    main()
