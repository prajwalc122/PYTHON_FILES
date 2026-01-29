#install an external module and use it to perform an operation of your interest
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hello how are you  im waiting ggg")
engine.say("hello my name is prajwal i am studied in kateel ashok pai memorable college")
TimeoutError=2.9
engine.runAndWait()