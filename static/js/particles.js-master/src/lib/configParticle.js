/* -----------------------------------------------
/* How to use? : Check the GitHub README
/* ----------------------------------------------- */

/* To load a config file (particles.json) you need to host this demo (MAMP/WAMP/local)... */
/*
particlesJS.load('particles-js', 'particles.json', function() {
  console.log('particles.js loaded - callback');
});
*/

/* Otherwise just put the config content (json): */

particlesJS('particles-js',{

  "particles": {
    "number": {
      "value": 547,
      "density": {
        "enable": true,
        "value_area": 1987.297854546357
      }
    },
    "color": {
      "value": "#bb9772"
    },
    "shape": {
      "type": "edge",
      "stroke": {
        "width": 4,
        "color": "#091f35"
      },
      "polygon": {
        "nb_sides": 3
      },
      "image": {
        "src": "img/github.svg",
        "width": 100,
        "height": 100
      }
    },
    "opacity": {
      "value": 0.5,
      "random": false,
      "anim": {
        "enable": false,
        "speed": 1,
        "opacity_min": 0.1,
        "sync": false
      }
    },
    "size": {
      "value": 1,
      "random": true,
      "anim": {
        "enable": false,
        "speed": 40,
        "size_min": 0.1,
        "sync": false
      }
    },
    "line_linked": {
      "enable": true,
      "distance": 150,
      "color": "#091f35",
      "opacity": 0.4,
      "width": 1
    },
    "move": {
      "enable": true,
      "speed": 18.216897000008274,
      "direction": "none",
      "random": false,
      "straight": false,
      "out_mode": "bounce",
      "bounce": false,
      "attract": {
        "enable": false,
        "rotateX": 1573.2774681825326,
        "rotateY": 1200
      }
    }
  },
  "interactivity": {
    "detect_on": "canvas",
    "events": {
      "onhover": {
        "enable": true,
        "mode": "bubble"
      },
      "onclick": {
        "enable": true,
        "mode": "push"
      },
      "resize": true
    },
    "modes": {
      "grab": {
        "distance": 1019.4406920450066,
        "line_linked": {
          "opacity": 1
        }
      },
      "bubble": {
        "distance": 239.12806356611264,
        "size": 29.36660429759278,
        "duration": 1.594187090440751,
        "opacity": 8,
        "speed": 3
      },
      "repulse": {
        "distance": 79.91497047141839,
        "duration": 0.4
      },
      "push": {
        "particles_nb": 4
      },
      "remove": {
        "particles_nb": 2
      }
    }
  },
  "retina_detect": false


  }

);
