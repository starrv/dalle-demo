import {useState} from 'react'

function Form({URL,setImages,images}){

    const [prompt,setPrompt]=useState("")

    function handlePrompt(e){
        setPrompt(e.target.value)
    }

    async function handleSubmit(e){
        e.preventDefault()
        const dialog=document.querySelector("#dialog-box")
        dialog.showModal()
        const resp=await fetch(URL,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                "prompt":prompt
            })
        })
        if(resp.ok){
            const data=await resp.json()
            setImages([...images,...data])
            
            dialog.close()
        }
        else{
            console.log(await resp.json())
            dialog.style.color="red"
            dialog.textContent="Error generating Image"
            setTimeout(()=>{
                dialog.close()
                dialog.style.color="green"
            },2000)
        }
    }


    return(
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="prompt">
                    Prompt:
                </label>
                <input type="text" name="prompt" onChange={handlePrompt} />
            </div>
            <div>
                <input type="submit" value="generate image" />
            </div>
        </form>
    )
}

export default Form