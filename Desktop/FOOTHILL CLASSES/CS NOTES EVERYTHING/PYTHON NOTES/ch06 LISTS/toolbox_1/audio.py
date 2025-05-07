import numpy
import scipy.io.wavfile

def main() :
   inputname = input("Input file: ")

   contents = scipy.io.wavfile.read(inputname)
   samplerate = contents[0]
   data = contents[1].tolist() # Now it's a Python list

   outputdata = process(data)
   outputname = inputname.replace(".wav", ".out.wav")
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

def process(data) :
   result = []
   for i in range(len(data)) :
      if (data[i] > 0) :
         result.append(30000)
      else :
         result.append(-30000)            
   return result         
    
# Start the program.
main()

