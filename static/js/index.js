
$(document).ready(function() {
    $('.category').select2();
});


$(document).ready(function() {
    $('.colors').select2();
});

let codify = () => {


    return({
        createModal: (name) => {
            let btns = document.querySelectorAll(`.${name}`)
            let modal = document.querySelector(`#${name}`)

            for(let btn of btns){
                btn.addEventListener('click', ()=> {
                    modal.classList.toggle('d-none')
                })
            }
            
        },
       
    })
}


if(document.querySelector('.cart_price') !== null){
    let cart_items = document.querySelectorAll('.cart_price')
    let cart_total = 0
    
    for(let item of cart_items){
    
        let parent = item.parentElement.parentElement
        let quantity = Number(parent.querySelector('.input').value)
        let result = Number(item.innerHTML) * quantity
    
        cart_total += result
    }
    
    document.querySelector('.cart_total').innerHTML = cart_total 
    document.querySelector('.hidden_total').value = cart_total 
    
}





let memory_boxes = document.querySelectorAll('.memory_box')

for(let box of memory_boxes){
   
    box.addEventListener('click', ()=> {
        box.classList.add('active')
        console.log('ok')
     
    })
}





if(document.querySelector('.addProductColor') !== null){
    let addProductColor = document.querySelector('.addProductColor')
    let addProductColorContainer = document.querySelector('.addProductColorContainer')
    
    addProductColor.addEventListener('click', ()=> {
    
        if(addProductColor.innerHTML == 'Отменить'){
            addProductColorContainer.classList.add('d-none')
            addProductColor.className = 'btn btn-green rounded-1 addProductColor'
            addProductColor.innerHTML = 'Добавить цвет' 
        } else {
            addProductColorContainer.classList.remove('d-none')
            addProductColor.className = 'btn btn-grey rounded-1 addProductColor'
            addProductColor.innerHTML = 'Отменить'
        }
    
    
    })
    
    
}



if(document.querySelector('.addImage') !== null){
    let addImage = document.querySelector('.addImage')
    let inputFileContainer = document.querySelector('.inputFileContainer')

 


    addImage.addEventListener('click', (e)=> {


       

        let box = document.createElement('div')
        box.className = 'd-flex w-50'

        let input = document.createElement('input')
        input.setAttribute('type', 'file')
        input.setAttribute('name', 'image[]')
        input.className = 'input'

        // let btn = document.createElement('button') 
        // btn.className = 'btn btn-green rounded-1 ml-2'
        // btn.innerHTML = 'Добавить'

        let btnRemove = document.createElement('button') 
        btnRemove.className = 'btn btn-grey rounded-1 ml-2'
        btnRemove.innerHTML = 'Удалить'
        btnRemove.setAttribute('type', 'button')

        btnRemove.addEventListener('click', (e)=> {
            let parent = e.target.parentElement
            inputFileContainer.removeChild(parent)
            
        })

        box.appendChild(input)
        // box.appendChild(btn)
        box.appendChild(btnRemove)
        

        inputFileContainer.appendChild(box)

        if(inputFileContainer.querySelector('.btn-blue').classList.contains('d-none')){
            inputFileContainer.querySelector('.btn-blue').classList.remove('d-none')
        }
})

}

if(document.querySelector('.storageModal') !== null){
    let storageModalBtn = document.querySelectorAll('.storageModal')

    for(let item of storageModalBtn){
        item.addEventListener('click', (e)=> {
            let productId = Number(item.id)
            let modal = document.querySelector('.storageModalContainer')
            modal.classList.toggle('d-none')

            let modalForm = modal.querySelector('.form')
            modalForm.setAttribute('action', `${productId}/`)
        })
    }
}


if(document.querySelector('.modalMain') !== null){
    let btnMain = document.querySelector('.btnMain')

    btnMain.addEventListener('click', (e)=> {

        let target = e.target
        let imageSrc = target.getAttribute('data-img')
        let productId = target.getAttribute('data-id')

        console.log(imageSrc)

        let modal =  document.querySelector('.modalMain')
        modal.classList.remove('d-none')

        let image = modal.querySelector('.w-100')
        let form = modal.querySelector('.form')
        image.setAttribute('src', `${imageSrc}`)
        form.setAttribute('action', `/user/product-image/${productId}/`)

    })
}



if(document.querySelectorAll('.productColorSizeEditBtn') !== null){
    let editBtns = document.querySelectorAll('.productColorSizeEditBtn')

    for(let btn of editBtns){
        btn.addEventListener('click', ()=> {
            btn.parentElement.classList.add('d-none')
            btn.parentElement.parentElement.querySelector('.form_edit').classList.remove('d-none')
        })
    }
}


if(document.querySelectorAll('.productColorSizeCancelBtn') !== null){
    let cancelBtns = document.querySelectorAll('.productColorSizeCancelBtn')

    for(let btn of cancelBtns){
        btn.addEventListener('click', ()=> {
            btn.parentElement.classList.add('d-none')
            btn.parentElement.parentElement.querySelector('.initial_form').classList.remove('d-none')
        })
    }
}

 



$(document).ready( function () {
    $('#myTable').DataTable();
} );



$(document).ready( function () {
    $('#myTable2').DataTable();
} );