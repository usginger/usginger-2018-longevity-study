import time
import sys

# Mock library setup for environments testing without physical GPIO pins connected
try:
    import Adafruit_DHT
    import RPi.GPIO as GPIO
    HARDWARE_AVAILABLE = True
except ImportError:
    HARDWARE_AVAILABLE = False

# --- HARDWARE CONFIGURATION CONSTANTS ---
DHT_SENSOR = 22      # DHT22 Sensor connected to GPIO pin 22
DHT_PIN = 4          # DHT22 Data pin connected to GPIO pin 4
PELTIER_PIN = 17     # Relay control for Dehumidifier on GPIO pin 17
FAN_PIN = 27         # Relay control for Circulation Fans on GPIO pin 27

# --- TARGET STASIS THRESHOLDS ---
TARGET_HUMIDITY_MAX = 45.0  # Max humidity percentage before dehumidifier triggers
TARGET_HUMIDITY_MIN = 35.0  # Target low humidity marker for stasis baseline

def setup_system():
    """Initializes the GPIO pins on the Raspberry Pi."""
    if not HARDWARE_AVAILABLE:
        print("[System Info] Running in simulation mode. No Raspberry Pi hardware detected.")
        return
        
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PELTIER_PIN, GPIO.OUT)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    
    # Start with climate controls offline
    GPIO.output(PELTIER_PIN, GPIO.LOW)
    GPIO.output(FAN_PIN, GPIO.LOW)
    print("[System Info] GPIO Pins initialized successfully.")

def monitor_climate(simulated_humidity=50.0):
    """Monitors ambient conditions and controls active hardware arrays."""
    print("\n--- Starting Active Stasis Climate Automation Loop ---")
    
    try:
        while True:
            if HARDWARE_AVAILABLE:
                humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            else:
                # Simulation mode behavior to verify control paths
                humidity = simulated_humidity
                temperature = 22.5
                
            if humidity is not None and temperature is not None:
                print(f"Current Environment -> Temp: {temperature:.1f}°C | Humidity: {humidity:.1f}%")
                
                # Evaluation logic for active dehumidification
                if humidity > TARGET_HUMIDITY_MAX:
                    print("⚠️ ALERT: Humidity above stasis thresholds! Activating Peltier Dehumidifier and Fans.")
                    if HARDWARE_AVAILABLE:
                        GPIO.output(PELTIER_PIN, GPIO.HIGH)
                        GPIO.output(FAN_PIN, GPIO.HIGH)
                    simulated_humidity -= 2.5 # Simulate moisture dropping in test mode
                
                elif humidity <= TARGET_HUMIDITY_MIN:
                    print("✅ IDEAL: Target stasis environment reached. Powering down active systems to conserve energy.")
                    if HARDWARE_AVAILABLE:
                        GPIO.output(PELTIER_PIN, GPIO.LOW)
                        GPIO.output(FAN_PIN, GPIO.LOW)
                    simulated_humidity += 0.5 # Simulate natural moisture seep in test mode
                    
                else:
                    print("⚙️ STABLE: Conditions nominal. Circulation fans maintaining baseline airflow.")
                    if HARDWARE_AVAILABLE:
                        GPIO.output(FAN_PIN, GPIO.HIGH)
                        
            else:
                print("[Hardware Error] Failed to retrieve data from DHT22 sensor. Retrying connection...", file=sys.stderr)
            
            # Run loops every 5 seconds for tracking stability
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n[System Interrupted] Shutting down climate loops safely.")
    finally:
        if HARDWARE_AVAILABLE:
            GPIO.cleanup()
        print("[System Status] GPIO pins cleared. Chamber in passive stasis mode.")

if __name__ == "__main__":
    setup_system()
    # Runs the tracker loop. Pass arbitrary start values to test behavior in mock environments.
    monitor_climate(simulated_humidity=52.0)
