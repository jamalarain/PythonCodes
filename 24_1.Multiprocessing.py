
import os
from multiprocessing import Process, current_process

def square(number):
    result =number * number
    print(f"the number {number} squares to {result}.")
            
if __name__ == '__main__':
    arr=[3,4,5,6]
    
    for number in arr:
        square(number)
###############################################################
def square(number):
    result =number * number
    process_id = os.getpid()
    print(f"Process ID :{process_id}")
    
    print(f"the number {number} squares to {result}.")
            
if __name__ == '__main__':
    processes=[]
    arr=[3,4,5,6]
    
    for number in arr:
        process=Process(target=square, args=(number,))
        processes.append(process)
        
        process.start() #we tell the process to start

##############################################################
def square(number):
    result =number * number
    process_name= current_process().name #curent process is used to get the name of the process
    print(f"Process name :{process_name}")
    
    print(f"the number {number} squares to {result}.")
            
if __name__ == '__main__':
    processes=[]
    arr=[3,4,5,6]
    
    for number in arr:
        process=Process(target=square, args=(number,))
        processes.append(process)
        
        process.start() 

############################################################
import time
        
def square(number):
    for number in arr:
        time.sleep(0.5)
        result =number * number
            
        print(f"the number {number} squares to {result}.")
            
if __name__ == '__main__':
    arr=range(100)
    
    for i in range(50):
        process=Process(target=square, args=(number,))
        processes.append(process)
        
        process.start() 
        
    for process in processes:
        process.join() 
        print("Multiprocessing complete")
        
#htop
#########################################################