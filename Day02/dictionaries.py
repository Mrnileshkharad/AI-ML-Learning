response = {
    "transactionId": "TXN1001",
    "status": "SUCCESS",
    "amount": 2500,
    "currency": "INR"
}

print("Transaction ID: ", response["transactionId"])
print("Status: ", response["status"])
print("Amount: ", response["amount"])

##Adding remarks tag in response
response.update({"remarks":"Payment Successful"})
print("Remarks: ", response["remarks"])

##Updating status to COMPLETED
response.update({"status":"COMPLETED"})
print("Status: ", response["status"])

##getting all tags from respose
print(response.keys())

##getting all values from respose
print(response.values())

##getting all key-value pairs from respose
print(response.items())

##safe reading customerName tag
print(response.get("customerName"))
print(response.get("customerName","Not Availlable"))



