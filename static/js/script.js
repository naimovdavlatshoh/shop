
let handleToggle = () => {
    document.querySelector('.bars').classList.toggle('active')
    document.querySelector('.accaunt-navigator-hidden-container').classList.toggle('active')
    document.querySelector('.accaunt-navigator-hidden').classList.toggle('active')
}

// Slider 

let slider_wrapper = document.querySelectorAll('.slider-wrapper')

let elements = []

slider_wrapper.forEach((wrapper, index)=> {
    let slider = wrapper.querySelectorAll('.slider')
    wrapper.setAttribute('data-id', index + 1)

    let obj = {}
    obj['counter'] = 0
    obj['sliderCounter'] = 0
    obj['id'] = index + 1

    elements.unshift(obj)
   
    for(let item of slider){
        item.style.transform = `translateX(${elements[0].counter}%)`
        elements[0].counter = elements[0].counter + 100   

        let status = false

        // let start = ''
        // let finish = ''

        // item.addEventListener('mousedown', (e)=> {
        //     status = true
        //     start = e.clientX 
        // })

        // item.addEventListener('mouseup', (e)=> {
             
        //     finish = e.clientX

        //     if (start < finish ){
        //         leftArrow()
        //         console.log('left')
        //     } else {
        //         rightArrow()
        //         console.log('right')
        //     }
  
        // })
    }

    let leftArrow = () => {
        // Wrapper Id
        let id = Number(wrapper.getAttribute('data-id'))
        // Array Id
        let elementId = elements.filter((e)=> e.id == id)

    
        if (id == elementId[0].id){
            if(elements[id - 1].sliderCounter == 0 || elements[id - 1].sliderCounter  == 1){
                for(let item of slider){
    
                    let first = item.style.transform.indexOf('(') + 1
                    let last = item.style.transform.indexOf('%')
                    let size = Number(item.style.transform.slice(first, last))
            
                   item.style.transform = `translateX(${size - ((slider.length - 1) * 100)}%)`
                }
                elements[id - 1].sliderCounter  -= 1
                if(elements[id - 1].sliderCounter  == -1 || elements[id - 1].sliderCounter  == 0){
                  elements[id - 1].sliderCounter  = 3
                }
               
               } else {
                for(let item of slider){
                    
                    let first = item.style.transform.indexOf('(') + 1
                    let last = item.style.transform.indexOf('%')
                    let size = Number(item.style.transform.slice(first, last))
            
                    item.style.transform = `translateX(${size + 100}%)`
                }
           
                elements[id - 1].sliderCounter  -= 1
                
                
            } 
     
        }
    }

    let rightArrow = () => {
        // Wrapper Id
        let id = Number(wrapper.getAttribute('data-id'))
        // Array Id
        let elementId = elements.filter((e)=> e.id == id)
        

        if (id == elementId[0].id) {
            if(elements[id - 1].sliderCounter  == 0){
                elements[id - 1].sliderCounter  += 1

                

            }
        
            if(elements[id - 1].sliderCounter  == 3 || elements[id - 1].sliderCounter  == 0){
                elements[id - 1].sliderCounter  = 1
                for(let item of slider){
                    
                    let first = item.style.transform.indexOf('(') + 1
                    let last = item.style.transform.indexOf('%')
                    let size = Number(item.style.transform.slice(first, last))
        
                    item.style.transform = `translateX(${size + ((slider.length - 1) * 100)}%)`
                }
                
            
            } else {
                for(let item of slider){
                    
                    let first = item.style.transform.indexOf('(') + 1
                    let last = item.style.transform.indexOf('%')
                    let size = Number(item.style.transform.slice(first, last))
        
                    item.style.transform = `translateX(${size - 100}%)`
                }
                elements[id - 1].sliderCounter  += 1

           
            }
           
        }
    }

    wrapper.querySelector('.left-arrow').addEventListener('click', leftArrow )

    wrapper.querySelector('.right-arrow').addEventListener('click', rightArrow)
})


let openModal = () => {
    document.querySelector('.modal-container').classList.toggle('d-block')
    console.log(document.querySelector('.modal-container'))
}




const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");




modal_btn = document.querySelector('.modal_btn')
modal_ = document.querySelector('.modal_')
close_btn = document.querySelector('.close_btn')

modal_btn.addEventListener('click', ()=>{
    modal_.classList.remove('d-none')
   
})


close_btn.addEventListener('click', ()=>{
    modal_.classList.add('d-none')
})

