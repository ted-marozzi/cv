# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("./tar")):
        
        
        dst ='golden_retriever_' + str(count) + ".jpg"
        
        
        # rename() function will 
        # rename all the files 
        os.rename("./tar/" + filename, "./tar/" + dst)
        

# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 