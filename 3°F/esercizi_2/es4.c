#include <stdio.h>

void main(){
	int n = 7;
	int lista[n] = {43, 45,22, 543, 11, 6, 7};
	int i = 0;
	int x, y;
	int b = 0;

	for (b; b < n; b++){
		
		for (i; i < n-1; i++){
			if (lista[i] < lista[i+1]){
				x = lista[i];
				y = lista[i+1];
				lista[i] = y;
				lista[i+1]	= x;
			}
		}
	}
	printf("%d", lista[0]);
}

