from pyfcm import FCMNotification

class FCMNotifier:
    def __init__(self, api_key, devices):
        '''Creates an instance of MLNotifier

        Configures Firebase Cloud Messaging to be able to push notifications.
        You must provide an API key and a device token.
        For more information, see https://firebase.google.com/docs/cloud-messaging

        Attributes:
            api_key (string): Your Firebase project's API key
            devices (string or list): A single string containing a device suitable to
                receive notifications or a list of them.
        '''
        self.push_service = FCMNotification(api_key=api_key)

        self.devices = devices

    def notify(self, **kwargs):
        '''Notifies your device the status of anything

        Generates a notification based on kwargs passed.
        All arguments are optional and the message will be generated
        on the key and value. 
        
        Examples:
            - Calling `notify(title='Notification Title', message='Notification body')`
            generates a notification like:
                'Notification Title'
                'Notification Body'

            - Calling `notify(Loss=123, Accuracy=0.9)` generates a notification like:
                'Train Status'
                'Loss: 123
                 Accuracy: 0.9'

        Attributes:
            title (string, optional): The title of the notification
            message (string, optional): The whole message to be sent
        '''
        title='Train Status'
        message = ''

        for key, value in kwargs.items():
            if key == 'title':
                title = value
            elif key == 'message':
                message = value
            else:
                message += key + ': ' + str(value) + '\n'

        try:
            if type(self.devices) is list:
                result = self.push_service.notify_multiple_devices(registration_ids=self.devices, message_title=title, message_body=message)
            else:
                result = self.push_service.notify_single_device(registration_id=self.devices, message_title=title, message_body=message)
        except Exception as e:
            print('MLNotifier', e)

if __name__ == '__main__':
    import random
    notifier = FCMNotifier(
        '<API_KEY>',
        '<DEVICE_TOKEN>'
    )
    notifier.notify(
        Loss=random.random(),
        Acc=random.random()
    )