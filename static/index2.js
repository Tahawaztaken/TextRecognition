window.addEventListener("load", () =>{
    console.log("START")
    const canvas = document.querySelector("#canvas");
    const context = canvas.getContext("2d");

    //variables
    let painting = false

    function startDraw(e){
        painting = true
        draw(e)
    }
    function draw(e){
        if(!painting) return;
        context.lineWidth = 10
        context.lineCap = 'round'

        context.lineTo(e.clientX, e.clientY)
        context.stroke()
        context.beginPath()
        context.moveTo(e.clientX, e.clientY)

    }
    function finishDraw(){
        painting = false
        context.beginPath()
    }

    //EventListeners
    canvas.addEventListener('mousedown', startDraw)
    canvas.addEventListener('mouseup', finishDraw)
    canvas.addEventListener('mousemove', draw)
    
})