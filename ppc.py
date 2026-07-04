def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): 
    if b == 0: raise ZeroDivisionError
    return a / b
def floor_divide(a, b): 
    if b == 0: raise ZeroDivisionError
    return a // b
def power(a, b): return a ** b
def modulo(a, b): 
    if b == 0: raise ZeroDivisionError
    return a % b

def print_header():
    print("\n" + "=" * 45)
    print("     ENHANCED MATHEMATICAL CALCULATOR (MC)   ")
    print("  Supported Operators: +, -, *, /, \\, ^, %  ")
    print("=" * 45)
    print(" Special Keys:")
    print("  [ C ]   -> Clear Current State / View History")
    print("  [ OFF ] -> Safely Terminate the System")
    print("-" * 45)

def run_math_calculator():
    # Track calculation history to make the program more robust
    history = []
    calculation_count = 0
    
    print_header()

    while True:
        user_input = input("\nEnter expression (or 'OFF'/'C'): ").strip()

        # 1. Selection Control for System Commands
        if user_input.upper() == 'OFF':
            print("\n" + "=" * 45)
            print(f" Shutting down system. Total operations run: {calculation_count}")
            if history:
                print(" Last 3 calculations:")
                for item in history[-3:]:
                    print(f"  -> {item}")
            print("=" * 45)
            break
            
        if user_input.upper() == 'C':
            print("\n--- Screen Cleared ---")
            if history:
                print(f"Session History ({len(history)} total items):")
                for index, item in enumerate(history, 1):
                    print(f"  {index}. {item}")
            else:
                print("No history recorded yet.")
            print("-" * 22)
            continue

        # 2. Parsing and Tokenization Logic
        # Explicit parsing prevents malicious or broken input code execution
        try:
            # Find which requested operator is present in the input string
            target_operator = None
            for op in ['+', '-', '*', '/', '\\', '^', '%']:
                if op in user_input:
                    target_operator = op
                    break
            
            if not target_operator:
                print("Error: No valid arithmetic operator found (+, -, *, /, \\, ^, %)")
                continue
                
            # Split numbers based on the operator found
            parts = user_input.split(target_operator)
            if len(parts) != 2 or parts[0].strip() == "" or parts[1].strip() == "":
                print("Error: Format must be [Number] [Operator] [Number] (e.g., 15 + 5)")
                continue
                
            # Convert values to floating-point numbers for high computational accuracy
            num1 = float(parts[0].strip())
            num2 = float(parts[1].strip())
            
            # 3. Selection Control Statements for Mathematical Mapping
            result = 0.0
            op_name = ""
            
            if target_operator == '+':
                result = add(num1, num2)
                op_name = "Addition"
            elif target_operator == '-':
                result = subtract(num1, num2)
                op_name = "Subtraction"
            elif target_operator == '*':
                result = multiply(num1, num2)
                op_name = "Multiplication"
            elif target_operator == '/':
                result = divide(num1, num2)
                op_name = "Standard Division"
            elif target_operator == '\\':
                result = floor_divide(num1, num2)
                op_name = "Floor Division"
            elif target_operator == '^':
                result = power(num1, num2)
                op_name = "Exponentiation"
            elif target_operator == '%':
                result = modulo(num1, num2)
                op_name = "Modulo Remainder"
            
            # Formatting results cleanly (dropping .0 if integer value)
            formatted_result = int(result) if result.is_integer() else result
            
            # 4. Display Result and Save Log Summary
            print(f"Operation : {op_name}")
            print(f"Result    = {formatted_result}")
            
            log_entry = f"{num1} {target_operator} {num2} = {formatted_result}"
            history.append(log_entry)
            calculation_count += 1
            
        # 5. Robust Exception Safety Handling
        except ZeroDivisionError:
            print("Mathematical Error: Division by zero is undefined.")
        except ValueError:
            print("Input Value Error: Please make sure both operands are numeric integers or decimals.")
        except Exception as error:
            print(f"System Error encountered: {error}")

if __name__ == "__main__":
    run_math_calculator()
