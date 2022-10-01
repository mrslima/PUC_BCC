#include <stdio.h>
#include <stdbool.h>

#define SIZE_CATALOGO 5
#define LEN_DESC 30

const char * operacoes = "Escolha uma operação:\n\
[1] Listar catálogo\n\
[2] Inserir novo produto\n\
[3] Remover produto\n\
[4] Atualizar estoque\n\
[5] Aumentar estoque\n\
[6] Reduzir estoque\n\
[7] Sair\n\n\
>>> ";


enum Categoria_t {ELETRODOMESTICO, FERRAMENTA, VESTUARIO};

typedef struct
{
  int codigo;
  char descricao[LEN_DESC];
  int estoque;
  enum Categoria_t categoria;
} Catalogo_t;

char categoria_nome[3][16] = {"Eletrodoméstico", "Ferramenta", "Vestuário"};
Catalogo_t catalogo[SIZE_CATALOGO];
int index_catalogo, cod_itens;

void limparBuffer(void){
  char c;
  while ((c = getchar()) != '\n');
}

void listar_catalogo(void){
  if (index_catalogo == 0){
    puts("\nNenhum produto registrado.\n");
  } else{
    char temp;
    for (int i = 0; i < index_catalogo; i++){
      switch (catalogo[i].categoria){
        case ELETRODOMESTICO:
          temp = "Eletrodoméstico";
          break;
        case FERRAMENTA:
          temp = "Ferramenta";
          break;
        case VESTUARIO:
          temp = "Vestuário";
          break;
      }
      
      printf("Código: %i\n\
      Descrição: %s\n\
      Estoque: %i\n\
      Categoria: %s\n", catalogo[i].codigo, catalogo[i].descricao, catalogo[i].estoque, temp);
    }
  }
}

bool inserir_produto(void){
  if (index_catalogo < SIZE_CATALOGO){
    int temp;
    
    puts("\n|--<[ INSERIR NOVO PRODUTO ]>--|\n");
    puts("Descrição:");
    scanf("%[^\n]s", &catalogo[index_catalogo].descricao);
    limparBuffer();
    
    puts("Categoria:");
    puts("[1] Eletrodoméstico\n[2] Ferramenta\n[3] Vestuário\n");
    scanf("%d", &temp);
    limparBuffer();

    switch (temp-1){
      case 0:
        catalogo[index_catalogo].categoria = 0;
        break;
      case 1:
        catalogo[index_catalogo].categoria = 1;
        break;
      case 2:
        catalogo[index_catalogo].categoria = 2;
        break;
    }

    catalogo[index_catalogo].codigo = cod_itens; 
    cod_itens++;
    index_catalogo++;
  } else {
    puts("Catálogo lotádo! Operação não realizada.");
    return false;
  }

  return true;
}

// void removerProduto(void){
//   ...
// }

// void atualizarEstoque(void){
//   ...
// }

// void aumentarEstoque(void){
//   ...
// }

// void reduzirEstoque(void){
//   ...
// }


int main(void){
  int usr_in;
  bool validador_mainloop = true;
  bool validador_input = true;
  
  do{
    do{
      printf("%s", operacoes);
      scanf("%d", &usr_in);
      limparBuffer();

      switch (usr_in){
        case 1:
          listar_catalogo();
          break;
        case 2:
          inserir_produto();
          break;
        case 3:
          break;
        case 4:
          break;
        case 5:
          break;
        case 6:
          break;
        case 7:
          validador_input = false;
          validador_mainloop = false;
          break;
      };
      
    } while (validador_input == true);
    
  } while (validador_mainloop == true);
  
  puts("Programa encerrado.");
  return 0;
}