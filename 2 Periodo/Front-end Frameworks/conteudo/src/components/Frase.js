import styles from "./Frase.module.css";

function Frase(){
  return(
        <div className={styles.fraseContainer} >
            <p className={styles.fraseContent}> Usando um componente frase </p>
        </div>
    )

}
export default Frase;