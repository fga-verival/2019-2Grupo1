## TBL 1 - Fase 3

## Equipe

| Nome | GitHub| Participação |
|:--|:--|:--:|
| André Bargas | [@andrebargas](https://github.com/andrebargas) | 70% |
| Brian Lui | [@brian2397](https://github.com/brian2397) | 80% |
| Gustavo Duarte Moreira |[@gustavoduartemoreira](https://github.com/gustavoduartemoreira) | 90%|
| Lucas Machado | [@lmmLucasMachado](https://github.com/lmmLucasMachado) | 100% |
| Mateus Oliveira | [@omateusp](https://github.com/omateusp) | 95% |
| João de Assis| [@Jonjon667](https://github.com/Jonjon667) | 65% |
| Tâmara Barbosa Tavares | [@tamarabarbosa](https://github.com/tamarabarbosa) | 100%|

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
 
 ### Connect(object)
 ```
 ▷ Conecta na api
    

    procedure __init__(self, url, headers←None, params←None):
        
        ▷ Connection constructor
        begin
            if headers:
                begin
                    self.__headers ← headers
                end
            else:
                begin
                    self.__headers ← {'Accept': 'application/json'}
                end
            try:
                begin
                    __response ← requests from params
                end
        end

    procedure result(self):

        ▷ Obter JSON resultado da requisição

        begin
            if type(__result) == dict:
                begin
                    return Launch(
                        flight_number←__result.get('flight_number'),
                        mission_name←__result.get('mission_name'),
                        rocket←__result.get('rocket').get('rocket_name'),
                        rocket_type←__result.get('rocket').get('rocket_type'),
                        launch_success←__result.get('launch_success'),
                        launch_date←__result.get('launch_date_utc'),
                        launch_year←__result.get('launch_year')
                    )
                end

            launchs ← None
            
            for result in __result:
                begin
                    launchs.append(
                        Launch(
                            flight_number←result.get('flight_number'),
                            mission_name←result.get('mission_name'),
                            rocket←result.get('rocket').get('rocket_name'),
                            rocket_type←result.get('rocket').get('rocket_type'),
                            launch_success←result.get('launch_success'),
                            launch_date←result.get('launch_date_utc'),
                            launch_year←result.get('launch_year')
                        )
                    )
                end

            return launchs
        end

    procedure response(self):
        ▷ Obter resposta da requisição

        begin
            return __response
        end
 ```
## 3. Instância Pseudocódigo
```
procedure run(cls):
        
        ▷ Exibe menus para o usuário
```
O menu é exibido, digita-se o valor da opção desejada, 1 por exemplo.
```
        begin
            while:
                begin
                    print menu
                    scan number
                    option ← number
```
A variável recebe o número digitado.
```
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
```
Como 1 é intero e dentro do intervalo 1 e 5, a opção é selecionada.
```
                
                    print Deseja sair da aplicação? (S/N)
                    scan answer 
```
É verificado se deseja sair da aplicação, no caso insere-se "S"
```
                    if answer == S
                        begin
                            __close()
                        end
                end

        end
```
A aplicação é fechada.


## 4. Análise do Código
## 5. Evidências da Execução
```
O que você deseja visualizar?

1) Próximo Lançamento
2) Último Lançamento
3) Próximos Lançamentos
4) Lançamentos Passados
5) Sair

Insira uma opção: 1


Número do Voo: 84
Missão: Starlink 2
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 01/11/2019 às 00:00

Deseja sair da aplicação? (S/N): N

O que você deseja visualizar?

1) Próximo Lançamento
2) Último Lançamento
3) Próximos Lançamentos
4) Lançamentos Passados
5) Sair

Insira uma opção: 2

Número do Voo: 83
Missão: Amos-17
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 06/08/2019 às 22:52
Lançamento realizado com sucesso!

Deseja sair da aplicação? (S/N): N

O que você deseja visualizar?

1) Próximo Lançamento
2) Último Lançamento
3) Próximos Lançamentos
4) Lançamentos Passados
5) Sair

Insira uma opção: 3

Número do Voo: 84
Missão: Starlink 2
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 01/11/2019 às 00:00

----------------------------------------------------------

Número do Voo: 85
Missão: Starlink 3
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 01/11/2019 às 00:00

----------------------------------------------------------

Número do Voo: 86
Missão: JCSat 18 / Kacific 1
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 11/11/2019 às 00:00

----------------------------------------------------------

Número do Voo: 87
Missão: Crew Dragon In Flight Abort Test
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 23/11/2019 às 00:00

----------------------------------------------------------

Número do Voo: 88
Missão: ANASIS-II
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 01/11/2019 às 00:00

----------------------------------------------------------

Número do Voo: 89
Missão: Starlink 4
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 01/12/2019 às 00:00

----------------------------------------------------------

Número do Voo: 90
Missão: CRS-19
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 04/12/2019 às 17:00

----------------------------------------------------------

Número do Voo: 91
Missão: SXM-7
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 01/10/2019 às 00:00

----------------------------------------------------------

Número do Voo: 92
Missão: Starlink 5
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 01/12/2019 às 00:00

----------------------------------------------------------

Número do Voo: 93
Missão: CCtCap Demo Mission 2
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/01/2020 às 00:00

----------------------------------------------------------

Número do Voo: 94
Missão: GPS III SV03 (Columbus)
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/01/2020 às 00:00

----------------------------------------------------------

Número do Voo: 95
Missão: SAOCOM 1B
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/02/2020 às 00:00

----------------------------------------------------------

Número do Voo: 96
Missão: CRS-20
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/03/2020 às 00:00

----------------------------------------------------------

Número do Voo: 97
Missão: Smallsat SSO Rideshare 1 (Mission 1)
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/03/2020 às 00:00

----------------------------------------------------------

Número do Voo: 98
Missão: GPS III SV04
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/05/2020 às 00:00

----------------------------------------------------------

Número do Voo: 99
Missão: USCV-1 (NASA Crew Flight 1)
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/05/2020 às 00:00

----------------------------------------------------------

Número do Voo: 100
Missão: Turksat 5A
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/04/2020 às 00:00

----------------------------------------------------------

Número do Voo: 101
Missão: SXM-8
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/01/2020 às 00:00

----------------------------------------------------------

Número do Voo: 102
Missão: CRS-21
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/08/2020 às 00:00

----------------------------------------------------------

Número do Voo: 103
Missão: GPS SV05
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/09/2020 às 00:00

----------------------------------------------------------

Número do Voo: 104
Missão: Smallsat SSO Rideshare 2 (Mission 9)
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2020
Data de Lançamento (UTC): 01/10/2020 às 00:00

----------------------------------------------------------

Deseja sair da aplicação? (S/N): N

O que você deseja visualizar?

1) Próximo Lançamento
2) Último Lançamento
3) Próximos Lançamentos
4) Lançamentos Passados
5) Sair

Insira uma opção: 4

Número do Voo: 1
Missão: FalconSat
Foguete: Falcon 1 (Merlin A)
Ano de Lançamento: 2006
Data de Lançamento (UTC): 24/03/2006 às 22:30
Lançamento falhou!

----------------------------------------------------------

Número do Voo: 2
Missão: DemoSat
Foguete: Falcon 1 (Merlin A)
Ano de Lançamento: 2007
Data de Lançamento (UTC): 21/03/2007 às 01:10
Lançamento falhou!

----------------------------------------------------------

Número do Voo: 3
Missão: Trailblazer
Foguete: Falcon 1 (Merlin C)
Ano de Lançamento: 2008
Data de Lançamento (UTC): 02/08/2008 às 03:34
Lançamento falhou!

----------------------------------------------------------

Número do Voo: 4
Missão: RatSat
Foguete: Falcon 1 (Merlin C)
Ano de Lançamento: 2008
Data de Lançamento (UTC): 28/09/2008 às 23:15
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 5
Missão: RazakSat
Foguete: Falcon 1 (Merlin C)
Ano de Lançamento: 2009
Data de Lançamento (UTC): 13/07/2009 às 03:35
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 6
Missão: Falcon 9 Test Flight
Foguete: Falcon 9 (v1.0)
Ano de Lançamento: 2010
Data de Lançamento (UTC): 04/06/2010 às 18:45
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 7
Missão: COTS 1
Foguete: Falcon 9 (v1.0)
Ano de Lançamento: 2010
Data de Lançamento (UTC): 08/12/2010 às 15:43
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 8
Missão: COTS 2
Foguete: Falcon 9 (v1.0)
Ano de Lançamento: 2012
Data de Lançamento (UTC): 22/05/2012 às 07:44
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 9
Missão: CRS-1
Foguete: Falcon 9 (v1.0)
Ano de Lançamento: 2012
Data de Lançamento (UTC): 08/10/2012 às 00:35
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 10
Missão: CRS-2
Foguete: Falcon 9 (v1.0)
Ano de Lançamento: 2013
Data de Lançamento (UTC): 01/03/2013 às 19:10
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 11
Missão: CASSIOPE
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2013
Data de Lançamento (UTC): 29/09/2013 às 16:00
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 12
Missão: SES-8
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2013
Data de Lançamento (UTC): 03/12/2013 às 22:41
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 13
Missão: Thaicom 6
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2014
Data de Lançamento (UTC): 06/01/2014 às 18:06
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 14
Missão: CRS-3
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2014
Data de Lançamento (UTC): 18/04/2014 às 19:25
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 15
Missão: OG-2 Mission 1
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2014
Data de Lançamento (UTC): 14/07/2014 às 15:15
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 16
Missão: AsiaSat 8
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2014
Data de Lançamento (UTC): 05/08/2014 às 08:00
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 17
Missão: AsiaSat 6
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2014
Data de Lançamento (UTC): 07/09/2014 às 05:00
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 18
Missão: CRS-4
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2014
Data de Lançamento (UTC): 21/09/2014 às 05:52
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 19
Missão: CRS-5
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2015
Data de Lançamento (UTC): 10/01/2015 às 09:47
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 20
Missão: DSCOVR
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2015
Data de Lançamento (UTC): 11/02/2015 às 23:03
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 21
Missão: ABS-3A / Eutelsat 115W B
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2015
Data de Lançamento (UTC): 02/03/2015 às 03:50
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 22
Missão: CRS-6
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2015
Data de Lançamento (UTC): 14/04/2015 às 20:10
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 23
Missão: TürkmenÄlem 52°E / MonacoSAT
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2015
Data de Lançamento (UTC): 27/04/2015 às 23:03
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 24
Missão: CRS-7
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2015
Data de Lançamento (UTC): 28/06/2015 às 14:21
Lançamento falhou!

----------------------------------------------------------

Número do Voo: 25
Missão: OG-2 Mission 2
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2015
Data de Lançamento (UTC): 22/12/2015 às 01:29
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 26
Missão: Jason 3
Foguete: Falcon 9 (v1.1)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 17/01/2016 às 15:42
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 27
Missão: SES-9
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 04/03/2016 às 23:35
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 28
Missão: CRS-8
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 08/04/2016 às 20:43
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 29
Missão: JCSAT-2B
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 06/05/2016 às 05:21
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 30
Missão: Thaicom 8
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 27/05/2016 às 21:39
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 31
Missão: ABS-2A / Eutelsat 117W B
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 15/06/2016 às 14:29
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 32
Missão: CRS-9
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 18/07/2016 às 04:45
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 33
Missão: JCSAT-16
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 14/08/2016 às 05:26
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 34
Missão: Amos-6
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2016
Data de Lançamento (UTC): 01/09/2016 às 13:07
Lançamento falhou!

----------------------------------------------------------

Número do Voo: 35
Missão: Iridium NEXT Mission 1
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 14/01/2017 às 17:54
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 36
Missão: CRS-10
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 19/02/2017 às 14:39
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 37
Missão: EchoStar 23
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 16/03/2017 às 06:00
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 38
Missão: SES-10
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 30/03/2017 às 22:27
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 39
Missão: NROL-76
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 01/05/2017 às 11:15
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 40
Missão: Inmarsat-5 F4
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 15/05/2017 às 23:21
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 41
Missão: CRS-11
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 03/06/2017 às 21:07
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 42
Missão: BulgariaSat-1
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 23/06/2017 às 19:10
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 43
Missão: Iridium NEXT Mission 2
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 25/06/2017 às 20:25
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 44
Missão: Intelsat 35e
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 05/07/2017 às 23:35
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 45
Missão: CRS-12
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 14/08/2017 às 16:31
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 46
Missão: FormoSat-5
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 24/08/2017 às 18:50
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 47
Missão: Boeing X-37B OTV-5
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 07/09/2017 às 13:50
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 48
Missão: Iridium NEXT Mission 3
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 09/10/2017 às 12:37
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 49
Missão: SES-11 / Echostar 105
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 11/10/2017 às 22:53
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 50
Missão: KoreaSat 5A
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 30/10/2017 às 19:34
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 51
Missão: CRS-13
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 15/12/2017 às 15:36
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 52
Missão: Iridium NEXT Mission 4
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2017
Data de Lançamento (UTC): 23/12/2017 às 01:27
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 53
Missão: ZUMA
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 08/01/2018 às 01:00
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 54
Missão: SES-16 / GovSat-1
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 31/01/2018 às 21:25
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 55
Missão: Falcon Heavy Test Flight
Foguete: Falcon Heavy (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 06/02/2018 às 20:45
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 56
Missão: Paz / Starlink Demo
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 22/02/2018 às 14:17
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 57
Missão: Hispasat 30W-6
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 06/03/2018 às 05:33
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 58
Missão: Iridium NEXT Mission 5
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 30/03/2018 às 14:13
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 59
Missão: CRS-14
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 02/04/2018 às 20:30
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 60
Missão: TESS
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 18/04/2018 às 22:51
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 61
Missão: Bangabandhu-1
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 11/05/2018 às 20:14
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 62
Missão: Iridium NEXT Mission 6
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 22/05/2018 às 19:47
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 63
Missão: SES-12
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 04/06/2018 às 04:45
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 64
Missão: CRS-15
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 29/06/2018 às 09:42
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 65
Missão: Telstar 19V
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 22/07/2018 às 05:50
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 66
Missão: Iridium NEXT Mission 7
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 25/07/2018 às 11:39
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 67
Missão: Merah Putih
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 07/08/2018 às 05:18
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 68
Missão: Telstar 18V
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 10/09/2018 às 04:45
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 69
Missão: SAOCOM 1A
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 08/10/2018 às 02:22
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 70
Missão: Es’hail 2
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 15/11/2018 às 20:46
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 71
Missão: SSO-A
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 03/12/2018 às 18:34
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 72
Missão: CRS-16
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 05/12/2018 às 18:16
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 73
Missão: GPS III SV01
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2018
Data de Lançamento (UTC): 23/12/2018 às 13:51
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 74
Missão: Iridium NEXT Mission 8
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 11/01/2019 às 15:31
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 75
Missão: Nusantara Satu (PSN-6) / S5 / Beresheet
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 22/02/2019 às 01:45
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 76
Missão: CCtCap Demo Mission 1
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 02/03/2019 às 07:45
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 77
Missão: ArabSat 6A
Foguete: Falcon Heavy (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 11/04/2019 às 22:35
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 78
Missão: CRS-17
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 04/05/2019 às 06:48
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 79
Missão: Starlink 1 (v0.9)
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 24/05/2019 às 02:30
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 80
Missão: RADARSAT Constellation
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 12/06/2019 às 14:17
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 81
Missão: STP-2
Foguete: Falcon Heavy (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 25/06/2019 às 03:30
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 82
Missão: CRS-18
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 25/07/2019 às 22:01
Lançamento realizado com sucesso!

----------------------------------------------------------

Número do Voo: 83
Missão: Amos-17
Foguete: Falcon 9 (FT)
Ano de Lançamento: 2019
Data de Lançamento (UTC): 06/08/2019 às 22:52
Lançamento realizado com sucesso!

----------------------------------------------------------

Deseja sair da aplicação? (S/N): N



O que você deseja visualizar?

1) Próximo Lançamento
2) Último Lançamento
3) Próximos Lançamentos
4) Lançamentos Passados
5) Sair

Insira uma opção: 5
Finalizando o programa...
```




## Referências

- FERREIRA, Bruno. UMA TÉCNICA PARA VALIDAÇÃO DE PROCESSOS DE DESENVOLVIMENTO DE SOFTWARE. Belo Horizonte, p.60-61, fev. 2008.

-  MYERS, Glenford J.. The Art of Software Testing. p.22-28.
