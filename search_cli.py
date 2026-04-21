import sys
import pandas as pd
from census_engine import CensusEngine
from rich.console import Console
from rich.table import Table

def main():
    if len(sys.argv) < 2:
        print("Usage: python search_cli.py \"<search_term>\"")
        print("Example: python search_cli.py \"poverty\"")
        sys.exit(1)

    search_term = sys.argv[1]
    console = Console()
    
    try:
        # Initialize engine and load data
        engine = CensusEngine()
        df = engine.load_data()
        
        # Execute search
        results = engine.search(df, search_term)
        
        # Print summary
        count = len(results)
        console.print(f"\n[bold green]Found {count} results for term:[/bold green] [italic blue]'{search_term}'[/italic blue]\n")
        
        if count > 0:
            # Criando a tabela Rich
            table = Table(show_header=True, header_style="bold magenta", border_style="dim")
            
            # Adiciona as colunas baseadas no DataFrame
            for column in results.columns:
                table.add_column(column)

            # Adiciona as linhas (convertendo tudo para string para evitar erros)
            for _, row in results.iterrows():
                table.add_row(*[str(val) for val in row])

            console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()