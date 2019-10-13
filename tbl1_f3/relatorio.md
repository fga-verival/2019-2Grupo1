## TBL 1 - Fase 3

## Equipe

| Nome | GitHub|
|--|--|
| André Bargas | [@andrebargas](https://github.com/andrebargas) |
| Brian Lui | [@brian2397](https://github.com/brian2397) |
| Gustavo Duarte Moreira |[@gustavoduartemoreira](https://github.com/gustavoduartemoreira) |
| Lucas Machado | [@lmmLucasMachado](https://github.com/lmmLucasMachado) |
| Mateus Oliveira | [@omateusp](https://github.com/omateusp) |
| João de Assis| [@Jonjon667](https://github.com/Jonjon667) |
| Tâmara Barbosa | [@tamarabarbosa](https://github.com/tamarabarbosa) |

## 1. Walkthrough

Walkthrough é um processo de teste que consiste em um time de tamanho variado que lê e inspeciona o programa. Nele, a revisão do código é executada passo-a-passo com o objetivo de verificar a ocorrência de erros, esse processo é realizado por um grupo de desenvolvedores e conta com o autor para guiar os outros integrantes usando cenários pré-definidos.

O walkthrough é melhor do que um processo em que o próprio programador lê seu programa, ele é mais efetivo pois outras pessoas além do autor estão envolvidos facilitando a identificação dos erros. Outra vantagem dessa técnica é que normalmente expõe um conjunto de erros e suas localizações precisas no código.

Alguns testadores que utilizam desta técnica, concluíram que processos de teste humanos como Inspeções e Walkthroughs tendem a ser mais efetivas que testes computadorizados em encontrar certos tipos de erros, enquanto o oposto vale para outros tipos de erros. Então estas técnicas são complementares à testes realizados pelo computador.

## 2. Pseudocódigo 
### SpaceX
```
    NEXT_LAUNCH ← 1
    LATEST_LAUNCH ← 2
    UPCOMING_LAUNCHES ← 3
    PAST_LAUNCHES ← 4

    procedure run(cls):
        
        ▷ Exibe menus para o usuário

        begin
            while:
                begin
                    print menu
                    scan number
                    option ← number
                    
                    if inteiro:
                        begin
                            if option < 1 or option > 5
                                begin
                                    print Essa opção não existe, por favor insira uma opção válida.
                                end
                            if option == 5:
                                begin
                                    __close()
                                end
                            else:
                                begin
                                    __show_result(option)
                                end
                        end
                
                    print Deseja sair da aplicação? (S/N)
                    scan answer 

                    if answer == S
                        begin
                            __close()
                        end
                end

        end

    procedure __show_result(cls, option):
      
        ▷ Executa uma função específica

        begin
            print()

            if option == SpaceX.NEXT_LAUNCH:
                begin
                    __next_launch()
                end
            elif option == SpaceX.LATEST_LAUNCH:
                begin
                    __latest_launch()
                end
            elif option == SpaceX.UPCOMING_LAUNCHES:
                begin
                    __upcoming_launches()
                end
            elif option == SpaceX.PAST_LAUNCHES:
                begin
                    __past_launches()
                end
            else:
                begin
                    print Opção invalida
                end
          end
            
    procedure __clean(seconds):
        
        ▷ Limpa o console

        begin
            sleep

            if 'win' in sys.platform:
                begin
                    clean windows' screen
                end
            else:
                begin
                    clean another os screen
                end
        end
        
    procedure __close():
        
        ▷ Fecha o programa
        begin
            print Finalizando o programa...
            sleep
        end

    procedure __next_launch():
        
        ▷ Retorna os próximos lançamentos
        begin
            connection ← next launch from the api
            print connection.result
        end

    procedure __upcoming_launches():
      
        ▷ Exibe os próximos lançamento
        begin
            connection ← upcoming launch from the api

            for result in connection.result:
                begin
                    print result
                end
        end


    procedure __latest_launch():
        
        ▷ Exibe o ultimo lançamento
        begin
            connection ← latest launch from the api
            print connection.result
        end


    procedure __past_launches():
        
        ▷ Exibe os lançamentos passados
        begin
            connection ← past launch from the api

            for result in connection.result:
                begin
                    print(result)
                end
        end
 ```


## Referências

- FERREIRA, Bruno. UMA TÉCNICA PARA VALIDAÇÃO DE PROCESSOS DE DESENVOLVIMENTO DE SOFTWARE. Belo Horizonte, p.60-61, fev. 2008.

-  MYERS, Glenford J.. The Art of Software Testing. p.22-28.
