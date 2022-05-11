try:
    import MDCalc

    a = int(input('最初の整数:'))
    b = int(input('次の整数  :'))

    # MDCalcファイルの中のMDCクラスをインスタンス化している
    # インスタンス化するときのa, bはコンストラクタに渡される変数
    mdc = MDCalc.MDC(a, b)
    mdc.calcing()

except ZeroDivisionError:
    print('ゼロの割り算はできません！')

except ValueError:
    print('数字を入力してください')