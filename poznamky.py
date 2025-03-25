barva = input("Zadejte vaší oblíbenou barvu")
#input načte od uživatele zadanou věc do proměné
číslo = int(input("zadejte své oblíbené číslo"))
#přetypování na číslo
if barva == "modrá":
    print("barva není hezká")
elif barva == "modrá" and barva == "černá":
    print("barva modrá je hezčí než barva černá")
else:
    print("nemáš vkus")

