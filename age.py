# Zadání veku uzivatele
vek = int(input('Kolik je ti let? '))

# Kontrola na neobvykle vysoky vek
if vek > 100:
    print('Wow, to je úctyhodný věk! Nejsi náhodou upír?')
    
elif vek >= 18:
    print('Jsi dospělý.')
    vek_za_pet_let = vek + 5
    print('Za 5 let ti bude', vek_za_pet_let, 'let.')
    
# Kontrola na neobvykle vysoky vek
elif vek < 0:
    print('Věk nemůže být záporný! Zadal jsi to správně.')
    
else:
    print('Jsi nezletilý.')
