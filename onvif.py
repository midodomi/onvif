from time import sleep

from onvif import ONVIFCamera

def perform_move(ptz, request, timeout):
    ptz.ContinuousMove(request)
    sleep(timeout)

def move(ptz, request, x, y, zoom, timeout):
    request.Velocity.PanTilt._y = y
    request.Velocity.PanTilt._x = x

    request.Velocity.Zoom._x = zoom
    perform_move(ptz, request, timeout)

def stop(ptz, request):
    print "STOP"
    ptz.Stop({'ProfileToken': request.ProfileToken})

def continuous_move():
    mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')

    media = mycam.create_media_service()
    ptz = mycam.create_ptz_service()

    media_profile = media.GetProfiles()[0];

def continuous_move():
    mycam = ONVIFCamera('192.168.13.12', 80, 'admin', 'Supervisor')

    media = mycam.create_media_service()
    ptz = mycam.create_ptz_service()

    media_profile = media.GetProfiles()[0];

    request = ptz.create_type('GetConfigurationOptions')
    request.ConfigurationToken = media_profile.PTZConfiguration._token
    ptz_configuration_options = ptz.GetConfigurationOptions(request)

    request = ptz.create_type('ContinuousMove')
    request.ProfileToken = media_profile._token

    ptz.Stop({'ProfileToken': media_profile._token})

    for i in range(1,50):
        move(ptz, request, 0.01*i, 0.01*i, 0.1*i/20, 0.15)
        print i

    for i in range (1,50):
        move(ptz, request, 0.50 - 0.01*i, -(0.50-0.01*i), 0.25-0.1*i/20, 0.15)
        print i

    for i in range(1,50):
        move(ptz, request, -0.01*i, -0.01*i, 0.50-0.01*i, 0.15)

    for i in range (1,50):
        move(ptz, request, -(0.50 - 0.01*i), 0.50 - 0.01*i, 0.1*i/20, 0.15)
        print i

    stop(ptz, request)


if __name__ == '__main__':
  continuous_move()




