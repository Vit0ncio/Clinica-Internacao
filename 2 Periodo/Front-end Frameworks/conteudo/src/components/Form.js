import { useState } from "react";

function Form(){
    
    function cadastroUsuario(e){
        e.preventDefault()//Impede o comportamento padrão do formulário de recarregar a página
        console.log('Cadastrou Usuaário!')
        console.log(`Usuário ${nome} foi cadastrado com a senha ${password}`)
    }
//  Essas duas linhas criam estados (states) 
//  no React usando o hook useState, servindo
//  para armazenar e atualizar os valores digitados 
//  nos campos de nome e senha do seu formulário em tempo real.
    const [nome, setName] = useState()
    const [password, setPassword] = useState()
  

    return (
        <div>
            <h1>Meu Cadastro</h1>
            <form onSubmit = {cadastroUsuario}>
                <div>
                    <label htmlFor = 'name'>Nome:</label>
                    <input type='text' id='name' name='name' placeholder='Digite o seu nome'
                        onChange={(e) => setName(e.target.value)}/>
                </div>
                
                <div>
                    <label htmlFor = 'password'>Senha:</label>
                    <input type='password' id='password'name='password' placeholder='Digite sua senha'
                        onChange={(e) => setPassword(e.target.value)}//pega o valor e atualiza o estado do password
                        
                        />
                </div>

                <div>
                    <input type='submit' placeholder='Cadastrar'/>
                </div>
            </form>
        </div>
    )
}

export default Form