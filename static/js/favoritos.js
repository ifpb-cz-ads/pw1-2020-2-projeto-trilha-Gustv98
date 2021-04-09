var updateBtns = document.getElementsByClassName('update-favorites')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var eventoTitulo = this.dataset.filmes
        var action = this.dataset.action
        console.log('eventoTitulo:', eventoTitulo, 'action:', action)
    })
}