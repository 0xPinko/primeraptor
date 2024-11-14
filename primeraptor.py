import os
import subprocess

print(r"""
██████╗ ██████╗ ██╗███╗   ███╗███████╗██████╗  █████╗ ██████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝██████╔╝██║██╔████╔██║█████╗  ██████╔╝███████║██████╔╝   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██║██╔═══╝    ██║   ██║   ██║██╔══██╗
██║     ██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║██║  ██║██║        ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")
print("""
Proof of Concept by Max Pilgrim
``````````````````````````````````
""")

def get_variables():
    variables = {}
    variables["admin_email"] = input("Enter admin email: ")
    variables["admin_whitelist"] = input("Enter the IP addresses for admin access (comma-separated): ").split(",")
    variables["admin_username"] = input("Enter the admin username (default 'admin'): ") or "admin"
    variables["name"] = input("Enter the project name (default 'primeraptor'): ") or "primeraptor"
    variables["volume_size"] = input("Enter the volume size (default 1000): ") or "1000"
    variables["instance_type"] = input("Enter the instance type (default 'm5.large'): ") or "m5.large"
    return variables

def modify_variables_tf(vars_dict):
    # Overwrite variables.tf with default values based on user input
    variables_tf_path = os.path.join("modules", "variables.tf")
    with open(variables_tf_path, "w") as file:
        for key, value in vars_dict.items():
            if isinstance(value, list):
                formatted_value = f"[{','.join(f'\"{v.strip()}\"' for v in value)}]"
            else:
                formatted_value = f"\"{value}\""
            file.write(f'variable "{key}" {{\n  default = {formatted_value}\n}}\n\n')

def restore_variables_tf():
    # Restore variables.tf to its original form without default values
    original_variables = """
variable "name" {
  type        = string
  default     = "primeraptor"
  description = "Name for the project"
}

variable "admin_whitelist" {
  type        = list(string)
  description = "IP for admin access"
}

variable "admin_username" {
  type        = string
  description = "Username for admin connection"
  default     = "admin"
}

variable "admin_email" {
  type        = string
  description = "Admin Email (to receive config information)"
}

variable "volume_size" {
  type        = number
  description = "Volume for the instance"
  default     = 1000
}

variable "instance_type" {
  type        = string
  description = "Instance type for the server"
  default     = "m5.large"
}
"""
    variables_tf_path = os.path.join("modules", "variables.tf")
    with open(variables_tf_path, "w") as file:
        file.writelines(original_variables)

def run_terraform_command(command):
    # Run Terraform command within the modules directory
    process = subprocess.run(["terraform", command], text=True, cwd="modules")
    if process.returncode != 0:
        print(f"Error running terraform {command}")
    else:
        print(f"Terraform {command} completed successfully")

def main():
    variables = get_variables()
    
    print("Assigning variables.tf with specified requirements...")
    modify_variables_tf(variables)

    try:
        print("Initializing Terraform...")
        subprocess.run(["terraform", "init"], text=True, cwd="modules")
        
        print("Running Terraform plan...")
        run_terraform_command("plan")
        
        apply = input("Do you want to apply these changes? (yes/no): ")
        if apply.lower() == 'yes':
            print("Applying changes...")
            run_terraform_command("apply")
        else:
            print("Terraform apply canceled.")
    finally:
        # Restore variables.tf to original definitions without defaults
        print("Restoring original variables.tf definitions...")
        restore_variables_tf()

if __name__ == "__main__":
    main()
