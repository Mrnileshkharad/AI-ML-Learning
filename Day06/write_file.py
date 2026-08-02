file = open ("Day06/logs/execution_log.txt",'w')
file.write("========== Automation Execution ==========\nExecution Started\nExecuting TC_Login\nExecuting TC_Payment\nExecuting TC_Refund\nExecution Completed\n==========================================")
file.close()
file = open ("Day06/logs/execution_log.txt",'r')
logs=file.read()
print(logs)
file.close()

log_data = [
    "========== Automation Execution ==========",
    "Execution Started",
    "Executing TC_Login",
    "Executing TC_Payment",
    "Executing TC_Refund",
    "Execution Completed",
    "=========================================="
]

file = open ("Day06/logs/execution_log.txt",'w')
for logs in log_data:
    file.write(logs +"\n")
file.close()