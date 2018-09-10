import os
from ansible import errors


class FilterModule(object):
    def filters(self):
        return {
            'device_inode': self.device_inode,
            'format_location': self.format_location,
        }

    def device_inode(self, path):
        return os.stat(path).st_dev

    def format_location(self, format_location, count=0):
        if len(format_location.split('.')) > 4:
            raise errors.AnsibleFilterError(
                'The maximum distance between two services is 4')

        return format_location.format(str(count))
