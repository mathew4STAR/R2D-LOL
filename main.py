import description
import download as vidget
import facedet

target = input("Please input suspected link: ")

print("Running test 1")
test1 = description.main(target)

def correct():
    print("This is a rickroll")
    return True

def wrong():
    print("First detectection complete")
    print("status:not a rickroll")
    print("running second test")

if test1 == True:
    d = correct()
else:
    wrong()

if d == False:
    name = vidget.download_video(target)
    finalval = facedet.det(name)

if finalval == True:
    correct()
else:
    wrong()
