#include <stdio.h>

void main (){
	int volte;
	int numero;
	int i = 0;
	
	int lista[3];	
	for (i; i < 3; i++){
		printf("Inserisci Numero: ");
		scanf("%d", &numero);
		int j = 0;
		for (j; j <= volte; j++){
			if (numero == lista[j]){
				printf("%d e' gia' presente  \n", numero);
			}
		}
			
		lista[i] = numero;	
	}
}

