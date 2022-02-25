# API LEADS



<h3 style='color: green'>/POST</h3>

<p>Endpoint: <b>/api/leads</b></p>

Este endpoint com o verbo POST é a rota de cadastro do lead user.

Formato do corpo da requisição:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-17-55.png" />





Caso o usuário seja criado com sucesso a resposta deverá ser a seguinte:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-18-17.png" />



Se o usuário já estiver cadastrado a resposta deverá ser a seguinte:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-25-56.png"/>


Para o cadastro todos os campos devem ser informados. Se faltar um campo no corpo da requisição a seguinte resposta é enviada:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-28-10.png"/>



Os valores dos campos devem ser do tipo string. Tipos diferentes informados geram a seguinte resposta:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-29-36.png"/>



O número de telefone deve estar no formato (YY)-9XXXX-XXXX, sendo o YY o código regional. Informação incorreta produz a seguinte resposta:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-36-01.png"/>
<hr/>

<h3 style='color: purple'>/GET</h3>

<p>Endpoint: <b>/api/leads</b></p>

Este endpoint com o verbo GET é a rota de obtenção da listagem de lead users cadastrados.

A requisição não possui corpo e a resposta é a seguinte:



<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-35-26.png"/>



Se não existirem registros a seguinte mensagem é retornada:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-40-44.png"/>
<hr/>


<h3 style='color: gold'>/PATCH</h3>

<p>Endpoint: <b>/api/leads</b></p>

Este endpoint com o verbo PATCH é a rota de update do número de visitas e o horário do campo "last_visit" é atualizado.

O corpo da requisição é o e-mail do lead user:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-44-42.png"/>


A resposta é a de código 204 e não existe conteúdo na mesma.

Caso o usuário não exista no banco a seguinte resposta é enviada:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-46-34.png"/>
<hr/>


<h3 style='color: red'>/DELETE</h3>

<p>Endpoint: <b>/api/leads</b></p>

Este endpoint com o verbo DELETE é a rota de deleção do lead user.

No corpo da requisição deve constar o e-mail:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-48-38.png"/>



Caso o usuário não exista no banco a seguinte resposta é enviada:

<img src="./public/assets/Captura%20de%20tela%20de%202022-02-25%2010-46-34.png"/>
