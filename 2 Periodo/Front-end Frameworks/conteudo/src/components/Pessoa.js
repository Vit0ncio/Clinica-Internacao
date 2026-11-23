/* function Pessoa(props) {
 return (
    <div>
        <h1>Nome: {props.nome}</h1>
      <p>Idade: {props.idade}</p>
       <p>Profissão: {props.profissao}</p>
    </div>
   );
 }
 export default Pessoa; */

function Pessoa({ nome, idade, profissao, email }) {
  return (
    <div>
      <h1>Nome: {nome}</h1>
      <h1>Idade: {idade}</h1>
      <h1>Profissão: {profissao}</h1>
      <h1>Email: {email}</h1>
    </div>
  );
} 
export default Pessoa;