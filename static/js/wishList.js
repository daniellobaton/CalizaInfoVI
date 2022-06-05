let updateWishList = document.getElementsByClassName('update-wish-list');
let deleteWishList = document.getElementsByClassName('delete-wish-list');

for(let i = 0; i < deleteWishList.length; i++){

    deleteWishList[i].addEventListener('click', function() {

        let productId = this.dataset.productwishlist;

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


for(let i = 0; i < updateWishList.length; i++){

    updateWishList[i].addEventListener('click', function(){

        let productId = this.dataset.productwishlist;
        let action = this.dataset.actionwishlist;

        console.log('product id: ', productId);
        console.log('action: ', action);
        
        if(user !== 'AnonymousUser') {

            update(productId, action);

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


function update(productId, action){

    var url = '/update_wishList/';

    console.log('product id: ', productId);
    console.log('action: ', action);

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