let updateBtns = document.getElementsByClassName('update-wish-list');
let deleteBtns = document.getElementsByClassName('delete-wish-list');

for(let i = 0; i < deleteBtns.length; i++){

    deleteBtns[i].addEventListener('click', function() {

        let productId = this.dataset.product;

        if(user){

            deleteWishListItem(productId);

        }

    });

}

function deleteWishListItem(productId){

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
    .then(() => {
        location.reload();
    })

}


for(let i = 0; i < updateBtns.length; i++){

    updateBtns[i].addEventListener('click', function(){

        let productId = this.dataset.product;
        let action = this.dataset.action;

        // console.log('productId: ', productId, 'action: ', action);

        // console.log('User: ', user);
        
        if(user) {

            updateUserOrder(productId, action);

        }

    })

}

// function addCookieItem(productId, action){

//     console.log('Not logged in...');

//     if (action == 'add'){
        
//         if (cart[productId] == undefined) {
            
//             cart[productId] = {'quantity': 1};

//         }else{

//             cart[productId]['quantity'] += 1;

//         }
    
//     }

//     if(action == 'remove'){

//         cart[productId]['quantity'] -= 1;

//         if(cart[productId]['quantity'] <= 0){

//             console.log('Remove item');

//             delete cart[productId];

//         }

//     }

//     console.log('Cart: ', cart);

//     document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";

//     location.reload();
// }


function updateUserOrder(productId, action){

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
    .then(() =>{
        location.reload();
    })
}