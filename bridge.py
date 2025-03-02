import serial
import time
import subprocess
import re

# Configuration
SERIAL_PORT = '/dev/ttyUSB0'  # Change to match your setup (COM1, etc. on Windows)
BAUD_RATE = 4800
MAX_TEXT_LENGTH = 80  # Maximum characters to send at once to MINT

def clean_text_for_speech(text):
    """Clean and prepare text for the speech synthesizer"""
    # Remove special characters that might confuse MINT
    text = re.sub(r'[^a-zA-Z0-9 .,?!]', '', text)
    # Limit length to prevent buffer overflow
    if len(text) > MAX_TEXT_LENGTH:
        text = text[:MAX_TEXT_LENGTH-3] + "..."
    return text

def send_to_mint(text):
    """Send text to the MINT speech interface via serial port"""
    try:
        # Open serial connection
        ser = serial.Serial(
            port=SERIAL_PORT,
            baudrate=BAUD_RATE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1
        )
        
        print(f"Sending to MINT speech interface: '{text}'")
        
        # Send the text followed by Enter
        ser.write(text.encode('ascii', errors='replace'))
        ser.write(b'\r')
        
        # Wait for completion and read any response
        time.sleep(2)  # Allow time for processing
        response = ser.read(ser.in_waiting).decode('ascii', errors='replace')
        if response:
            print(f"Response from MINT: {response}")
        
        # Close the connection
        ser.close()
        return True
        
    except serial.SerialException as e:
        print(f"Error communicating with MINT: {e}")
        return False

def run_sentiment_analysis():
    """Run the sentiment analysis Python script and capture its output"""
    try:
        # Run the sentiment analysis script
        process = subprocess.Popen(
            ['python', 'sentiment_analysis.py'],  # Adjust the path as needed
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Interact with the script - send a test sentence
        print("Sending test sentence to sentiment analysis...")
        test_sentence = "Today was a really good day"
        process.stdin.write(test_sentence + "\n")
        process.stdin.flush()
        
        # Read output until we get a response
        output = ""
        while True:
            line = process.stdout.readline()
            output += line
            print(line.strip())  # Display in console
            
            # Check if we got a response line
            if "Response:" in line:
                # Extract just the response part
                response_text = line.split("Response:", 1)[1].strip()
                
                # Clean and send to MINT
                clean_response = clean_text_for_speech(response_text)
                send_to_mint(clean_response)
                break
                
            # Avoid infinite loop if something goes wrong
            if not line or "Prediction phase ended" in line:
                break
        
        # Close process
        process.terminate()
        return output
        
    except Exception as e:
        print(f"Error running sentiment analysis: {e}")
        return None

def interactive_mode():
    """Interactive mode to send sentences to analysis and then to MINT"""
    try:
        # Start the sentiment analysis process
        process = subprocess.Popen(
            ['python', 'sentiment_analysis.py'],  # Adjust path as needed
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("Interactive mode started. Enter sentences for analysis (or 'exit' to quit).")
        
        # Skip initial output until prompt
        while True:
            line = process.stdout.readline()
            print(line.strip())
            if "Enter sentence for prediction" in line:
                break
        
        # Main interaction loop
        while True:
            # Get user input
            user_input = input("\nEnter sentence for analysis (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
                
            # Send to sentiment analysis
            process.stdin.write(user_input + "\n")
            process.stdin.flush()
            
            # Read output until we get a response
            response_found = False
            while not response_found:
                line = process.stdout.readline()
                print(line.strip())
                
                if "Response:" in line:
                    # Extract just the response part
                    response_text = line.split("Response:", 1)[1].strip()
                    
                    # Ask user if they want to send to MINT
                    send_choice = input(f"Send this response to MINT? (y/n): ")
                    if send_choice.lower() == 'y':
                        # Clean and send to MINT
                        clean_response = clean_text_for_speech(response_text)
                        send_to_mint(clean_response)
                        
                    response_found = True
                
                # Handle feedback prompt
                if "Is this prediction accurate?" in line:
                    feedback = input("Enter feedback (y/n, or press Enter to skip): ")
                    process.stdin.write(feedback + "\n")
                    process.stdin.flush()
                    
                    # If feedback is 'n', handle the rating prompt
                    if feedback.lower() == 'n':
                        rating_line = process.stdout.readline()
                        print(rating_line.strip())
                        rating = input("Enter rating (1-10): ")
                        process.stdin.write(rating + "\n")
                        process.stdin.flush()
                        
                        # Read the updated response
                        while True:
                            line = process.stdout.readline()
                            print(line.strip())
                            if "Updated Response:" in line:
                                response_text = line.split("Updated Response:", 1)[1].strip()
                                
                                # Ask user if they want to send to MINT
                                send_choice = input(f"Send this updated response to MINT? (y/n): ")
                                if send_choice.lower() == 'y':
                                    clean_response = clean_text_for_speech(response_text)
                                    send_to_mint(clean_response)
                                break
                
                # Avoid infinite loop
                if not line or "Prediction phase ended" in line:
                    break
        
        # Close process
        print("Exiting interactive mode.")
        process.terminate()
        
    except Exception as e:
        print(f"Error in interactive mode: {e}")

if __name__ == "__main__":
    print("Python to MINT Speech Interface Bridge")
    print("-------------------------------------")
    print("1. Run sentiment analysis with test sentence")
    print("2. Enter interactive mode")
    print("3. Send custom text to MINT")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        run_sentiment_analysis()
    elif choice == '2':
        interactive_mode()
    elif choice == '3':
        text = input("Enter text to send to MINT: ")
        clean_text = clean_text_for_speech(text)
        send_to_mint(clean_text)
    else:
        print("Exiting.")
