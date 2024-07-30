import os
from python_terraform import *

def create_s3_bucket():
    # Define the working directory
    working_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Initialize the Terraform instance
    tf = Terraform(working_dir=working_dir)
    
    # Initialize Terraform
    return_code, stdout, stderr = tf.init()
    print(f"Terraform init return code: {return_code}")
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")
    
    # Apply the Terraform configuration
    return_code, stdout, stderr = tf.apply(skip_plan=True)
    print(f"Terraform apply return code: {return_code}")
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")

if __name__ == "__main__":
    create_s3_bucket()