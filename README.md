# Firebase Cloud Messaging Notifier
A python module I made to notify about ML model training statuses with Firebase Cloud Messaging.

## Requires
- Python 3 and `pyfcm` module (`pip install pyfcm`)
- A Firebase Cloud Messaging project token (see https://firebase.google.com/docs/cloud-messaging)
- A device token (to receive notifications)

## Usage
- Install: 
  
  `pip install git+https://github.com/bryanlincoln/fcm-notifier`
- In your code, import it with

  `from fcm_notifier import FCMNotifier`
- Instantiate it passing your FCM API Token and device tokens (may be a single string or a list of strings):
  
  `notifier = FCMNotifier(<API TOKEN>, <DEVICE TOKENS>)`
- Push a notification! 
  
  `notifier.notify(title='Hello world')`

You may use the optional argument `message` to set up a notification body. Aditional optional arguments are accepted too, being arranged in the notification's body.
