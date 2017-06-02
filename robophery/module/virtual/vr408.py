from robophery.base import Module


class Vr408Module(Module):
    """
    Module for Allbot 4 legged 8 servos spider.
    """
    DEVICE_NAME = 'vr408'

    def __init__(self, *args, **kwargs):
        super(Vr408Module, self).__init__(*args, **kwargs)
        self._joint = kwargs['joint']

    def commit_action(self, action):
        if action == 'read_data':
            return self.read_data()
        elif action == 'stop':
            self.stop()
        elif action == 'forward':
            self.walk_forward(5, 200)
        elif action == 'backward':
            self.walk_backward(5, 200)
        elif action == 'turn_left':
            self.turn_left(5, 200)
        elif action == 'turn_right':
            self.turn_left(5, 200)
        elif action == 'wave_rear_left':
            self.wave_rear_left(10, 200)
        return self.read_data()

    def _move(self, joint, angle):
        self._manager._module[self._joint[joint]].commit_action('set_angle', angle)

    def _animate(self, speed):
        self._msleep(speed)

    def _delay(self, speed):
        self._msleep(speed)

    def stop(self):
        """
        Stop the tank movement.
        """
        pass

    def wave_rear_left(self, waves, speed):

        self._move("knee_rear_left", 180)
        self._animate(speed)

        for i in range(waves):
            self._move("hip_rear_left", 0)
            self._animate(speed)

            self._move("hip_rear_left", 65)
            self._animate(speed)

            self._move("hip_rear_left", 0)
            self._animate(speed)

            self._move("hip_rear_left", 45)
            self._animate(speed)

        self._move("knee_rear_left", 45)
        self._animate(speed)

    def wave_rear_right(self, waves, speed):
        self._move("knee_rear_right", 180)
        self._animate(speed)

        for i in range(waves):
            self._move("hip_rear_right", 0)
            self._animate(speed)

            self._move("hip_rear_right", 65)
            self._animate(speed)

            self._move("hip_rear_right", 0)
            self._animate(speed)

            self._move("hip_rear_right", 45)
            self._animate(speed)

        self._move("knee_rear_right", 45)
        self._animate(speed)

    def wave_front_right(self, waves, speed):

        self._move("knee_front_right", 180)
        self._animate(speed)

        for i in range(waves):
            self._move("hip_front_right", 0)
            self._animate(speed)

            self._move("hip_front_right", 65)
            self._animate(speed)

            self._move("hip_front_right", 0)
            self._animate(speed)

            self._move("hip_front_right", 45)
            self._animate(speed)

        self._move("knee_front_right", 45)
        self._animate(speed)

    def wave_front_left(self, waves, speed):
        self._move("knee_front_left", 180)
        self._animate(speed)

        for i in range(waves):
            self._move("hip_front_left", 0)
            self._animate(speed)

            self._move("hip_front_left", 65)
            self._animate(speed)

            self._move("hip_front_left", 0)
            self._animate(speed)

            self._move("hip_front_left", 45)
            self._animate(speed)

        self._move("knee_front_left", 45)
        self._animate(speed)

    def scared(self, shakes):
        self._move("knee_front_right", 0)
        self._move("knee_rear_right", 0)
        self._move("knee_front_left", 0)
        self._move("knee_rear_left", 0)
        self._animate(50)

        for i in range(shakes):
            self._move("hip_rear_right", 80)
            self._move("hip_rear_left", 10)
            self._move("hip_front_right", 10)
            self._move("hip_front_left", 80)
            self._animate(100)

            self._move("hip_rear_left", 80)
            self._move("hip_rear_right", 10)
            self._move("hip_front_left", 10)
            self._move("hip_front_right", 80)
            self._animate(50)

        self._move("hip_rear_right", 45)
        self._move("hip_rear_left", 45)
        self._move("hip_front_right", 45)
        self._move("hip_front_left", 45)
        self._animate(200)

        self._move("knee_front_right", 45)
        self._move("knee_rear_right", 45)
        self._move("knee_front_left", 45)
        self._move("knee_rear_left", 45)
        self._animate(75)

    def lean_right(self, speed):
        self._move("knee_front_right", 90)
        self._move("knee_rear_right", 90)
        self._animate(speed)

        self._delay(speed / 2)

        self._move("knee_front_right", 45)
        self._move("knee_rear_right", 45)
        self._animate(speed)

    def lean_left(self, speed):
        self._move("knee_front_left", 90)
        self._move("knee_rear_left", 90)
        self._animate(speed)

        self._delay(speed / 2)

        self._move("knee_front_left", 45)
        self._move("knee_rear_left", 45)
        self._animate(speed)

    def leanforward(self, speed):
        self._move("knee_front_left", 90)
        self._move("knee_front_right", 90)
        self._animate(speed)

        self._delay(speed / 2)

        self._move("knee_front_left", 45)
        self._move("knee_front_right", 45)
        self._animate(speed)

    def leanbackward(self, speed):
        self._move("knee_rear_left", 90)
        self._move("knee_rear_right", 90)
        self._animate(speed)

        self._delay(speed / 2)

        self._move("knee_rear_left", 45)
        self._move("knee_rear_right", 45)
        self._animate(speed)

    def look_left(self, speed):
        self._move("hip_rear_left", 80)
        self._move("hip_rear_right", 10)
        self._move("hip_front_left", 10)
        self._move("hip_front_right", 80)
        self._animate(speed)

        self._delay(speed / 2)

        self._move("hip_rear_right", 45)
        self._move("hip_rear_left", 45)
        self._move("hip_front_right", 45)
        self._move("hip_front_left", 45)
        self._animate(speed)

    def look_right(self, speed):
        self._move("hip_rear_right", 80)
        self._move("hip_rear_left", 10)
        self._move("hip_front_right", 10)
        self._move("hip_front_left", 80)
        self._animate(speed)

        self._delay(speed / 2)

        self._move("hip_rear_right", 45)
        self._move("hip_rear_left", 45)
        self._move("hip_front_right", 45)
        self._move("hip_front_left", 45)
        self._animate(speed)

    def walk_forward(self, steps, speed):
        for i in range(steps):
            self._move("knee_rear_right", 80)
            self._move("knee_front_left", 80)
            self._animate(speed)

            self._move("hip_rear_right", 80)
            self._move("hip_front_left", 20)
            self._animate(speed)

            self._move("knee_rear_right", 30)
            self._move("knee_front_left", 30)
            self._animate(speed)

            self._move("hip_rear_right", 45)
            self._move("hip_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_right", 45)
            self._move("knee_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_left", 80)
            self._move("knee_front_right", 80)
            self._animate(speed)

            self._move("hip_rear_left", 80)
            self._move("hip_front_right", 20)
            self._animate(speed)

            self._move("knee_rear_left", 30)
            self._move("knee_front_right", 30)
            self._animate(speed)

            self._move("hip_rear_left", 45)
            self._move("hip_front_right", 45)
            self._animate(speed)

            self._move("knee_rear_left", 45)
            self._move("knee_front_right", 45)
            self._animate(speed)

    def walk_backward(self, steps, speed):
        for i in range(steps):
            self._move("knee_rear_right", 80)
            self._move("knee_front_left", 80)
            self._animate(speed)

            self._move("hip_rear_right", 20)
            self._move("hip_front_left", 80)
            self._animate(speed)

            self._move("knee_rear_right", 30)
            self._move("knee_front_left", 30)
            self._animate(speed)

            self._move("hip_rear_right", 45)
            self._move("hip_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_right", 45)
            self._move("knee_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_left", 80)
            self._move("knee_front_right", 80)
            self._animate(speed)

            self._move("hip_rear_left", 20)
            self._move("hip_front_right", 80)
            self._animate(speed)

            self._move("knee_rear_left", 30)
            self._move("knee_front_right", 30)
            self._animate(speed)

            self._move("hip_rear_left", 45)
            self._move("hip_front_right", 45)
            self._animate(speed)

            self._move("knee_rear_left", 45)
            self._move("knee_front_right", 45)
            self._animate(speed)

    def walk_left(self, steps, speed):
        for i in range(steps):
            self._move("knee_rear_right", 80)
            self._move("knee_front_left", 80)
            self._animate(speed)

            self._move("hip_rear_right", 0)
            self._move("hip_front_left", 90)
            self._animate(speed)

            self._move("knee_rear_right", 30)
            self._move("knee_front_left", 30)
            self._animate(speed)

            self._move("hip_rear_right", 45)
            self._move("hip_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_right", 45)
            self._move("knee_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_left", 80)
            self._move("knee_front_right", 80)
            self._animate(speed)

            self._move("hip_rear_left", 90)
            self._move("hip_front_right", 0)
            self._animate(speed)

            self._move("knee_rear_left", 30)
            self._move("knee_front_right", 30)
            self._animate(speed)

            self._move("hip_rear_left", 45)
            self._move("hip_front_right", 45)
            self._animate(speed)

            self._move("knee_rear_left", 45)
            self._move("knee_front_right", 45)
            self._animate(speed)

    def walk_right(self, steps, speed):
        for i in range(steps):
            self._move("knee_rear_left", 80)
            self._move("knee_front_right", 80)
            self._animate(speed)

            self._move("hip_rear_left", 0)
            self._move("hip_front_right", 90)
            self._animate(speed)

            self._move("knee_rear_left", 30)
            self._move("knee_front_right", 30)
            self._animate(speed)

            self._move("hip_rear_left", 45)
            self._move("hip_front_right", 45)
            self._animate(speed)

            self._move("knee_rear_left", 45)
            self._move("knee_front_right", 45)
            self._animate(speed)

            self._move("knee_rear_right", 80)
            self._move("knee_front_left", 80)
            self._animate(speed)

            self._move("hip_rear_right", 90)
            self._move("hip_front_left", 0)
            self._animate(speed)

            self._move("knee_rear_right", 30)
            self._move("knee_front_left", 30)
            self._animate(speed)

            self._move("hip_rear_right", 45)
            self._move("hip_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_right", 45)
            self._move("knee_front_left", 45)
            self._animate(speed)

    def turn_left(self, steps, speed):
        for i in range(steps):
            self._move("knee_rear_right", 80)
            self._move("knee_front_left", 80)
            self._animate(speed)

            self._move("hip_rear_right", 90)
            self._move("hip_front_left", 90)
            self._animate(speed)

            self._move("knee_rear_right", 30)
            self._move("knee_front_left", 30)
            self._animate(speed)

            self._move("hip_rear_right", 45)
            self._move("hip_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_right", 45)
            self._move("knee_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_left", 80)
            self._move("knee_front_right", 80)
            self._animate(speed)

            self._move("hip_rear_left", 0)
            self._move("hip_front_right", 0)
            self._animate(speed)

            self._move("knee_rear_left", 30)
            self._move("knee_front_right", 30)
            self._animate(speed)

            self._move("hip_rear_left", 45)
            self._move("hip_front_right", 45)
            self._animate(speed)

            self._move("knee_rear_left", 45)
            self._move("knee_front_right", 45)
            self._animate(speed)

    def turn_right(self, steps, speed):
        for i in range(steps):
            self._move("knee_rear_right", 80)
            self._move("knee_front_left", 80)
            self._animate(speed)

            self._move("hip_rear_right", 0)
            self._move("hip_front_left", 0)
            self._animate(speed)

            self._move("knee_rear_right", 30)
            self._move("knee_front_left", 30)
            self._animate(speed)

            self._move("hip_rear_right", 45)
            self._move("hip_front_left", 45)
            self._animate(speed)

            self._move("knee_rear_right", 45)
            self._move("knee_front_left", 45)
            self._animate(speed)

        self._move("knee_rear_left", 80)
        self._move("knee_front_right", 80)
        self._animate(speed)

        self._move("hip_rear_left", 90)
        self._move("hip_front_right", 90)
        self._animate(speed)

        self._move("knee_rear_left", 30)
        self._move("knee_front_right", 30)
        self._animate(speed)

        self._move("hip_rear_left", 45)
        self._move("hip_front_right", 45)
        self._animate(speed)

        self._move("knee_rear_left", 45)
        self._move("knee_front_right", 45)
        self._animate(speed)

    def read_data(self):
        data = []
        return data

    def meta_data(self):
        """
        Get the readings meta-data.
        """
        return {}
