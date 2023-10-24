# NASA Astronomy Picture of the Day (APOD) Viewer

Este é um simples script Python que utiliza a API da NASA para acessar a "Astronomy Picture of the Day" (APOD) e exibir a imagem do dia em seu navegador. A APOD é uma coleção de imagens astronômicas incríveis, acompanhadas por descrições escritas por astrônomos profissionais.

<img src="Foto da NASA.png"/>

### Pré-requisitos
Antes de executar este código, certifique-se de que você tenha o Python instalado em seu sistema. Além disso, você precisará de uma API Key da NASA para acessar os dados.

### Obtendo uma API Key da NASA
Acesse NASA API Key para criar uma conta e obter sua chave de API gratuita.

### Como Usar
Abra um terminal ou prompt de comando.

Navegue até o diretório onde o seu código está localizado.

Execute o código Python:

```
python seu_codigo.py
```

### O código faz o seguinte:

- Faz uma solicitação à API da NASA com sua chave de API.
- Define a qualidade da imagem como alta ("hd=True").
- Especifica a data da imagem (no exemplo, está configurada para '2023-10-03', mas você pode alterá-la conforme desejado).
- Obtém a resposta da API e extrai os dados em formato JSON.
- Abre o URL da imagem em seu navegador padrão.
- Você verá a "Astronomy Picture of the Day" da NASA exibida em seu navegador.

#### Nota
Este script é uma maneira simples de acessar e visualizar a imagem astronômica do dia fornecida pela NASA. Lembre-se de que as imagens da APOD são atualizadas diariamente, portanto, você verá uma nova imagem a cada dia. Certifique-se de manter sua chave de API segura e use-a de acordo com os termos de serviço da NASA. Este código é apenas um exemplo e pode ser estendido para incluir funcionalidades adicionais, como salvar as imagens em seu computador ou automatizar o processo de busca da imagem do dia.
