#Formatação de Strings
from datetime import datetime
ano_atual = datetime.now().year
clube = 'SCCP'
ano_fundacao = 1910
campeonato_mundial = 2
print(f"{clube}possui{campeonato_mundial}titulos mundiais.")
print(f"Corinthians {ano_atual - ano_fundação} anos de existendia.")