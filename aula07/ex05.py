metros = float(input('digite quantos metros você quer converter'))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('{}km\n{}hm\n{}dam\n{}m\n{:.0f}dm\n{}cm\n{}mm'.format(km, hm, dam, metros, dm, cm, mm))