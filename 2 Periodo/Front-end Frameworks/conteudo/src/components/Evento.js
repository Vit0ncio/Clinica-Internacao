
function Evento() {
 
   function meuEvento() {
    console.log(`Ativando primeiro evento!`);
  }

  return (
    <div>
      <h1>Clique para disparar o evento</h1>
      <button onClick={meuEvento}>Ativar Evento</button> 
      
    </div>

  );
}
export default Evento;