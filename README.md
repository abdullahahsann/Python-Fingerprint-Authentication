# Python-Fingerprint-Authentication

A practical implementation with some bit of changes of the "Hands on Fingerprint Recognition with OpenCV and Python by Raffaele Cappelli"

I was learning to make a fingerprint authentication program in python. After many videos and blogs i finally came across this one and found it to be most useful. I've made it into an executable python file, and categorised the functions as such that it works for any two passed images.

You can implement a for loop if you want to go through all the files in database.

## How to run
Run the fg.py file, and provide the fingerprint images path in the twp_fp_comparison() function at the end.

The main process of getting the local ridges, image enhancemet, minutiae positions, directions and local structures is in the analyze_fp.py file

## Resources that helped me

  1. Hands on Fingerprint Recognition with OpenCV and Python (To whom the code belongs): https://www.comp.hkbu.edu.hk/wsb2021/lecturer_details.php?lect_id=2
  2. Fingerprint algorithm recognition: https://medium.com/@cuevas1208/fingerprint-algorithm-recognition-fd2ac0c6f5fc
  3. Fingerprint Recognition - Computerphile: https://www.youtube.com/watch?v=xD88Qs_DZp4&ab_channel=Computerphile

## Rights

I do not own and have not written the code. The code belongs to Raffaele Cappelli and is available via the resouces mentioned above. I've just made some changes to it.
