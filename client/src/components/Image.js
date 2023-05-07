function Image({image}){
    const image_data="data:image/png;base64,"+image.image
    return(
        <div key={image.id}>
            <img src={image_data} alt="image" />
        </div>
    )
}

export default Image