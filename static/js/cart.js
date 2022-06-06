let updateBtns = document.getElementsByClassName('update-cart');
let deleteBtns = document.getElementsByClassName('delete-cart');

for(let i = 0; i < deleteBtns.length; i++){

    console.log(deleteBtns);

    deleteBtns[i].addEventListener('click', function(){

        console.log('Boton eliminar clickeado');

        let productId = this.dataset.product;

        if(user === 'AnonymousUser'){

            deleteCookieItem(productId);

        }else{

            deleteCartItem(productId);

        }

    });

}

function deleteCookieItem(productId){

    delete cart[productId];

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";

    location.reload();

}

function deleteCartItem(productId){

    var url = '/delete_items/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId})
    })

    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        console.log('data: ', data);
        location.reload();
    })

}


for(let i = 0; i < updateBtns.length; i++){

    updateBtns[i].addEventListener('click', function(){

        let productId = this.dataset.product;
        let action = this.dataset.action;

        console.log('productId: ', productId, 'action: ', action);

        console.log('User: ', user);
        
        if(user === 'AnonymousUser'){

            addCookieItem(productId, action);

        }else{

            updateUserOrder(productId, action);

        }

    })

}

function addCookieItem(productId, action){

    console.log('Not logged in...');

    if (action == 'add'){
        
        if (cart[productId] == undefined) {
            
            cart[productId] = {'quantity': 1};

        }else{

            cart[productId]['quantity'] += 1;

        }
    
    }

    if(action == 'remove'){

        cart[productId]['quantity'] -= 1;

        if(cart[productId]['quantity'] <= 0){

            console.log('Remove item');

            delete cart[productId];

        }

    }

    console.log('Cart: ', cart);

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";

    location.reload();
}


function updateUserOrder(productId, action){

    console.log('User is logged in');

    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        console.log('data: ', data);
        location.reload();
    })
}
