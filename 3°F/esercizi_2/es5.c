// Scrivere un programma che, preso in input un array di dimensione n, generi un secondo array che non contenga i duplicati.

#include <stdio.h>

void main(){
	int n = 8;
	int lista[8] = {43, 45,22, 543, 11, 6, 7, 7};
	int list[8] = {};
	int i = 0;
	int x, y;
	int j = 0;

	for (j; j < n; j++){
		
		for (i; i < n-1; i++){
			if (lista[i] < lista[i+1]){
				x = lista[i];
				y = lista[i+1];
				lista[i] = y;
				lista[i+1]	= x;
			}
		}
		i = 0;
	}
	
	j = 0;
	for (j;j < n; j++){
		printf("%d ", lista[j]);
	} 
	printf("\n");
	j = 0;
	for (j; j < n; j++){
		for (i; i <= n-1; i++){
			if (lista[i] != lista[i+1]){
				list[i] = lista[i];
			}
	}
	j = 0;
	for (j;j < n; j++){
	
		printf("%d ", list[j]);
	} 
}
}
