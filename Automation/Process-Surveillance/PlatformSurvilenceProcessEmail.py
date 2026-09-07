import psutil
import sys
import os
import time
import schedule
import datetime
import smtplib

from email.message import EmailMessage

# This function sends the generated log file through email
def send_mail(FileName,sender_email, app_password, receiver_email, subject, body):

    try:
        msg = EmailMessage()                 # Create an email message object

        msg["From"] = sender_email           # Set sender email address
        msg["To"] = receiver_email           # Set receiver email address
        msg["Subject"] = subject             # Set email subject

        msg.set_content(body)                # Set email body content

        fObj = open(FileName,"rb")           # Open the log file in binary read mode

        FileData = fObj.read()               # Read the complete log file
        fObj.close()                         # Close the file

        msg.add_attachment(FileData,maintype="application",subtype="octet-stream",
                           filename=os.path.basename(FileName))       # Attach the log file to the email

        smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)    # Create secure Gmail SMTP connection
        smtp.login(sender_email, app_password)           # Login using sender email and app password
        smtp.send_message(msg)                            # Send the email
        smtp.quit()                                       # Close the SMTP connection

        print("Mail send successfully\n")

    except Exception as e:
        print("Unable to send email\n")
        print(e)


# This function finds and sorts processes according to CPU usage
def Top10CpuProcess():

    Data = ProcessScan()                  # Get information about all running processes

    Data.sort(key = lambda x : x["cpu_percent"], reverse=True)      # Data can sort CPU percent in descending order
    return Data                         


# This function finds and sorts processes according to RAM usage
def Top10RamProcess():

    Data = ProcessScan()                  # Get information about all running processes

    Data.sort(key= lambda x : x["memory_percent"], reverse=True)        # Data can sort RAM percent in descending order
    return Data                         


# This function scans all currently running processes
def ProcessScan():

    listprocess = []                     # Create an empty list to store process information

    for proc in psutil.process_iter():   # Iterate through all running processes
        try:
            info = proc.as_dict(attrs=["pid","name","username","status"])       # Get basic information about the current process

            info["cpu_percent"] = proc.cpu_percent(None)       # Get CPU usag
            info["memory_percent"] = proc.memory_percent()     # Get RAM usage
            info["creation_time"] = proc.create_time()        # Get process creation time

            listprocess.append(info)                           # Add process information to the list

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):      # Handle processes which cannot be accessed
            pass

    return listprocess                     # Return the process information list


