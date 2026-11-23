import Button from "./Button";

function Evento2() {
   function meuEvento() {
    console.log(`Ativando primeiro evento!`);
  }

  function segundoEvento() {
    console.log(`Ativando segundo evento!`);
  }

    function terceiroEvento() {
    console.log(`Ativando terceiro evento!`);
  }

  return (

      <div>
            <p>Clique para disparar o evento</p>
            <Button event={meuEvento} text ='Primeiro Evento' />
            <Button event={segundoEvento} text ='Segundo Evento' />
            <Button event={terceiroEvento} text ='Terceiro Evento' />
        </div>
  )  }
    export default Evento2;