# Firebase Cloud Messaging Notifier

A python module to notify about Machine Learning model training statuses with Firebase Cloud Messaging. It is best used with [Flutter Firebase Cloud Messaging Receiver](https://github.com/bryanlincoln/flutter-fcm-receiver), a Flutter app I made to export device's tokens and receive notifications.

## Requirements

-   Python 3 and `pyfcm` module (`pip install pyfcm`)
-   A Firebase Cloud Messaging project token (see https://firebase.google.com/docs/cloud-messaging)
-   A device token (to receive notifications). You may use [Flutter Firebase Cloud Messaging Receiver](https://github.com/bryanlincoln/flutter-fcm-receiver) for this.

## Usage

-   Install:

    `pip install git+https://github.com/bryanlincoln/fcm-notifier`

-   Set up the environment variables `FCM_API_KEY` and `FCM_DEVICE_TOKEN` with your Firebase project token and your device token. Alternatively, you may pass this values directly to the FCMNotifier constructor (in this order), but it's not recommended for security reasons.

-   In your code, import it with

    `from fcm_notifier import FCMNotifier`

-   Instantiate it:

    `notifier = FCMNotifier()`

-   Push a notification!

    `notifier.notify(title='Hello world')`

## Additional Info

You may use the optional argument `message` to set up a notification body for method `notify`. Aditional arguments are accepted too. They'll be arranged into the notification's body. Examples:

- Calling `notify(title='Notification Title', message='Notification Body')` generates a notification like:

| Notification Title |
|--------------------|
| Notification Body  |

- Calling `notify(Loss=123, Accuracy=0.9)` generates a notification like:

| Train Status  |
|---------------|
| Loss: 123     |
| Accuracy: 0.9 |
