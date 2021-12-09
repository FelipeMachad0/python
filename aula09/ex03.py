cidade = str(input('Em qual cidade você nasceu? ')).strip()
santo = cidade[:5].upper()
if santo == 'SANTO':
    print('A cidade que você nasceu começa com Santo')
else:
    print('A cidade que você nasceu não começa com Santo')
