from promptflow import tool
import json
import os

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def to_jsonl(answer: str, question: str, chatlist: list ) -> str:
    k1= os.getcwd()
    # Get current working directory
    cwd = os.getcwd()

    # Define filename
    filename = "output.jsonl"

    # Combine cwd and filename
    filepath = os.path.join(cwd, filename)

  
    chatlist_count = len(chatlist)  # Get the count of chatlist
    print(chatlist_count )
  

    # Check if the file exists
    if os.path.isfile(filepath):
        print('File exists')
    else:
        print('File does not exist')
    
    data = {}  # Declare the 'data' variable outside of the loop
    with open(filepath, "a") as file:
        for item in chatlist:
            #print(item)
            question = item['inputs']['question']
            answer = item['outputs']['output']
            data = {
                "question": question,
                "answer": answer
            }
            json.dump(data, file)
            print('record updated in file')
            file.write('\n')
    return k1