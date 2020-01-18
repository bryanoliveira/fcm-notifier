# Firebase Cloud Messaging Notifier
A python module I made to notify about ML model training statuses with Firebase Cloud Messaging.

## Requires
- Python 3 and `pyfcm` module (`pip install pyfcm`)
- A Firebase Cloud Messaging project token (see https://firebase.google.com/docs/cloud-messaging)
- A device token (to receive notifications)

## Usage
- Install:
  
  `pip install git+https://github.com/bryanlincoln/fcm-notifier`
- Set up the environment variables `FCM_API_KEY` and `FCM_DEVICE_TOKEN` with your Firebase project token and your device token. Alternatively, you may pass this values directly to the FCMNotifier constructor, but it's not recommended for security reasons.
- In your code, import it with

  `from fcm_notifier import FCMNotifier`
- Instantiate it:
  
  `notifier = FCMNotifier()`
- Push a notification! 
  
  `notifier.notify(title='Hello world')`

You may use the optional argument `message` to set up a notification body. Aditional optional arguments are accepted too, being arranged in the notification's body.
