class Switch(object):
    STATE_ON = True
    STATE_OFF = False
    
    def __init__(self):
        self.state_ = Switch.STATE_OFF

    def state(self):
        return self.state_

    def turn_on(self):
        self.state_ = Switch.STATE_ON

    def turn_off(self):
        self.state_ = Switch.STATE_OFF

    def toggle(self):
        if self.state_ == Switch.STATE_ON:
            self.state_ = Switch.STATE_OFF
        else:
            self.state_ = Switch.STATE_ON

class Lightbulb(object):
    STATE_ON = True
    STATE_OFF = False
    
    def __init__(self, switch1, switch2, accept1, accept2):
        self.switches = [switch1, switch2]
        self.accepting_states = [accept1, accept2]

    def state(self):
        return [switch.state() for switch in self.switches] == self.accepting_states
