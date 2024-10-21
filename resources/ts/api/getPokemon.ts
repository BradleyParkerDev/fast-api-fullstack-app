import axios from "axios"

export const getPokemon = async () =>{
    const pokemon = localStorage.getItem('pokemon');
    console.log('Checking Pokemon!')

    if(pokemon){
        console.log(`Pokemon in localStorage.`)
        const pokemonData = JSON.parse(pokemon);
        console.log(pokemonData)
    }else{
        console.log(`Pokemon not in localStorage, calling API.`)
        const response = await axios.get("https://pokeapi.co/api/v2/pokemon/")
        const jsonString = JSON.stringify(response);
        localStorage.setItem('pokemon',jsonString)

    }

}