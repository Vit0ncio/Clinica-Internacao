import { useState } from "react";
import Button from "./Button";

function EventoSomarUsuario() {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");

  function eventoSomar(e) {
    e.preventDefault();
    const soma = Number(num1) + Number(num2);
    console.log(`O resultado da soma é: ${soma}`);
  }

  return (
    <div>
      <p>Digite dois valores para somar</p>
      <form onSubmit={eventoSomar}>
        <div>
          <label htmlFor="num1">Primeiro número:</label>
          <input type="number" id="num1"  name="num1" placeholder="Digite o 1º número"
            onChange={(e) => setNum1(e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="num2">Segundo número:</label>
          <input type="number"id="num2" name="num2" placeholder="Digite o 2º número"
            onChange={(e) => setNum2(e.target.value)}
          />
        </div>

        <Button text="Somar" />
      </form>
    </div>
  );
}

export default EventoSomarUsuario;
