$(function(){
    $('.addToCart').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let product = btn.attr('data-id')
            
    
        $.ajax({
            url:url,
            type:'POST',
            data:{product},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                $('.cart_parent').load( ' .cart_child ')
                alert('Продукт добавлен')
            },

            error: (msg)=> {
                console.log(msg)
            }
        })  
        
    })
})




$(function(){
    $('.cartPlus').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let cart_id = btn.attr('data-id')
        let quantity = btn.parent().find('.input').val()
        let input_parent = btn.parent().find('.cart_input_parent')
        
    
        
    
        $.ajax({
            url:url,
            type:'POST',
            data:{cart_id, quantity},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                console.log(data)
                input_parent.load(` .cart_input_child${cart_id} `)

                let cart_items = document.querySelectorAll('.cart_price')
                cart_total = 0

                for(let item of cart_items){

                    let parent = item.parentElement.parentElement
                    let quantity = 0
                    
                    if(item.id == cart_id){
                        quantity = Number(parent.querySelector('.input').value) + 1
                      
                    } else {
                        quantity = Number(parent.querySelector('.input').value)
                    }
                    let result = Number(item.innerHTML) * quantity

                    cart_total += result
                }

          

                document.querySelector('.cart_total').innerHTML = cart_total 
                document.querySelector('.hidden_total').value = cart_total 

                

               
            },

            error: (msg)=> {
                console.log(msg)
            }
        })  
        
    })
})



$(function(){
    $('.cartMinus').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let cart_id = btn.attr('data-id')
        let quantity = btn.parent().find('.input').val()
        let input_parent = btn.parent().find('.cart_input_parent')

        if(quantity == 1){
            btn.parent().parent().parent().remove()
        }
      
        $.ajax({
            url:url,
            type:'POST',
            data:{cart_id, quantity},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                input_parent.load(` .cart_input_child${cart_id} `)
                
                let cart_items = document.querySelectorAll('.cart_price')
                cart_total = 0

                for(let item of cart_items){

                    let parent = item.parentElement.parentElement
                    let quantity = 0
                    
                    if(item.id == cart_id){
                        quantity = Number(parent.querySelector('.input').value) - 1
                      
                    } else {
                        quantity = Number(parent.querySelector('.input').value)
                    }
                    let result = Number(item.innerHTML) * quantity

                    cart_total += result
                }

                console.log(cart_total)

                document.querySelector('.cart_total').innerHTML = cart_total 
                document.querySelector('.hidden_total').value = cart_total 

               
            },

            error: (msg)=> {
                console.log(msg)
            }
        }) 
    
    
         
        
    })
})





// Edit produt color size


$(function(){
    $('.productColorSizeAdd').on('click', function() {
      
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let id = btn.attr('data-id')

        let price = btn.parent().find('.productColorSizePrice')[1]
        let memory = btn.parent().find('.productColorSizeMemory')[1]

      
        price = price.value
        memory = memory.value
      
     
       
        $.ajax({
            url:url,
            type:'POST',
            data:{id,price,memory},
            headers:{
                'X-CSRFToken':token
            },


            success: (data)=>{
                console.log(data)
            },

            error: (msg)=> {
                console.log(msg)
            }
        })  
        
    })
})






$(function(){
    $('.addToFavourite').on('click', function() {
        let btn = $(this)
        let token = $('[name = csrfmiddlewaretoken').val()
        let url = btn.attr('data-url')
        let sizeId = btn.attr('data-id')
        
            
    
        $.ajax({
            url:url,
            type:'POST',
            data:{sizeId},
            headers:{
                'X-CSRFToken':token
            },
            


            success: (data)=>{
                $('.cart_parent').load( ' .cart_child ')
                if(data == 'ok'){
                    btn.removeClass('btn-yellow')
                    btn.addClass('btn-red')

                    btn.html('saved')
                } else {
                    btn.addClass('btn-yellow')
                    btn.removeClass('btn-red')

                    btn.html('Save')
                }
            },

            error: (msg)=> {
                console.log(msg)
            }
        })  
        
    })
})







// Start

$(document).on("click",".productColorSizeEdit",function(){
    let btn = $(this)
    let token = $('[name = csrfmiddlewaretoken').val()
    let url = btn.attr('data-url')
    let id = btn.attr('data-id')
    let price = btn.parent().parent().find('.input').val()

   
    let refreh_parent = btn.parent().parent().parent().find('.refreshParent')
    let refreh_parent2 = btn.parent().parent().parent().find('.refreshParent2')

    let box = btn.parent().parent().parent().find('.memory_box_front')
   
    $.ajax({
        url:url,
        type:'POST',
        data:{id, price},
        headers:{
            'X-CSRFToken':token
        },


        success: (data)=>{
            
            btn.parent().parent().parent().removeClass('active')

            // setTimeout(()=> {
              
            // },2000)
      
            refreh_parent.load(location.href + ` .refreshChild${id}`)
            refreh_parent2.load(location.href + ` .refreshChild2${id}`)

            if(price == '0' || data == '0'){
                box.removeClass('border-green')
                box.addClass('border-red')
            }else{
                box.removeClass('border-red')
                box.addClass('border-green')
            }

            
        },

        error: (msg)=> {
            console.log(msg)
        }
    })  
    
})



$(document).on("click",".btnGalleryRemove",function(){
    let btn = $(this)
    let token = $('[name = csrfmiddlewaretoken').val()
    let url = btn.attr('data-url')
    let imageId = btn.attr('data-imageId')
   
   
    $.ajax({
        url:url,
        type:'POST',
        data:{imageId},
        headers:{
            'X-CSRFToken':token
        },


        success: (data)=>{
            btn.parent().addClass('d-none')
        },

        error: (msg)=> {
            console.log(msg)
        }
    })  
    
})



// Product Color Size


$(document).on("click",".productColorSizeDeleteBtn",function(){
    let btn = $(this)
    let token = $('[name = csrfmiddlewaretoken').val()
    let url = btn.attr('data-url')
    let productId = btn.attr('data-id')
   
   
    $.ajax({
        url:url,
        type:'POST',
        data: {productId},
        headers:{
            'X-CSRFToken':token
        },


        success: (data)=>{
            btn.parent().addClass('d-none')
        },

        error: (msg)=> {
            console.log(msg)
        }
    })  
    
})



$(document).on("click",".productColorSize_edit",function(){
    let btn = $(this)
    let token = $('[name = csrfmiddlewaretoken').val()
    let url = btn.attr('data-url')
    let productId = btn.attr('data-id')
    let price = btn.parent().find('.input_price').val()

    console.log(url)
   
    $.ajax({
        url:url,
        type:'POST',
        data: {productId, price},
        headers:{
            'X-CSRFToken':token
        },


        success: (data)=>{
            btn.parent().parent().find('.refreshPrice').val(data)
            btn.parent().addClass('d-none')
            btn.parent().parent().find('.initial_form').removeClass('d-none')
        },

        error: (msg)=> {
            console.log(msg)
        }
    })  
    
})
