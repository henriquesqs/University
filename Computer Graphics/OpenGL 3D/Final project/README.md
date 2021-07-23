# 3d Scenario with Luminosity and Specular Reflection
This projects aims to create a 3D scenario using Wavefront objects generated from 3D models using [Blender](https://www.blender.org/).

There's a moon rotating on this scenario reflecting its light on all the objects using the [Phong's Reflection Model](https://en.wikipedia.org/wiki/Phong_reflection_model). If you wait patiently, you'll see the reflection based on where the camera (your cursor) is pointing to.

![Preview of the running project](https://i.imgur.com/QQiKl33.png)
## Requisites
- [Python](https://www.python.org/downloads/) 3+
- [pip](https://pip.pypa.io/en/stable/installing/)

## How to use
1. Install dependencies by entering:
```
pip install -r requirements.txt
```

2. Run the project by typing:
```
python3 project.py
```

3. Controls

- `W, A, S, D` keyboard keys moves the camera
  
- `P` keyboard key toggles the polygon mode

- `U` and `I` to increase and decrease scenario luminosity, respectively

- `Mouse` rotates the camera
  
  **To change parameters from the projection perspective, use the following keyboard keys:**

- `Numbers 1 and 2` to increase (1) and decrease (2) the **'fovy'** parameter
  
- `Numbers 3 and 4` to increase (3) and decrease (4) the **'aspect'** parameter
  
- `Numbers 5 and 6` to increase (5) and decrease (6) the **'near'** parameter
  
- `Numbers 7 and 8` to increase (7) and decrease (8) the **'far'** parameter


## Models credits
1. **[Abandoned Cottage House](https://free3d.com/3d-model/abandoned-cottage-house-825251.html)** by [Animated Heaven](http://www.animatedheaven.weebly.com/)
2. **[Banjofrog v1](https://free3d.com/3d-model/banjofrog-v1--699349.html)**
3. **[Wind Mill](https://free3d.com/3d-model/wind-mill-2774.html)**
4. **[Horse with big tush](https://free3d.com/3d-model/a-horse-with-a-big-tush-498195.html)** by [flyingpimphat](https://free3d.com/user/flyingpimphat)
5. **[Birch tree](https://free3d.com/3d-model/birch-tree-48016.html)** by [sandralavixen](https://free3d.com/user/sandralavixen)

## Project credits
- [Bruno dos Santos](https://github.com/brunin-cps/)
- Me
- [Witor M. A. de Oliveira](https://github.com/witorMao/)
- **And a huge thanks to [Paulinho](https://github.com/pau1o-hs/) who taught us how to use Blender** :heart: