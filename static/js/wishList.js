let updateWishList = document.getElementsByClassName('update-wish-list');
let deleteWishList = document.getElementsByClassName('delete-wish-list');

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







for(let i = 0; i < deleteWishList.length; i++){

    deleteWishList[i].addEventListener('click', function() {

        let productId = this.dataset.productwishlist;
        let iteration = this.dataset.iteration;

        if(user !== 'AnonymousUser'){

            deleteListItem(productId, iteration);

        }

    });

}

function deleteListItem(productId, iteration){

    var url = '/delete_wishList/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'iteration': iteration})
    })

    .then((response) =>{
        return response.json();
    })
    .then(() => {
        location.reload();
    })

}