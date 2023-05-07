import '../css/App.css';
import Header from "./Header"
import Form from "./Form"
import Images from "./Images"
import {useState,useEffect} from 'react'

function App() {

  const URL="http://127.0.0.1:5555/images"
  const [images,setImages]=useState([])
  const [noContent,setNoContent]=useState(true)

  useEffect(()=>{
    async function fetchData(){
        const resp=await fetch(URL)
        if(resp.ok){
            const data=await resp.json()
            console.log(data)
            if(data.length>0){
                setNoContent(false)
                setImages(data)
            }
        }
    }
    fetchData()
  },[])

  return (
    <div className="App">
      <Header />
      <dialog id="dialog-box">
        <p>
          Loading data....
        </p>
      </dialog>
      <Form URL={URL} setImages={setImages} images={images} />
      <Images URL={URL} images={images} noContent={noContent} />
    </div>
  );
}

export default App;
