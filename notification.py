from plyer import notification
import time 

if __name__ == "__main__":
    while True:
        notification.notify(
            title="~~~ Take Rest ~~~",
            message="Enough working Deva Priya!! It's time for rest :)",
            timeout=5)
        time.sleep(60*60)