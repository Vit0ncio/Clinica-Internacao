function SayMyName(props) {
  return (
    <div>
      <h1>Fala aí {props.nome}, tudo bem?</h1>
      <h1>Você tem idade é {props.idade}?</h1>

    </div>
  );
}
export default SayMyName;