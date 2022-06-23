document.querySelector(document).ready(function () {
  var trigger = document.querySelector('.hamburger'),
      overlay = document.querySelector('.overlay'),
     isClosed = false;

    trigger.click(function () {
      hamburger_cross();      
    });

    function hamburger_cross() {

      if (isClosed == true) {          
        overlay.hide();
        trigger.classList.remove('is-open');
        trigger.classList.add('is-closed');
        isClosed = false;
      } else {   
        overlay.show();
        trigger.classList.remove('is-closed');
        trigger.classList.add('is-open');
        isClosed = true;
      }
  }
  
  document.querySelector('[data-toggle="offcanvas"]').click(function () {
        document.querySelector('#wrapper').classList.toggle('toggled');
  });  
});