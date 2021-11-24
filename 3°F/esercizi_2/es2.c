// Ordinare un array di n elementi e misurare il tempo di esecuzione.

#include <time.h>
#include <stdio.h>
#include <unistd.h>

void main(){
	int n = 7;
	int lista[n] = {43, 45,22, 543, 11, 6, 7};
	int i = 0;
	int x, y;
	int j = 0;
	int b = 0;
	
for (b; b < n; b++){
	
	for (i; i < 6; i++){
		
		if (lista[i] >= lista[i+1]){
			
			x = lista[i];
			y = lista[i+1];
			lista[i] = y;
			lista[i+1]	= x;
		}
	}
	i = 0;
}

	for (j; j < n; j++){
		
		printf("%d ", lista[j]);
		
	}
	
	
    double time_spent = 0.0;
 
    clock_t begin = clock();
 
    sleep(3);
 
    clock_t end = clock();

    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
 
    printf("\ntempo speso in secondi %f: ", time_spent);
 
}
