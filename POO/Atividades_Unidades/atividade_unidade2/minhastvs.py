import eletrodomesticos

tv_sala = eletrodomesticos.Televisao()
tv_sala.nome = "tv_sala"
tv_sala.tamanho = 32
tv_sala.marca = "Filipys"

tv_quarto = eletrodomesticos.Televisao()
tv_quarto.nome = "tv_quarto"
tv_quarto.marca = "Xilco"
tv_quarto.ligada = True

print("Nome | Canal Atual | Tamanho | Marca | Ligada (S/N)")
print(f"{tv_sala.nome} | {tv_sala.canal} | {tv_sala.tamanho} | {tv_sala.marca} | {'S' if tv_sala.ligada else 'N'}")

print(f"{tv_quarto.nome} | {tv_quarto.canal} | {tv_quarto.tamanho} | {tv_quarto.marca} | {'S' if tv_quarto.ligada else 'N'}")