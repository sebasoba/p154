<html>
<head>
<script src="https://aframe.io/releases/0.6.0/aframe.min.js"> </script> 
</head>
<body>

AFRAME.registerComponent("base",{
    init: function () {
        for (var i = 1; i <= 10; i++) {
            const id = 'coin$(i)';

            const posX = Math.random() * 100 + -50
            const posY = Math.random() * 100 + -50
            const posZ = Math.random() * 100 + -50

            const position = (x: posX,y: posY,z: posZ)
            this.createCoins(id,position);
        
        }
    }
    createCoins: function (id,position) {
        const treasureEntity = document.querySelector("#treasureCoins");
        var coinEl = document.createElement("a-entity");

        coinEl.setAttribute("id",id);
        coinEl.setAttribute("position",position);
        coinEl.setAttribute("material","color","#ff9100");

        coinEl.setAttribute("geometry",{ primitive: "circle",radius: 1};

        coinEl.setAttribute("animation", {
            property: "rotation",
            to: "0 360 0",
            loop: "true",
            dur: 1000
        })

        treasureEntity.appendChild(coinEl);
    }
    
})

<a-entity
    gltf-model="#scuba_driver"
    scale="0.1 0.1 0.1"
    position="5 0 15"
    rotation="0 90 -20"
    diver-rotation-reader

></a-entity>
</body>
</html>