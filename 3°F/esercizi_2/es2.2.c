// Ordinare un array di n elementi, misurare il tempo di esecuzione e chiedere all’utente se lo vuole in ordine crescente o decrescente,

#include <time.h>
#include <stdio.h>
#include <unistd.h>

void main(){
	int n = 7;
	int lista[n] = {43, 45,22, 543, 11, 6, 7};
	int i = 0;
	int x, y;
	int b = 0;
	char ordine;
	printf("Ordine decresente o cresente (d o c): ");
	scanf("%c", &ordine);
	
	double time_spent = 0.0;
 
    clock_t begin = clock();
	
	if (ordine == 'd'){
		for (b; b < n; b++){
			
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
	}
	
	else if (ordine == 'c'){
		for (b; b < n; b++){
			
			for (i; i < n-1; i++){
				if (lista[i] > lista[i+1]){
					x = lista[i];
					y = lista[i+1];
					lista[i] = y;
					lista[i+1]	= x;
				}
			}
			i = 0;
		}
	}
	else{
	    printf("%c non esiste", ordine);
	
	}
    if (ordine == 'd' || ordine == 'c'){
    	for (i; i < n; i++){
    		printf("%d ", lista[i]);
    		
    	}
    }
    	
    
 
    
    sleep(3);
 
    clock_t end = clock();

    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
 
    printf("\ntempo speso in secondi %f: ", time_spent);
 
}

