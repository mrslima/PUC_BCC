# Resolução TAREFA 1

- **Como uma imagem é representada no computador? Matriz, Vetor?**
  - Uma imagem é um conjunto de pixels que são armazenados num array em forma de matriz multidimensional.
- **O que é um pixel e o que representa os valores de 0 a 255?**
  - Como o computador entende números e não cores, cada pixel é salvo no computador como um valor que corresponde a intensidade de cor presente nele. (0 - totalmente preto, 255 - totalmente branco | para imagens coloridas utiliza-se a mesma lógica, mas para o sistema RGB)
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
