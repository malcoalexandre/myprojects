 let productIndex = 0

 let productInfos = document.querySelectorAll('.product-info')

 setTimeout(() => {
     productInfos[productIndex].classList.add('active')
 }, 200);

 // SLIDE 

 let isSliding = false

 slide = () => {
    if (isSliding) return

    isSliding = true

    let currProduct = document.querySelector('.product-info.active')
    currProduct.classList.remove('active')

    productIndex = productIndex + 1 > productInfos.length -1 ? 0 : productIndex + 1
    productInfos[productIndex].classList.add('active')
}

//IMAGE SLIDER

const slider = document.querySelector('.slider');
const sliderImgs = document.querySelectorAll('.slider img');

// BUTTON
const nextBtn = document.querySelector('.slide-control');
const prevBtn = document.querySelector('.slide-control-2');
// COUNTER      

// vamos usar um counter para monitorar em qual imagem estamos 

let counter = 0; // vamos começar na primeira imagem
const size = sliderImgs[0].clientWidth; // so we know how much we need to slide (original width)

slider.style.transform = 'translateX(' + (size * counter) + 'px)';

// button listeners

nextBtn.addEventListener('click', () =>{
    slider.style.transition = 'transform 0.4s ease-in-out';
    counter++;
    slider.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

prevBtn.addEventListener('click', () =>{
    slider.style.transition = 'transform 0.4s ease-in-out';
    counter--;
    slider.style.transform = 'translateX(' + (-size * counter) + 'px)';
});






















//     // IMAGE SLIDE

//     let listItems = document.querySelectorAll('.slide')

//     let slider = document.querySelector('.slider')

//     let reverseItems = Array.from(listItems).slice().reverse()

//     left = reverseItems[0].offsetLeft + 'px'
//     height = reverseItems[0].offsetHeight + 'px'
//     width = reverseItems[0].offsetWidth + 'px'
//     zIndex = reverseItems[0].style.zIndex

//     reverseItems.forEach((el, index) => {
//         if (index < listItems.length - 1) {
//             el.style.left = reverseItems[index + 1].offsetLeft + 'px'
//             el.style.height = reverseItems[index + 1].offsetHeight + 'px'
//             el.style.width = reverseItems[index + 1].offsetWidth + 'px'
//             el.style.zIndex = reverseItems[index + 1].style.zIndex
//             el.style.transform = 'unset'
//             el.style.opacity = 1

//         }
//     })


//     setTimeout(() => {
//         isSliding = false
//     }, 1000);
// }

// let slideControl = document.querySelector('slide-control')

// slideControl.onclick = () => {
//     slide()

// }
