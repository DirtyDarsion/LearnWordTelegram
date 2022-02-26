// Animations

let cardAnimation = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {entry.target.classList.add('card-animation') }
    })
}, {
    threshold: .1
})

for (let i of document.querySelectorAll('.products .card')) (
    cardAnimation.observe(i)
)


let edgeAnimation = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {entry.target.classList.add('edges-animation') }
    })
}, {
    threshold: .3
})

for (let i of document.querySelectorAll('.edges')) (
    edgeAnimation.observe(i)
)



// Window contacts

setTimeout(
    'show_notify()',
    3000
);

function show_notify() {
    document.querySelector('.notify-start').hidden=false;
}


for (let i of document.querySelectorAll('.openContacts')) {
    i.onclick = function() {
        document.querySelector('.contacts-window').hidden=false;
        document.querySelector('.dark-background').hidden=false;
    };
}

document.querySelector('.close-notify').onclick = function () {
    document.querySelector('.notify-start').hidden=true;
};

document.querySelector('.closeContacts').onclick = function() {
    document.querySelector('.contacts-window').hidden=true;
    document.querySelector('.dark-background').hidden=true;
};