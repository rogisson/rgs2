preco_livro = 32.90 *0.65
quantidade = 75

custo_do_livro = preco_livro * quantidade
frete = 4 + (quantidade-1) * 0.80

preco_final = custo_do_livro + frete
print (preco_final)
