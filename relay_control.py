#!/usr/bin/env python3
"""
Relay Controller for Raspberry Pi Zero 2W
Simplified interface for controlling electromagnetic relays
"""

import RPi.GPIO as GPIO
import sys

# Relay pin assignments (BCM numbering)
RELAY_PIN = 27  # GPIO 27 (Pin 13) 

# Some relay modules are active LOW (relay ON when GPIO LOW)
# Set to True if your relay turns ON when you write LOW
ACTIVE_LOW = True  # Change to True if your relay is inverted

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RELAY_PIN, GPIO.OUT)
        
def relay_on() -> str:    
    try:        
        if ACTIVE_LOW:
            GPIO.output(RELAY_PIN, GPIO.LOW)   
        else:
            GPIO.output(RELAY_PIN, GPIO.HIGH) 
        
        return "Success: relay is ON"
    except Exception as e:
        return f"Error: {str(e)}"        

def relay_off() -> str:    
    try:        
        if ACTIVE_LOW:
            GPIO.output(RELAY_PIN, GPIO.HIGH)  
        else:
            GPIO.output(RELAY_PIN, GPIO.LOW)  
        
        return "Success: relay is OFF"
    except Exception as e:
        return f"Error: {str(e)}"        

def main():
    command = sys.argv[1].lower()
                
    # Route to appropriate function
    result = None
    
    if command == "on":
        result = relay_on()   
    elif command == "off":
        result = relay_off()
    elif command == "time":
        result = get_time()                
    else:
        result = "Unknown command"
    
    print(result)
    sys.exit(0 if result == "on" or result == "off" else 1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Error: Interrupted by user")
        GPIO.cleanup()
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)