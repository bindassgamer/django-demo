// Add animation when profile section enters the viewport
document.addEventListener('DOMContentLoaded', function() {
    var profileSection = document.querySelector('.profile');
    var isInViewport = function(elem) {
      var bounding = elem.getBoundingClientRect();
      return (
        bounding.top >= 0 &&
        bounding.left >= 0 &&
        bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
      );
    };
  
    var addAnimation = function() {
      if (isInViewport(profileSection)) {
        profileSection.classList.add('slide-in');
        window.removeEventListener('scroll', addAnimation);
      }
    };
  
    window.addEventListener('scroll', addAnimation);
    addAnimation();
  });
  