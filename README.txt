Warning i only support window for now, the link to the code is downthere is you have python 3.X on MacOS or linux just launch the Main.py with the data.txt in the same folder, you may need numpy and other regular library...

First download the SeedCracker.zip
unzip it then launch main.html with Chrome or Mozilla Firefox

How to use the seed cracking tool:

You need to get to the end and get the end pillars height for that get the location of your end platform and drag drop the number on the yellow case, if you dont like that method you can also input the number in the white box but it will start with the lower one (real world coordinate are x=0,z=42 and go clockwise. Once that done you will need to gather at least 5+1 structure chunks.

How to get the structure Chunks:

Remember its the chunks you need not the plain coordinate (use F3 screen line Chunk)

You only need to input 5 in the right panel

Dont use Igloo or Witch hut they aren't always reliable (jungle temple could also be an issue but i dont have experienced it for now).
-For Ocean monument, you need to get the central chunk where the Top elder guardian is (the bastion like i call it)
-For Mansion, you need to get the chunk at the entrance, its the one that start by the left side of the entrance and contain the main staircase to the next floor
-For end cities, you need to get the chunk of the base of the end city, most of end cities base generate in the corner of a chunk and their main part is in that chunk, that's the chunk you are looking for
-For Village, just locate the well, its always that chunk
-For desert temple, its the main chunk where the chests are and the Tnt, it contains at least 16x16 of the whole structure
-For jungle Temple, its the whole chunk in which it generated
-for witch hut, they can generate in corner or the middle of a chunk anyway that's the chunk where the main part is (Dangerous to use)
-Igloo, they tend to generate correctly if they have an underground liar, you can use them then, like all other structure, its the chunk where the main part is (Dangerous to use)

I will ask you a 6th one (the +1) to confirm the structure seed, if you select the Step assist option

How to get the biome Coordinate:

Tips:
-Use an area where 3 or more biome intersect and input the closest block from different biome in that area, the ideal would be a 2x2 square with 4 different biome.
-Dont mess up with the name, desert is different from desertHills, savanna M is different from savanna plateau M...
-If you want you can also input rare biome (mostly mutated one so ID>128 or after Mesa in the list) but it could be slower than a local area if too spread
-you only need 4 to guarantee at 85% the right seed, but get a fifth one in case, it could be ask in the process to confirm

When ready click on Next, you will redirect to a page called Performance for now i only support CPU multiprocessing so the more core/thread you have, the better, if you really dont know anything about this page just click on the case "I dont know" and i will calculate everything for you, ofc if you tweak anything be cautious the program is quite ressource intensive and could slow a lot your computer.
When you are done click on prepare download then download and put the data.txt (or any name but beginning by "data" and ending by ".txt") in the same folder as SeedCrackerByNeil.exe and launch the seed cracker. It will be ask if you want step assist or not, if you are near your computer i would say say N for step assist because the main part which is the structure seed computation will take a long time and when it stops you will have 5-10min of computation left before getting your seed. If you say Y for auto mode then the program will iterate all seed, check them and so on, which will take a lot of time and ressource.


the code can be found here: https://github.com/hube12/mccracking2