const topMenu = document.getElementById('top-menu')
console.log('log ~ topMenu:', topMenu)
const toggleTopMenuIcon = document.getElementById('toggle-top-menu-icon')
console.log('log ~ toggleTopMenuIcon:', toggleTopMenuIcon)

document.addEventListener('click', (e) => {
  if (toggleTopMenuIcon.contains(e.target)) {
    // Click to toggle top menu icon
    topMenu.classList.toggle('hidden')
    topMenu.classList.toggle('topmenu-expanded')
  } else {
    // Click Outside from Toggle top menu icon
    if (topMenu.classList.contains('topmenu-expanded')) {
      topMenu.classList.remove('topmenu-expanded')
      topMenu.classList.add('hidden')
    }
  }
})
