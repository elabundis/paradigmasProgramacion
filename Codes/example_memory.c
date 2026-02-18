#include <stdio.h>
#include <stdlib.h>

int main() {
	  // Alojar 20 bytes de memoria para cinco enteros en el apuntador 'ptr1'
		// (el bloc de memoria no esta inicializado y tiene informacion basura)
    int *ptr1 = (int *)malloc(5 * sizeof(int));

    // Checando fallos al alojar bloques de memoria
    if (ptr1 == NULL) {
        printf("Fallo al alojar memoria\n");
        exit(0);
    } else {
			printf("Se logro alojar bloque de memoria\n");
		}
    //--------------------------------------------------------------
    
    // Reajustar el bloque de memoria para que quepan 10 enteros
    ptr1 = (int *)realloc(ptr1, 10 * sizeof(int));
		
		// Asignando valores al arreglo
    for (int i = 0; i < 10; i++)
        ptr1[i] = i + 1;
		
		// Imprimiendo valores
    for (int i = 0; i < 10; i++)
        printf( "%d ", ptr1[i] );
    puts("");
    //--------------------------------------------------------------
    
    // No olvidar liberar la memoria en la pila terminados nuestros cálculos
    free(ptr1);
    // Es buena práctica hacer que el apuntador apunte a NULL ya que en este
    // momento no apunta a una dirección válida en memoria (dangling pointer)
    ptr1 = NULL;
    //--------------------------------------------------------------
    
		// Crear bloque de memoria con cinco enteros inicializados a zero
    int *ptr2 = (int *)calloc(5, sizeof(int));

		// Imprimiendo apuntador inicializado
    for (int i = 0; i < 5; i++)
        printf( "%d ", ptr2[i] );
    puts("");

    // No olvidemos liberar memoria
    free(ptr2);
    ptr2 = NULL;

    return 0;
}
