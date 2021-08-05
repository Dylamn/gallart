const toggleMenu = document.querySelector('.toggle-nav')
const navigation = document.querySelector('.navigation')

toggleMenu.addEventListener('click', (ev) => {
  ev.target.classList.toggle('active')
  navigation.classList.toggle('active')
})
