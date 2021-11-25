// Scrivere una funzione che presi in input 2 numeri a e b, calcoli a^b.

#include <stdio.h>
#include <math.h>

void main(){
	int base, esponente, risultato;
	printf("Base: ");
	scanf("%d", &base);
	printf("Esponente: ");
	scanf("%d", &esponente);
	risultato = pow(base, esponente);
	printf("Risultato: %d", risultato);
}
