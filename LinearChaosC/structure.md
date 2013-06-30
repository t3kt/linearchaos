The LinearChaosC system is divided into several subsystems:

## Geometry/Animation
The geometry/animation systems are responsible for generating and animating the 3d forms. There are (currently) 2 groups of shapes:
* The tube(s), with the core and wireframe variants, which are both based off of the same underlying geometry.
* The rings, which have their own separate geometry.

## Rendering
The rendering system is responsible for rendering the 3d forms. It also handles and animates the properties of the materials and lighting, as well as the camera position.

## Post-Processing
The post-processing system takes the output of the renderer and performs 2d image manipulation on it. It is based on a chain of effects, including:
* Edge enhancement
* Time-based displacement (though this largely ended up as just a switchable delay)
* Color modification (saturation)
* Color channel shifting - splitting the green and blue channels apart
* Bloom - an additive multi-stage blurring that gives the edges a glowing look
* Echo - a multi-tap delay with feedback, that has adjustable time offsets which makes it possible to sort of temporarily freeze the image and accelerate/decelerate it
* Time buffer/looper - allows the last few seconds to be looped
* Spacial distortion/warping - displacement based on a shifting pattern of smoothed noise

## Control Routing
The routing system is responsible for managing parameters which control various aspects of the other systems. It maps MIDI input on those parameters and supports recording and playing back input sequences. It also updates the control UI from MIDI input.

## Control UI
The UI is a control panel with a slider or button for each parameter supported by the routing system.