# This function creates the log file and stores complete system information
def PlatformSurvillance(FolderName, sender_email, app_password, receiver_email, subject, body):

    Border = "-"*50                       

    Ret = False                           # Initialize return variable

    Ret = os.path.exists(FolderName)      # Check whether the folder already exists

    if(Ret == True):
        Ret = os.path.isdir(FolderName)   # Check whether the existing path is a directory
        if(Ret == False):
            print("Unable to proceed as directory name is existing but its not a directory")
            return

    else:
        os.mkdir(FolderName)              # Create the folder
        print("Directory for the logfile gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")    # Generate current date and time

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)   # Create log file path

    fobj = open(FileName,"w")              # Open log file in write mode

    print(f"Log file gets succesfully created with name {FileName}")

    fobj.write(Border+"\n")                
    fobj.write("---- Marvellous Platform Survillence System ----\n")    
    fobj.write("Log file gets created at : "+timestamp+"\n")            # Write log creation time
    fobj.write(Border+"\n\n")              

    fobj.write("---------------- System Report -----------------\n")     # Write system report heading

    # CPU information
    fobj.write("CPU Report\n")              
    fobj.write("Number of active CPU cores : %s\n" %psutil.cpu_count())  # Write CPU core count
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())              # Write CPU usage
    fobj.write(Border+"\n")            

    # RAM information
    memory = psutil.virtual_memory()       # Get virtual memory information

    fobj.write("RAM Report\n")              
    fobj.write("RAM Usage : %s %%\n" %memory.percent)                    # Write RAM usage
    fobj.write("Total RAM available : %s\n" %memory.total)               # Write total RAM
    fobj.write(Border+"\n")                 

    # Netork Usage
    netobj = psutil.net_io_counters()      # Get network input/output information

    fobj.write("Network Report\n")         # Write network report heading
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))  # Write sent data
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024))) # Write received data
    fobj.write(Border+"\n")               

    # Disk Information
    dObj = psutil.disk_usage("/")          #it contais root directory 

    fobj.write("Disk Report\n")             # Write disk report heading
    fobj.write("Total disk space : %.2f GB\n" %(dObj.total / (1024 ** 3))) # Write total disk space
    fobj.write("Used disk space : %.2f GB\n" %(dObj.used / (1024 ** 3)))   # Write used disk space
    fobj.write("Free disk space : %.2f GB\n" %(dObj.free / (1024 ** 3)))   # Write free disk space
    fobj.write("Disk Usage : %s %%\n" %dObj.percent)                       # Write disk usage percentage
    fobj.write(Border+"\n")                

    # Process log
    Data = ProcessScan()                   # Get information about all running processes

    fobj.write("Process Report\n")         
    fobj.write(Border+"\n")                

    for info in Data:                       # Iterate through every process

        fobj.write("PID : %s\n" %info.get("pid"))                       # Write process ID
        fobj.write("Name : %s\n" %info.get("name"))                     # Write process name
        fobj.write("User Name : %s\n" %info.get("username"))            # Write username
        fobj.write("Status : %s\n" %info.get("status"))                 # Write process status
        fobj.write("CPU usage : %.2f\n" %info.get("cpu_percent"))       # Write CPU usage
        fobj.write("RAM usage : %.2f\n" %info.get("memory_percent"))    # Write RAM usage

        creation_time = datetime.datetime.fromtimestamp(info.get("creation_time"))      # Convert timestamp
        creation_time = creation_time.strftime("%d_%m_%Y_%H_%M_%S_%p")     # Format creation time

        fobj.write("Process creation time : %s\n" %creation_time)       # Write creation time

        fobj.write(Border+"\n")                

    # Top 10 CPU process
    Data = Top10CpuProcess()                   # Get processes sorted by CPU usage

    Cout = 0                                   # Initialize process counter

    fobj.write("Top 10 CPU Consuming Processes\n")  
    fobj.write(Border+"\n")                    

    for info in Data:                           # Iterate through sorted processes
        if(Cout == 10):                         # Check whether 10 processes are completed
            break                              

        fobj.write("PID : %s\n" %info.get("pid"))          
        fobj.write("Name : %s\n" %info.get("name"))       
        fobj.write("CPU usage : %.2f\n" %info.get("cpu_percent"))      

        Cout = Cout + 1                         # Increase process counter

        fobj.write(Border+"\n")             

    # Top 10 RAM Process
    Data = Top10RamProcess()                    # Get processes sorted by RAM usage

    fobj.write("Top 10 RAM Consuming Processes\n")  
    fobj.write(Border+"\n")                   

    Cout = 0                                    # Reset process counter

    for info in Data:                           # Iterate through sorted processes
        if(Cout == 10):                         # Check whether 10 processes are completed
            break

        fobj.write("PID : %s\n" %info.get("pid"))          
        fobj.write("Name : %s\n" %info.get("name"))        
        fobj.write("RAM usage %s %%\n" %info.get("memory_percent"))    

        Cout = Cout + 1                         # Increase process counter

        fobj.write(Border+"\n")                

    # Battery Information
    Battery = psutil.sensors_battery()         # Get battery information

    fobj.write("Battery Information\n")         
    fobj.write(Border + "\n")                 

    if(Battery != None):                       # Check whether battery information is available
        fobj.write("Battery Percentage : %s %%\n" %Battery.percent)     # Write battery percentage

        if(Battery.power_plugged == True):     # Check whether charger is connected
            if(Battery.percent == 100):        # Check whether battery is fully charged
                fobj.write("Battery Status : Fully Charged\n")
            else:
                fobj.write("Battery Status : Charging\n")

        else:
            fobj.write("Battery status : Discharging\n")

    else:
        fobj.write("Battery information is not available\n")          
        fobj.write(Border+"\n")                   

    fobj.write(Border+"\n")                   
    fobj.write("--------------- End of Log File ----------------\n")      
    fobj.write(Border+"\n")                    

    fobj.close()                            # Close log file

    print("Log created")
    print("Calling send_mail")

    send_mail(FileName,sender_email, app_password, receiver_email, subject, body) # Send log file through email
    print("Mail function completed")


# This function controls command-line arguments and schedules the project
def main():

    Border = "-"*50                         
    print(Border)
    print("---- Marvellous Platform Survillence System ----")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):                 # Check whether one command-line argument is provided
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):     # Check for help option
            print("This automation script is used to perform ")
            print("1 : It fetch the information of running processess")
            print("2 : It fetch information about the primary storage as RAM")
            print("3 : It fetch information about the secondary storage as HDD")
            print("4 : It fetch the information about the microprocessor")
            print("5 : It gets auto scheduled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):   # Check for usage option
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")

        else:
            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for getting more details")

    # Actual project code
    elif(len(sys.argv) == 3):                # Check whether correct number of arguments is provided

        sender_email = "gloomytwilight09@gmail.com"       # Sender email address
        app_password = "noglmwvejyjwguxt"                # Gmail app password
        receiver_email = "sharvaribhosale65@gmail.com"   # Receiver email address
        subject = "Platform Survilence Process Automation Script"   # Email subject
        body = "Hello,\n\nPlease find the attached Platform Surveillance Log File.\n\nThank You." # Email body

        print("Schedular started succesfully")
        print("Press Ctrl + C to abort the automation script")

        # Schedule PlatformSurvillance according to the given time interval
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance, sys.argv[2], sender_email, app_password, receiver_email, subject, body)

        while True:                         # Run the scheduler continuously
            schedule.run_pending()           # Execute pending scheduled tasks
            time.sleep(1)                    # Wait for one second

    else:
        print("Invalid number of argumenst")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("--- Thank you for using our automation System ---")
    print(Border)


# This condition ensures that main() runs only when this file is executed directly
if __name__ == "__main__":

    main()                                  # Call the main function