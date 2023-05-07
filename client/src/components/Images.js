import Image from "./Image"

function Images({images,noContent}){

    if(noContent){
        return <div><p>No Images.  Please check back later</p></div>
    }
    return (
        <div className="images-div">
            {images.map(image=><Image image={image} />)}
        </div>
    )
}
 export default Images