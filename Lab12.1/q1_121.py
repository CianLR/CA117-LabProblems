class File:

    FILE_PERMISSIONS = 'rwx'

    def __init__(self, filename, owner, size=0, permis=''):
        self.filename = filename
        self.owner = owner
        self.size = size
        self.permissions = ''.join(sorted(permis))

    def has_access(self, name, permis):
        if name == self.owner:
            return 'Access granted'
        elif permis in self.permissions:
            return 'Access granted'
        else:
            return 'Access denied'

    def enable_permission(self, name, permis):
        if name != self.owner:
            print('Access denied')
        elif permis not in self.permissions and permis in self.FILE_PERMISSIONS:
            self.permissions = ''.join(sorted(self.permissions + permis))

    def get_permissions(self):
        return self.permissions if self.permissions else 'null'

    def disable_permission(self, name, permis):
        if name != self.owner:
            print('Access denied')
        else:
            self.permissions = self.permissions.replace(permis, '')

    def __str__(self):
        ret = 'File: ' + self.filename
        ret += '\nOwner: ' + self.owner
        ret += '\nPermissions: ' + self.get_permissions()
        ret += '\nSize: {} bytes'.format(self.size)
        return ret
