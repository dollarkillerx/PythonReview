# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 22:10 
# @Author : DollarKillerx
# @Description :  err

def test_err():
    raise Exception('error')


if __name__ == '__main__':
    try:
        test_err()
    except Exception:
        print(Exception)
    finally:
        print("end")
