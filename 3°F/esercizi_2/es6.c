// Scrivere un programma che permetta di visualizzare le prime n righe del triangolo di tartaglia 
//(con n inserito da tastiera).
/*
#include <stdio.h>
void main(){
	int j,i = 0;
	int n = 5;
	int risultato = 1;
	
	for (i; i < n; i++){
		int lista[i+1];
		lista[i] = risultato;
		int list[i+2];
		for (j; j < i+2; j++){
			list[j] = risultato
		}
		risultato = lista[0] + lista [1]
		
		
		for(j; j < i+1; j++){
			printf("%d ", lista[i]);
		}
		
	}
	}
*/

  
#include <stdio.h>
#include <stdlib.h>

main()
{
	int riga,i,j,molt=1;
	do{
		printf("Inserisci la riga: ");
		scanf("%d",&riga);
	}while(riga<1);
	for(i=0;i<=riga;i++)
	{
		for(j=0;j<riga-i;j++)
		{
			printf("  ");
		}
		for(j=0;j<=i;j++)
		{
			if(j==0)
				molt=1;
			else
				molt=molt*(i-j+1)/j;
			printf("%4d",molt);
		}
		printf("\n");
	}
}

// Scrivere un programma che permetta di visualizzare le prime n righe del triangolo di tartaglia 
//(con n inserito da tastiera).

#include <stdio.h>
void main(){
	int i = 1;
	int j = 1;
	int volte = 1;
	int risultato = 1;
	for(i; i <= volte; i++ ){
		int lista[i] = risultato;
		int list[i+1];
		for(j; j <= i; j++){
			printf(" %d ", lista[j]);
		}
		printf("\n");
	}
}

