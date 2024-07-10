Localização de Itens em Armários
Este projeto consiste em um aplicativo desenvolvido em Python utilizando Tkinter para a interface gráfica e SQLite para armazenamento de dados. O objetivo principal é permitir aos usuários localizar itens específicos dentro de armários, usando uma interface intuitiva e fácil de usar.

Funcionalidades Principais
Adicionar Itens: Permite adicionar novos itens especificando seu nome, o armário onde está localizado e a coluna correspondente.

Pesquisar Itens: Permite buscar um item pelo seu nome e exibe o armário e a coluna onde ele está armazenado, caso encontrado.

Instalação e Execução
Para executar o projeto localmente, siga estas instruções:

Clone o Repositório
git clone https://github.com/miguellima15/localizacao-itens-armarios.git
Instale as Dependências:
pip install -r requirements.txt

Executar o Programa:
Via Código Python: Execute o programa diretamente usando Python:

python main.py
Via Executável (Windows): Se preferir executar o programa como um arquivo executável (.exe), navegue até a pasta dist onde o arquivo foi gerado pelo PyInstaller e execute:
./main.exe
Substitua nome-do-executavel pelo nome exato do arquivo executável gerado pelo PyInstaller.

Via Executável (Linux/macOS): Se estiver usando Linux ou macOS, dê permissão de execução ao arquivo e execute diretamente:
chmod +x nome-do-executavel
./main.exe

Estrutura do Projeto
main.py: Contém a lógica principal do programa.
banco/armarios.db: Banco de dados SQLite para armazenamento dos itens nos armários.
imagem/download.png: Imagem utilizada na interface gráfica para o logo do aplicativo.
Contribuição
Contribuições são bem-vindas! Para reportar bugs, sugestões de melhorias ou enviar novas funcionalidades, por favor abra uma issue ou envie um pull request.

Licença
Este projeto está licenciado sob a Licença MIT.

Esta descrição agora inclui instruções claras sobre como executar o programa tanto via código Python quanto usando o arquivo executável gerado pelo PyInstaller, adaptado para diferentes sistemas operacionais.
