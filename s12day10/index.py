#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fram import event_drive

class MyHandler(event_drive.BaseHandler):

    def execute(self):
        print 'event-drive execute MyHandler'


event_drive.event_list.append(MyHandler)
event_drive.run()