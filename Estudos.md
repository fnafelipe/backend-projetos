semana 02

    terça-feira

        estudos

            arquivos
                abrir e fechar arquivos usando open(nome, ação, encoding) e close
                with open as arquivo abre e garante que fecha, fica mais bonito visualmente
                r = ler, w = subistitui, a = adiciona, x = cria
                read = transforma todo o texto numa string só
                readline = le uma linha, readlines = lista [cada linha do arquivo]
                write = adiciona ou subistiui dependenodo da ação 'a' ou 'w'
                os.remove(nome do arquivo) = exclui o arquivo
            
            json
                dumps = transforma string python em json
                loads = transforma dict,list,tupla, string, int,float, etc.. python em json
                dump(item, arquivo, indent, ensure_ascii) =
                    junto com with open 'w' ou 'a' pra salvar um json no python
                load(arquivo) = junto com with open 'r' pra carregar um json no python
                json nao aceita aspas simples
        
        projeto

            criei arquivos json pra guardar dicts usuarios e exercicios e tirei eles do codigo principal, agora o projeto tem persistencia dos dados
            adicionei 4 funçoes, 2 de cada pra carregar e salvar exercicios e usuarios
            modifiquei o codigo todo agora, nao existe dicionario global nem pra exerciciso nem pros usuarios, tudo é passado como parametro dentro das funçoes
            troquei usuarios['email'] por usuario pra ficar mais bonito porem precisei modificar o dict usuario agora o email alem de chave do usuario tambem é um par do usuario, fiz isso pra poder printar o email quando precisasse e nao ter que passar um email como parametro das funçoes toda hora so pra isso, tambem refiz o codigo todo pra se adequar a essas mudanças

    quarta

        estudos

            tratamentode exceções
                try = executa um bloco verificando um erro ou nao
                except = executa um bloco se ocorrer um erro, pode criar variso blocos excepts para verificar erros diferentes, Exception as e: e pode ser printado
                else = executa um bloco se o try não der erro sere pra executar so oque é garantido de dar certo
                finally = executa independente de dar erro ou nao, bom pra fechar arquivos
                raise = executa um erro, bom pra garantir excepts quando o python nao conseguri diferenciar tipo, usuario cadastrar com id negativo
            
            tipos de exceções
                value = atribuição errada de valor, exp int(input('string'))
                type = interação entre 2 tipos diferetnes, int + 'string'
                name = variavel nao difinida, exp print(x), sem x no codigo
                zerodivision = divisao por zero, exp int / 0
                key = chave nao existe no dict, exp num = {'dez':10}, num['nove']
                index = indicie nao existe na list, exp list=[1,2,3], print(list[9])
                indentation = indentação incorreta
                exception = exceção base pra todos os erros
        
        projeto
            adcionei trys/excepts no validar idade peso altura porem nao achei nescessario usar valueerror pra todos pq queria msotrar uma mensagem especifica pra cada erro e nao so pra dizer que era numero, porem adicionei na idade na conversao pra int pra ver se ele tinnha tentado botar uma idade decimal e no peso e altura pra ver se o usuario tinha colocado um numero com 2 pontos ou 1 virgula ao nives de ponto
            adicionei no carregamento dos jsons tambem, agora durante o carregamento ele verifica se o json existe e se esta vazio ou corrmpido, se nao existir ele executa uma função que cria um novo arquiv json e retorna {} pro codigo, se estiver vazio ou corrompido ele so retorna {} dict vazio, mensagem em cada situação pra dizer oqeu aconteceu
    
    quinta

        estudos

            refatoracao e boas praticas
                pep8 = guia oficial de estilo do python, padroniza visual e estrutura do codigo
                clean code = principios pra deixar o codigo legivel, facil de manter e dar manutencao
                refatoracao = alterar a estrutura interna do codigo sem mudar o comportamento externo
                dry (dont repeat yourself) = nao repetir codigo, se usou a mesma logica 2x vira funcao
                kiss (keep it simple) = mantenha simples, evitar solucoes mirabolantes pra problemas simples
                single responsibility (srp) = uma funcao deve ter apenas uma unica responsabilidade
                biblioteca icecream = função ic que ajuda a depurar e verificar erros no codigo
        
        projeto
            hoje oque eu fiz mais foi dividir funçoes grandes em varias, as confirmaçoes de email e senha agora ocorrem em funçoes separadas ao inves das mesmas de verificação como antes, no perfil a atualização do historico de peso e altura agora ocorrem em funçoes separadas tambem, calculo de imc aogra tem uma funçao especifica so pra calcular o imc e outra pra atualizar no dict do usuario, treinos a mesma logica e a maioria das outras funçoes tambem foram separadas caso nescessario, isso foi oque cobriu a maior parte do meu tempo, nao fiz ainda a separação dos prints das paginas de menu por que vou fazer na sexta quando aprender rich, ai eu ja deixo bonito e separo em outra função logo, tirando isso tentei ajeitar umas logicas deixar elas mais simplificadas e ajeitar o nome de constantes tambem
    
    sexta

        estudos

            os
                system = executa comandos do terminal,exp 'cls' limpa tela 'dir' mmsotra o diretorio atual
                getcwd = retorna o caminho do diretorio atual
                exists = verifica se existe
                isdir = verifica se é diretorio
                isfile = verifica se é arquivo
                mkdir, rmddir = cria e deleta um direotiro
                listdir = lista o diretorio atual
                remove = deleta arquivo
                path.join = cria o nome de um caminho
                rename = renomeia ou move de lugar um arquivo ou repositorio
                name = nome do sistema peracional atual
            
            rich
                biblioteca pra adicionar cores, fontes, eomjis, tabelas, paineis e etc no python, console serve como um comando nescessario pra todos os outros da biblioteca
                print = adicionar cores estilos e emojis no print
                text = consegue guardar uma string e modificar ela por la
                theme = cria styles e guarda eles pra usar depois
                panel = permite a criação e customização de paineis
                table = mesmo pra tabelas
                prompt = como se fosse um input customizavel
                rule = desenha uma linha no terminal
        
        projeto
            hoje usei mais rich pra fazer os menus mais bonitos, fiz um menuzinho usando panel pra dizer a pagina atual, coloquei textos coloridos indicando as paginas, algumas rules, e tambem fiz tabelas pra mostrar estatisticas e ranking, hoje nao teve muito codigo so mudança visual mesmo, alem disso aproveitei pra terminar de separar algumas unçoes que sobraram ontem, agora nao tem nenhuma unção fazendo 2,3 ou mais coisas ao mesmo tempo, maioria separada e padronizada, os usei pouco no projeto hoje oi mais a pratica mesmo mas amanha vou usar bastante pra azer duas coisas, criar um carregar_pagina que vai esperar um pouco e limpar a tela pra evitar icar um monte de informação alem disso tambem quero usar um pouco dos comandos path ppra fazer o programa uncionar em qualquer computador, sem o usuario ter que modiicar o nome dos diretorios nas funçoes de arquivo, por hoje ofi isso
    
    sabado e domingo

        projeto
            novas alterações
                hoje dediquei o dia so ao projeto, por enquanto no geral fiz: botei mensagens blink red pra erros, bold green pra operações de sucesso, italic yellow para veriicações como mostrar que a idade so pode possuir numeros, bold white para mensagens em destaque, alem disso modifiquei a interface pra que todos os inputs sejam 2 linhas apos o menu com as opções, assim eu consigo printar a mensagem de verificação acima do input atual sem apagar o menu sem querer e sem precisar ficar printando o menu todo novamente, para isso utilizei uma função que volta 1 linha do codigo printa e mensagem de erro e volta pra linha original do input mantendo a interface limpa, criei uma funçao validar_resposta pra veriicar se a opcao de pagina do usuario esta entre as disponiveis, ela recebe o numero da ultima opção da pagina e verifica se a resposta do usuario esta no intervalo (1,ultimo numero), se nao estiver da resposta invalida e pergunta denovo ate o usuario dizer uma repspota que esteja no intervalo ai ela retorna a resposta, da pra usar essa função em qualquer pagina de navegação,

            paginas com interface nova ate agora:
                iniciar, menu entrada, login, sign in, encerrar, menu usuario, perfil, editarpeso, editaraltura, editarnome, IMC, calcularimc, classificarimc, Treinos (menu, adicionar, remover, editar, listar, selecionar exercício), Exercícios (menu, criar, pesquisar por nome, pesquisar por grupo), Estatísticas Individuais, Ranking, Estatísticas Gerais, Configurações, Trocar Senha, Excluir Conta e Logout. TODAS AS PAGINAS FINALIZADASSSS!!!!!!!!!!!!!

            interface paginas de navegação          interface paginas de ação
                -------------------------------         -------------------------------
                |                             |         |                             |
                |           ACADEMIA          |         |           ACADEMIA          |
                |                             |         |                             |
                -------------------------------         -------------------------------

                         NOME DA PAGINA                          NOME DA PAGINA

                -------------------------------         -------------------------------

                         01 escolha 1                           Digite sua ação
                         02 escolha 2
                         03 escolha 3

                -------------------------------

                        Digite sua escolha
