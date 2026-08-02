

log_data1 = [
    "========== Automation Execution ==========",
    "Execution Started",
    "Executing TC_Login",
    "Execution Completed",
]

with open ("Day06/logs/execution_log.txt",'w') as file:
 for log in log_data1:
    file.write(log +"\n")


log_data2 = [
    "------------------------------------------",
    "Execution Started",
    "Executing TC_Payment",
    "Executing TC_Refund",
    "Execution Completed"
]

with  open ("Day06/logs/execution_log.txt",'a') as file :
    for log in log_data2:
       file.write(log +"\n")

log_data3 = [
    "------------------------------------------\n",
    "Execution Started\n",
    "Executing TC_Payment\n",
    "Executing TC_Refund\n",
    "Execution Completed\n"
]

with open ("Day06/logs/execution_log.txt",'a') as file :
     file.writelines(log_data3)
