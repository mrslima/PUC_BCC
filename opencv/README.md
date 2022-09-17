# Resolução TAREFA 1

- **Como uma imagem é representada no computador? Matriz, Vetor?**
  - answers...
- **O que é um pixel e o que representa os valores de 0 a 255?**

----

####  Produza um código que carregue uma imagem do disco, desenhe um retangulo em qualquer posição e exiba na tela.

```c
#include <stdio.h>

enum Cores_do_semaforo { VERMELHO, VERDE, AMARELO };

int main()
{
    enum Cores_do_semaforo s1 = VERDE; // cor do semáforo primário

    printf("enum: %lu\n", sizeof(s1));

    return 0;
}
```
