let cardAnimation = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {entry.target.classList.add('card-animation') }
    })
}, {
    threshold: .3
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

