#include <stdio.h>

void main (){
	int volte;
	printf("Quante volte devi calcolare? ");
	scanf("%d", &volte);

	
	int i = 0;
	int x1 = 1;
	int x2 = 1;
	int x3;
	printf("%d %d ", x1, x2);
	for (i; i < volte - 2; i++){
		x3 = x1 + x2;
		printf("%d ", x3);
		x1 = x2;
		x2 = x3;
				
	
	}
}

