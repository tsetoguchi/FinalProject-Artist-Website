document.addEventListener('DOMContentLoaded', () => {

    // Disable volume fader
    document.querySelector('#vol-control').disabled = true;
    document.querySelector('#vol-control').hidden = true;

    const volControl = document.querySelector('#vol-control');
          volControl.style.animationPlayState  = 'paused';

    if (localStorage.getItem("volume") !== null) {
        var fader = document.querySelector("#vol-control");
        var volume = localStorage.getItem('volume');
        fader.input = volume;
    }

            // Flutter image click
            var image= document.querySelector('#flutter');

            image.onclick = function() {
            volControl.style.animationPlayState  = 'running';
            document.querySelector('#vol-control').hidden = false;
            var id = this.id;
            document.querySelector(`.${id}Aud`).play();
        };

            // Wont Let Go image click
            var image= document.querySelector('#wontletgo');

            image.onclick = function() {
            volControl.style.animationPlayState  = 'running';
            document.querySelector('#vol-control').hidden = false;
            var id = this.id;
            console.log(id)
            document.querySelector(`.${id}Aud`).play();
        };

            // Home image click
            var image= document.querySelector('#home');

            image.onclick = function() {
            volControl.style.animationPlayState  = 'running';
            document.querySelector('#vol-control').hidden = false;
            var id = this.id;
            console.log(id)
            document.querySelector(`.${id}Aud`).play();
        };

            // Away image click
            var image= document.querySelector('#away');

            image.onclick = function() {
            volControl.style.animationPlayState  = 'running';
            document.querySelector('#vol-control').hidden = false;
            var id = this.id;
            document.querySelector(`.${id}Aud`).play();
        };

            var audio = document.querySelectorAll("audio");

            audio.forEach((audio) => {
                audio.onplaying = function() {
                document.querySelector('#vol-control').disabled = false;
            };
        });

});



function SetVolume(val)
    {
        var players = document.querySelectorAll("audio");

        //loop all players with forEach and arrow function
        players.forEach((player) => {
            player.volume = val/100;
            localStorage.setItem('volume', player.volume);
        });
    }
