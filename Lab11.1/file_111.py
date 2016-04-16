class File:

    FILE_PERMISSIONS = 'rwx'

    def __init__(self, name, owner, size=0, permissions=''):
        self.name = name
        self.owner = owner
        self.size = size
        self.permissions = ''.join(sorted(permissions))

    def __str__(self):
        ret = 'File: {}\n'.format(self.name)
        ret += 'Owner: {}\n'.format(self.owner)
        ret += 'Permissions: {}\n'.format(self.get_permissions())
        ret += 'Size: {} bytes'.format(self.size)
        return ret

    def has_access(self, name, permis):
        if name == self.owner:
            return "Access granted"
        elif permis in self.permissions:
            return "Access granted"
        return "Access denied"

    def enable_permission(self, name, permis):
        if name != self.owner:
            print('Access denied')
            return

        if permis in self.FILE_PERMISSIONS and permis not in self.permissions:
            self.permissions = ''.join(sorted(self.permissions + permis))

    def disable_permission(self, name, permis):
        if name != self.owner:
            print('Access denied')
            return

        self.permissions = self.permissions.replace(permis, '')

    def get_permissions(self):
        if self.permissions == '':
            return 'null'
        else:
            return self.permissions
