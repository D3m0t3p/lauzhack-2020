# Lauzhack 2020
LauzHack is a hackathon that aims to let students and recent graduates from Switzerland and beyond unleash their imagination, meet new friends, discover technologies, and network with industry representatives, while staying at home.
The participants develop an idea in the form of code, optionally participate in challenges set by sponsors, and are judged at the end of the event with prizes for the top projects.

## Inspiration
We chose the challenge proposed by SBB, consisting of helping blind people to find train doors. In the description, it was advised to use and challenge the preexisting model designed by SBB, this using machine learning. Visually impaired customers would scan with the SBB Inclusive app the train they want to get in and thanks to a door button detector, the app would guide them inside the train safely. We chose to question this choice by asking ourselves if we could find a more privacy-friendly solution to this problem. In fact, by using the camera of the smartphone to detect a door button, one would also film others (maybe against their will) and these images wouldn’t be analyzed on the phone but surely on a cloud online.

## What it does
We started from the principle that we can know the exact position of every door on a train if we know the model of the train and its exact position on the platform. The first part can easily be retrieved thanks to the SBB API and documentation. For its position relative to the platform it is a bit more difficult (since we know that the train driver doesn’t have a very precise spot to stop on the platform), and we came up with two ideas. First, we chose to use computer vision (thanks to security cameras / a dedicated camera per platform) to detect the train and find its exact location. The second solution implies bluetooth beacons placed on the platform (which is possible after talking with SBB sponsors). We would place a beacon also on the train (at the beginning or the end of the train)(making sure it’s “outside” as the train acts as a Faraday cage, the electromagnetic waves would be trapped inside otherwise) and will be able to triangulate the beacon, and since it would be placed on a fixed point on the train we would immediately have the exact location of the train. The next step is now to locate the user on the platform. We will now use the same bluetooth beacons placed at equal distance on the platform to triangulate the person. Using this technology it is also possible to find the direction the phone is pointing by analysing the angle of arrival of the signal so it will greatly help us guiding the person to the door, hence to the door button. To guide the person to the door button, we will simply use SpeechSynthesis, an API that will allow us to vocalize the instructions to the person, and which is compatible with both iOS and Android.

## Advantages
Thanks to this solution we can also guide precisely the person to the right car, corresponding to the ticket he/she bought (first/second class). This can also be used for trains with assigned cars and seats so our solution is very modular and can solve other problems too. It will also be easier to use this since the person won’t have to hold the phone in his/her hands to scan in front of him/her and try to find the door, with a cane and/or a guide dog in the other hand. The phone could simply be in the person’s pocket and the speaker would guide him/her. Moreover, holding the camera in the person's hand will be less efficient since many people can be waiting for the same train, and the person could not be able to scan the button since everyone would be blocking the view and the algorithm.

## How I built it
Linear Algebra, Computer Vision, Python, OpenCV

## Challenges I ran into
Question a preexisting model and trying to find another way around the problem. How to locate precisely the train on the platform.

## Accomplishments that I'm proud of
Having precise measurements on pictures of a subway we took ourselves with a smartphone camera.
