import os

prefix_customer = 'uploads/profile/user/'


def upload_user_profile(instance, filename):
    file_base, extension = filename.split(".")
    path_file = "{0:s}.{1:s}".format(str(instance.userId.id), extension)
    return os.path.join(prefix_customer, path_file)

