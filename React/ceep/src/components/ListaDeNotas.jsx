import React, { Component } from "react";
import { CardNota } from "./CardNota/CardNota";
import "./CardNota/CardNotaEstilo.css"

export class ListaDeNotas extends Component {  
    render(){
        return( 
        <ul className="lista-notas"> 
            {this.props.notas.map((nota, index) => {
            return (
                <li key={index}>                    
                    <CardNota titulo={nota.titulo} texto={nota.texto} />
                </li>
            );
        })} </ul>);
    }
  }