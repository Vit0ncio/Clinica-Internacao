import Button from "./Button";

function EventoSomar() {
  
  function eventoSomar() {
    const a = 5;
    const b = 10;
    console.log(`O resultado da soma é: ${a + b}`);
  }

  return (
    <div>
      <p>Clique para disparar o evento de soma</p>
      <Button event={eventoSomar} text="Somar" />
    </div>
  );
}

export default EventoSomar;